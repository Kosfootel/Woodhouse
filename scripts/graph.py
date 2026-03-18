#!/usr/bin/env python3
"""
Woodhouse Microsoft Graph helper.
Credentials stored in macOS Keychain under account 'woodhouse'.
"""
import subprocess, httpx
from msal import ConfidentialClientApplication
from functools import lru_cache

GRAPH = "https://graph.microsoft.com/v1.0"
PRIMARY_USER = "erik_ross@hockeyops.ai"

def _keychain(service: str) -> str:
    r = subprocess.run(
        ['security', 'find-generic-password', '-a', 'woodhouse', '-s', service, '-w'],
        capture_output=True, text=True
    )
    return r.stdout.strip()

@lru_cache(maxsize=1)
def _msal_app():
    return ConfidentialClientApplication(
        _keychain("msgraph_client_id"),
        authority=f"https://login.microsoftonline.com/{_keychain('msgraph_tenant_id')}",
        client_credential=_keychain("msgraph_client_secret"),
    )

def get_token() -> str:
    result = _msal_app().acquire_token_for_client(
        scopes=["https://graph.microsoft.com/.default"]
    )
    if "access_token" not in result:
        raise RuntimeError(f"Auth failed: {result.get('error_description')}")
    return result["access_token"]

def headers() -> dict:
    return {"Authorization": f"Bearer {get_token()}"}

def get(path: str, **params) -> dict:
    url = path if path.startswith("http") else f"{GRAPH}/{path.lstrip('/')}"
    r = httpx.get(url, headers=headers(), params=params)
    r.raise_for_status()
    return r.json()

def post(path: str, body: dict) -> dict:
    url = path if path.startswith("http") else f"{GRAPH}/{path.lstrip('/')}"
    r = httpx.post(url, headers={**headers(), "Content-Type": "application/json"}, json=body)
    r.raise_for_status()
    return r.json()

def patch(path: str, body: dict) -> dict:
    url = path if path.startswith("http") else f"{GRAPH}/{path.lstrip('/')}"
    r = httpx.patch(url, headers={**headers(), "Content-Type": "application/json"}, json=body)
    r.raise_for_status()
    return r.json()

# ── Mail ──────────────────────────────────────────────────────────────────────

def get_messages(user=PRIMARY_USER, top=20, folder="inbox", unread_only=False):
    params = {
        "$top": top,
        "$orderby": "receivedDateTime desc",
        "$select": "id,subject,from,receivedDateTime,isRead,importance,bodyPreview,hasAttachments"
    }
    if unread_only:
        params["$filter"] = "isRead eq false"
    return get(f"users/{user}/mailFolders/{folder}/messages", **params).get("value", [])

def mark_read(message_id: str, user=PRIMARY_USER):
    return patch(f"users/{user}/messages/{message_id}", {"isRead": True})

def send_mail(to: str, subject: str, body: str, user=PRIMARY_USER):
    return post(f"users/{user}/sendMail", {
        "message": {
            "subject": subject,
            "body": {"contentType": "Text", "content": body},
            "toRecipients": [{"emailAddress": {"address": to}}]
        }
    })

# ── Calendar ──────────────────────────────────────────────────────────────────

def get_calendar_events(user=PRIMARY_USER, days_ahead=7):
    from datetime import datetime, timezone, timedelta
    now = datetime.now(timezone.utc)
    end = now + timedelta(days=days_ahead)
    return get(
        f"users/{user}/calendarView",
        **{
            "startDateTime": now.isoformat(),
            "endDateTime": end.isoformat(),
            "$orderby": "start/dateTime",
            "$select": "id,subject,start,end,location,organizer,isAllDay,bodyPreview",
            "$top": 50
        }
    ).get("value", [])

# ── Contacts ─────────────────────────────────────────────────────────────────

def get_contacts(user=PRIMARY_USER, top=25):
    return get(
        f"users/{user}/contacts",
        **{"$top": top, "$select": "displayName,emailAddresses,businessPhones,jobTitle,companyName"}
    ).get("value", [])

# ── Briefing ─────────────────────────────────────────────────────────────────

def morning_briefing(user=PRIMARY_USER):
    from datetime import datetime, timezone
    now = datetime.now(timezone.utc)

    unread = get_messages(user=user, top=10, unread_only=True)
    events = get_calendar_events(user=user, days_ahead=2)

    print(f"\n{'='*60}")
    print(f"  MORNING BRIEFING — {now.strftime('%A, %d %B %Y')}")
    print(f"{'='*60}")

    print(f"\n📬 UNREAD MAIL ({len(unread)} messages)")
    if unread:
        for m in unread:
            sender = m.get("from", {}).get("emailAddress", {}).get("name", "?")
            addr   = m.get("from", {}).get("emailAddress", {}).get("address", "?")
            imp    = " ⚠️" if m.get("importance") == "high" else ""
            att    = " 📎" if m.get("hasAttachments") else ""
            print(f"  • {m['receivedDateTime'][:10]} | {sender} <{addr}>{imp}{att}")
            print(f"    {m.get('subject','(no subject)')}")
    else:
        print("  Inbox clear, sir.")

    print(f"\n📅 UPCOMING EVENTS (next 48h)")
    if events:
        for e in events:
            start = e.get("start", {}).get("dateTime", "")[:16].replace("T", " ")
            loc   = e.get("location", {}).get("displayName", "")
            loc_s = f" @ {loc}" if loc else ""
            print(f"  • {start}{loc_s} — {e.get('subject','(no subject)')}")
    else:
        print("  Nothing on the calendar, sir.")

    print(f"\n{'='*60}\n")

if __name__ == "__main__":
    morning_briefing()

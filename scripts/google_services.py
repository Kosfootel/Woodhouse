#!/usr/bin/env python3
"""
Woodhouse Google services helper (Gmail, Calendar, Contacts).
Credentials stored in macOS Keychain under account 'woodhouse'.
"""
import subprocess
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

PRIMARY_ACCOUNT = "kosfootel@gmail.com"

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/calendar.events",
    "https://www.googleapis.com/auth/contacts.readonly",
]

def _keychain(service: str) -> str:
    r = subprocess.run(
        ['security', 'find-generic-password', '-a', 'woodhouse', '-s', service, '-w'],
        capture_output=True, text=True
    )
    return r.stdout.strip()

def _save_keychain(service: str, value: str):
    subprocess.run(
        ['security', 'add-generic-password', '-a', 'woodhouse', '-s', service, '-w', value, '-U'],
        capture_output=True
    )

def get_credentials() -> Credentials:
    creds = Credentials(
        token=_keychain("google_access_token"),
        refresh_token=_keychain("google_refresh_token"),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=_keychain("google_client_id"),
        client_secret=_keychain("google_client_secret"),
        scopes=SCOPES,
    )
    if creds.expired or not creds.valid:
        creds.refresh(Request())
        _save_keychain("google_access_token", creds.token)
        _save_keychain("google_token_expiry", str(creds.expiry))
    return creds

# ── Gmail ─────────────────────────────────────────────────────────────────────

def get_gmail_service():
    return build("gmail", "v1", credentials=get_credentials(), cache_discovery=False)

def get_messages(max_results=10, unread_only=True, label="INBOX"):
    svc = get_gmail_service()
    q = "is:unread" if unread_only else ""
    result = svc.users().messages().list(
        userId="me", maxResults=max_results, labelIds=[label], q=q
    ).execute()
    messages = result.get("messages", [])
    detailed = []
    for m in messages:
        msg = svc.users().messages().get(
            userId="me", id=m["id"],
            format="metadata",
            metadataHeaders=["Subject", "From", "Date"]
        ).execute()
        headers = {h["name"]: h["value"] for h in msg.get("payload", {}).get("headers", [])}
        detailed.append({
            "id": m["id"],
            "subject": headers.get("Subject", "(no subject)"),
            "from": headers.get("From", "?"),
            "date": headers.get("Date", "?"),
            "snippet": msg.get("snippet", ""),
            "labelIds": msg.get("labelIds", []),
        })
    return detailed

def mark_read(message_id: str):
    svc = get_gmail_service()
    svc.users().messages().modify(
        userId="me", id=message_id,
        body={"removeLabelIds": ["UNREAD"]}
    ).execute()

# ── Calendar ──────────────────────────────────────────────────────────────────

def get_calendar_service():
    return build("calendar", "v3", credentials=get_credentials(), cache_discovery=False)

def get_events(days_ahead=7, max_results=20):
    from datetime import datetime, timezone, timedelta
    svc = get_calendar_service()
    now = datetime.now(timezone.utc)
    end = now + timedelta(days=days_ahead)
    result = svc.events().list(
        calendarId="primary",
        timeMin=now.isoformat(),
        timeMax=end.isoformat(),
        maxResults=max_results,
        singleEvents=True,
        orderBy="startTime"
    ).execute()
    return result.get("items", [])

# ── Contacts ─────────────────────────────────────────────────────────────────

def get_contacts(max_results=25):
    svc = build("people", "v1", credentials=get_credentials(), cache_discovery=False)
    result = svc.people().connections().list(
        resourceName="people/me",
        pageSize=max_results,
        personFields="names,emailAddresses,phoneNumbers,organizations"
    ).execute()
    return result.get("connections", [])

# ── Briefing ─────────────────────────────────────────────────────────────────

def google_briefing():
    from datetime import datetime, timezone
    now = datetime.now(timezone.utc)

    unread = get_messages(max_results=10, unread_only=True)
    events = get_events(days_ahead=2)

    print(f"\n{'='*60}")
    print(f"  GOOGLE BRIEFING ({PRIMARY_ACCOUNT})")
    print(f"  {now.strftime('%A, %d %B %Y')}")
    print(f"{'='*60}")

    print(f"\n📬 UNREAD GMAIL ({len(unread)} messages)")
    if unread:
        for m in unread:
            print(f"  • {m['from'][:50]}")
            print(f"    {m['subject'][:60]}")
    else:
        print("  Gmail clear, sir.")

    print(f"\n📅 GOOGLE CALENDAR (next 48h)")
    if events:
        for e in events:
            start = e.get("start", {}).get("dateTime", e.get("start", {}).get("date", ""))[:16].replace("T", " ")
            print(f"  • {start} — {e.get('summary', '?')}")
    else:
        print("  Nothing on the calendar, sir.")

    print(f"\n{'='*60}\n")

if __name__ == "__main__":
    google_briefing()

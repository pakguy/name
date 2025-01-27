from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime
import pytz
import os

SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_credentials():
    credentials = None
    token_path = r"C:\Users\nom\Downloads\token.json"
    
    if os.path.exists(token_path):
        credentials = Credentials.from_authorized_user_file(token_path)
        
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            try:
                credentials.refresh(Request())
            except Exception as e:
                print("Error refreshing token:", e)
                credentials = None  # Reset credentials on refresh error
        else:
            flow = InstalledAppFlow.from_client_secrets_file(r"C:\Users\nom\Downloads\modules\calendar\credential.json", SCOPES)
            credentials = flow.run_local_server(port=0)
            
        if credentials:
            with open(token_path, "w") as token:
                token.write(credentials.to_json())
            
    return credentials

def create_event(event_data):
    try:
        summary = event_data['summary']
        location = event_data['location']
        description = event_data['description']
        datetime1 = event_data['datetime1']
        datetime2 = event_data['datetime2']
        timezone = 'Africa/Lagos'
        attendees = [{'email': email.strip()} for email in event_data.get('attendees', '').split(',') if email.strip()]
        
        credentials = get_credentials()
        service = build("calendar", "v3", credentials=credentials)
        
        event = {
            "summary": summary,
            "location": location,
            "description": description,
            "start": {"dateTime": datetime1.isoformat(), "timeZone": timezone},
            "end": {"dateTime": datetime2.isoformat(), "timeZone": timezone},
            "attendees": attendees
        }
        created_event = service.events().insert(calendarId="primary", body=event).execute()
        return True, created_event.get('htmlLink')
    except HttpError as error:
        return False, str(error)

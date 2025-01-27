# from google.oauth2 import service_account
# from googleapiclient.discovery import build

# # Define the necessary scopes
# SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

# # Replace 'credentials.json' with your service account credentials JSON file
# creds = service_account.Credentials.from_service_account_file('C:/Users/nom/Downloads/modules/warm-physics-421107-e4e8e1ca0e00.json', scopes=SCOPES)

# # Build the Calendar API service
# service = build('calendar', 'v3', credentials=creds)

# # Call the Calendar API to fetch the next 10 events
# events_result = service.events().list(calendarId='primary', maxResults=10, singleEvents=True, orderBy='startTime').execute()
# events = events_result.get('items', [])

# # If there are no events, print a message
# if not events:
#     print('No upcoming events found.')

# # Print the start time and summary of each event
# for event in events:
#     start = event['start'].get('dateTime', event['start'].get('date'))
#     print(start, event['summary'])


# from google.oauth2 import service_account
# from googleapiclient.discovery import build
# from datetime import datetime, timedelta

# # Define the necessary scopes
# SCOPES = ['https://www.googleapis.com/auth/calendar']

# # Replace 'credentials.json' with your service account credentials JSON file
# creds = service_account.Credentials.from_service_account_file('C:/Users/nom/Downloads/modules/warm-physics-421107-e4e8e1ca0e00.json', scopes=SCOPES)

# # Build the Calendar API service
# service = build('calendar', 'v3', credentials=creds)

# # Define event details
# event = {
#   'summary': 'Sample Event',
#   'location': 'Sample Location',
#   'description': 'This is a sample event created using Google Calendar API',
#   'start': {
#     'dateTime': datetime.now().isoformat(),
#     'timeZone': 'Africa/Lagos',  # Update with your timezone
#   },
#   'end': {
#     'dateTime': (datetime.now() + timedelta(hours=1)).isoformat(),
#     'timeZone': 'Africa/Lagos',  # Update with your timezone
#   },
#   'reminders': {
#     'useDefault': False,
#     'overrides': [
#       {'method': 'email', 'minutes': 24 * 60},  # 24 hours before the event
#       {'method': 'popup', 'minutes': 10},        # 10 minutes before the event
#     ],
#   },
# }

# # Insert event
# event = service.events().insert(calendarId='primary', body=event).execute()
# print('Event created: %s' % (event.get('htmlLink')))

# from google.oauth2 import service_account
# from googleapiclient.discovery import build
# from datetime import datetime, timedelta

# # Define the necessary scopes
# SCOPES = ['https://www.googleapis.com/auth/calendar']

# # Replace 'credentials.json' with your service account credentials JSON file
# creds = service_account.Credentials.from_service_account_file(r'C:\Users\nom\Downloads\modules\warm-physics-421107-e4e8e1ca0e00.json', scopes=SCOPES)

# # Build the Calendar API service
# service = build('calendar', 'v3', credentials=creds)

# # Define event details
# event = {
#   'summary': 'Sample Event',
#   'location': 'Sample Location',
#   'description': 'This is a sample event created using Google Calendar API',
#   'start': {
#     'dateTime': datetime.now().isoformat(),
#     'timeZone': 'Africa/Lagos',  # Update with your timezone
#   },
#   'end': {
#     'dateTime': (datetime.now() + timedelta(hours=1)).isoformat(),
#     'timeZone': 'Africa/Lagos',  # Update with your timezone
#   },
#   'reminders': {
#     'useDefault': False,
#     'overrides': [
#       {'method': 'email', 'minutes': 24 * 60},  # 24 hours before the event
#       {'method': 'popup', 'minutes': 10},        # 10 minutes before the event
#     ],
#   },
# }

# # Insert event
# event = service.events().insert(calendarId='primary', body=event).execute()
# print('Event created: %s' % (event.get('htmlLink')))

# from google.oauth2 import service_account
# from googleapiclient.discovery import build
# from datetime import datetime, timedelta
# from googleapiclient.errors import HttpError

# # Define the necessary scopes
# SCOPES = ['https://www.googleapis.com/auth/calendar']

# try:
#     # Replace 'credentials.json' with your service account credentials JSON file
#     creds = service_account.Credentials.from_service_account_file(r'C:\Users\nom\Downloads\modules\warm-physics-421107-e4e8e1ca0e00.json', scopes=SCOPES)

#     # Build the Calendar API service
#     service = build('calendar', 'v3', credentials=creds)

#     # Define event details
#     event = {
#         'summary': 'Sample Event',
#         'location': 'Sample Location',
#         'description': 'This is a sample event created using Google Calendar API',
#         'start': {
#             'dateTime': datetime.now().isoformat(),
#             'timeZone': 'Africa/Lagos',  # Update with your timezone
#         },
#         'end': {
#             'dateTime': (datetime.now() + timedelta(hours=1)).isoformat(),
#             'timeZone': 'Africa/Lagos',  # Update with your timezone
#         },
#         'reminders': {
#             'useDefault': False,
#             'overrides': [
#                 {'method': 'email', 'minutes': 24 * 60},  # 24 hours before the event
#                 {'method': 'popup', 'minutes': 10},        # 10 minutes before the event
#             ],
#         },
#     }

#     # Insert event
#     event = service.events().insert(calendarId='primary', body=event).execute()
#     print('Event created: %s' % (event.get('htmlLink')))

# except HttpError as e:
#     print(f"An error occurred: {e}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")


# from google.oauth2 import service_account
# from googleapiclient.discovery import build
# from datetime import datetime, timedelta
# from googleapiclient.errors import HttpError

# # Define the necessary scopes
# SCOPES = ['https://www.googleapis.com/auth/calendar']

# try:
#     # Replace 'credentials.json' with your service account credentials JSON file
#     creds = service_account.Credentials.from_service_account_file(r'C:\Users\nom\Downloads\modules\warm-physics-421107-e4e8e1ca0e00.json', scopes=SCOPES)

#     # Build the Calendar API service
#     service = build('calendar', 'v3', credentials=creds)

#     # Define event details
#     event = {
#         'summary': 'Sample Event',
#         'location': 'Sample Location',
#         'description': 'This is a sample event created using Google Calendar API',
#         'start': {
#             'dateTime': datetime.now().isoformat(),
#             'timeZone': 'Africa/Lagos',  # Update with your timezone
#         },
#         'end': {
#             'dateTime': (datetime.now() + timedelta(hours=1)).isoformat(),
#             'timeZone': 'Africa/Lagos',  # Update with your timezone
#         },
#         'attendees': [
#             {'email': 'divineusang511@gmail.com'}
#         ],
#         'reminders': {
#             'useDefault': False,
#             'overrides': [
#                 {'method': 'email', 'minutes': 24 * 60},  # 24 hours before the event
#                 {'method': 'popup', 'minutes': 10},        # 10 minutes before the event
#             ],
#         },
#     }

#     # Insert event
#     event = service.events().insert(calendarId='primary', body=event).execute()
#     print('Event created: %s' % (event.get('htmlLink')))

# except HttpError as e:
#     print(f"An error occurred: {e}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def main():
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "C:/Users/nom/Downloads/modules/calendar/credential.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    print("Getting the upcoming 10 events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return

    # Prints the start and name of the next 10 events
    for event in events:
      start = event["start"].get("dateTime", event["start"].get("date"))
      print(start, event["summary"])

  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()
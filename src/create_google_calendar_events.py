import datetime
import ast
from prompt import prompt
from chatgpt import *
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import dotenv
dotenv.load_dotenv()

import os

# Path to your credentials.json file
cwd = os.getcwd()
SERVICE_ACCOUNT_FILE = os.path.join(cwd, 'creds.json')

# Define the scopes required
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Authenticate and create the service
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('calendar', 'v3', credentials=creds)

# Define the calendar ID (use 'primary' for the primary calendar)
CALENDAR_ID = os.getenv("CALENDAR_ID")

# Helper function to convert date and time
def get_datetime(date_str, time_str):
    date_time_str = f"{date_str} {time_str}"
    dt = datetime.datetime.strptime(date_time_str, '%b %d, %Y %I:%M:%S %p')
    # Convert to ISO format with UTC offset (for PST use -07:00)
    return dt.astimezone(datetime.timezone(datetime.timedelta(hours=-7))).isoformat()


# Helper function to find and delete conflicting events
def delete_conflicting_events(start_datetime, end_datetime):
    try:
        events_result = service.events().list(
            calendarId=CALENDAR_ID,
            timeMin=start_datetime,
            timeMax=end_datetime,
            singleEvents=True,
            orderBy='startTime'
        ).execute()

        events = events_result.get('items', [])
        for event in events:
            event_id = event['id']
            print(f"Deleting conflicting event: {event.get('summary')} ({event_id})")
            service.events().delete(calendarId=CALENDAR_ID, eventId=event_id).execute()
    except HttpError as error:
        print(f"An error occurred while deleting events: {error}")


def Handler():
    
    cwd = os.getcwd()
    filename = 'last_prompt.json'
    
    if os.path.isfile(os.path.join(cwd, filename)):
        print('Uploading last schedule to local knowledge . . .')
        upload_to_knowledge(filename)
    
    print('Creating schedule...')
    schedule = ast.literal_eval(get_response(prompt))
    print('Schedule complete!')
    
    print('Writing the new schedule to JSON...')
    write_local_file(schedule, filename)
    
    print('Creating events in Google Calendar...')
    # Create events
    for event in schedule:
        start_datetime = get_datetime(event['date'], event['start_time'])
        end_datetime = get_datetime(event['date'], event['end_time'])

        # Debugging: print the date times
        print(f"Start: {start_datetime}, End: {end_datetime}")

        # Delete conflicting events
        delete_conflicting_events(start_datetime, end_datetime)

        event_body = {
            'summary': event['event'],
            'start': {
                'dateTime': start_datetime,
                'timeZone': 'America/Los_Angeles',  # PST time zone
            },
            'end': {
                'dateTime': end_datetime,
                'timeZone': 'America/Los_Angeles',  # PST time zone
            },
            'colorId': str(event['colorId']),
        }

        # Create the event
        try:
            created_event = service.events().insert(calendarId=CALENDAR_ID, body=event_body).execute()
            print(f"Event created: {created_event.get('htmlLink')}")
        except HttpError as error:
            print(f"An error occurred while creating event: {error}")
            
    print('Schedule created successfully!')


if __name__ == '__main__':
    Handler()

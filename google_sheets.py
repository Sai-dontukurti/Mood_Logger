#%%
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Scope tells Google what APIs we're accessing
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

# Load credentials from the JSON file
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

# Connect to the Google Sheets API
client = gspread.authorize(credentials)

# Replace this with your actual sheet name
SHEET_NAME = "MoodLogger"

# Get the sheet (first worksheet)
def get_worksheet():
    return client.open(SHEET_NAME).sheet1

# Append a new mood entry to the sheet
def append_mood(mood, note):
    sheet = get_worksheet()
    timestamp = datetime.now().isoformat()
    sheet.append_row([timestamp, mood, note])

# Get today's mood entries as a DataFrame
def get_today_moods():
    sheet = get_worksheet()
    records = sheet.get_all_records()
    df = pd.DataFrame(records)

    # Convert timestamp to datetime
    print("Columns from sheet:", df.columns.tolist())

    #df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='ISO8601')


    # Filter for today only
    today = pd.Timestamp.now().normalize()
    return df[df['timestamp'] >= today]

if __name__ == "__main__":
    sheet = get_worksheet()
    records = sheet.get_all_records()
    df = pd.DataFrame(records)

    print("Raw sheet records:", records)
    print("DataFrame columns:", df.columns.tolist())
    print("DataFrame preview:\n", df.head())


# %%

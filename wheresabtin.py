
from pprint import pprint
from googleapiclient import discovery
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import json
from datetime import datetime, timedelta
import time
credentials = None

service = discovery.build('sheets', 'v4', credentials=credentials)

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a the Where's Abtin? sheet.
SPREADSHEET_ID = '1C-LRmuPGuMtBscI7_qh7FvTZds8Sr_uIj9GIRiTezy8'
RANGE_ = 'A1:B'

def retrieve():
    '''calling sheets api and writing to text file.'''
    request = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_,majorDimension='ROWS')
    response = request.execute()
    locationEntries = response["values"]
    for entry in locationEntries[-5:-1]: # data cleanup for txt file writing
        stringified=entry[0] + " " + entry[1] + "\n"
        file = open("test.txt", "a")
        file.write(stringified)
        file.close()

def main():
    while True:
        dt = datetime.now() + timedelta(hours=1)
        while datetime.now() < dt:
            time.sleep(1)
        retrieve()
        #TODO: write to serial port

if __name__ == '__main__':
    main()
    
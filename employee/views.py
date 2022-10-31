from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

# Create your views here.

def index(request):
    global values
    output = values
    template = loader.get_template('index.html')
    return HttpResponse(output)

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)

SAMPLE_SPREADSHEET_ID = '14x6TJYkXVH5tX4YFDVjvfNuiceKepPQgAknQcXi_XiE'


try:
    global values
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range='Sheet1!A1:B8').execute()
    values = result.get('values', [])
    print(values)
    print('hi')

except HttpError as err:
    print(err)

try:
    aoa = [['a',1],['b',2],['c',3]]
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='Sheet2!B2', valueInputOption='USER_ENTERED', body={"values":aoa}).execute()
except HttpError as err:
    print(err)




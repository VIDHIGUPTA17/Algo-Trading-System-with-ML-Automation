# sheets_logging/sheets_client.py
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class SheetsClient:
    def __init__(self, cred_file, sheet_id):
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(cred_file, scope)
        self.client = gspread.authorize(creds)
        self.sheet = self.client.open_by_key(sheet_id)
    def append_trade(self, row):
        self.sheet.worksheet('Sheet1').append_row(row)
    def update_summary(self, pnl, win_ratio):
        ws = self.sheet.worksheet('summary')
        ws.update('A2', [[pnl, win_ratio]])

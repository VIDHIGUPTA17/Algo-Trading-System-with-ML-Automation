
import os
from dotenv import load_dotenv
from sheets_client import SheetsClient

load_dotenv()

def log_trades(trades, pnl, win_ratio):
    credentials_path = os.getenv("SHEETS_CREDENTIALS_PATH")
    spreadsheet_id = os.getenv("SHEETS_SPREADSHEET_ID")

    sc = SheetsClient(credentials_path, spreadsheet_id)
    for t in trades:
        sc.append_trade([t[0].strftime('%Y-%m-%d'), t[1], t[2], t[3]])
    sc.update_summary(pnl, win_ratio)


import gspread
from google.oauth2.service_account import Credentials

import os
#from dotenv import load_dotenv,dotenv_values

scopes = [ "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("/etc/secrets/cred.json", scopes=scopes)#for deployment
#creds = Credentials.from_service_account_file("cred.json", scopes=scopes)#local development
client = gspread.authorize(creds)

#sheet_id=os.getenv("GOOGLE_SHEET_ID")
sheet_id = "1v21AGPdkgt_TAC9y9XfVI5Hztr2JXPn6KF9QXo53l50"

spreadsheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}"
sheet = client.open_by_url(spreadsheet_url).sheet1


def add_row_to_sheet(values):
    
        # מציאת השורה הבאה הפנויה
    next_row = len(sheet.get_all_values()) + 1
        
        # אם הרשימה היא רשימה של רשימות (כמה עמודות)
    if isinstance(values[0], list):
        sheet.insert_rows(values, next_row)
        # אם הרשימה היא רשימה פשוטה (עמודה אחת)
    else:
        sheet.insert_row(values, next_row)
            
    #     print(f"נוספה שורה חדשה במיקום: {next_row}")
    # except Exception as e:
    #     print(f"שגיאה בהוספת השורה: {e}")


# הוספת כמה שורות בבת אחת
# row =  ["שורה1-ערך1", "שורה1-ערך2", "שורה1-ערך3"]
# add_row_to_sheet(row)

def return_data():
    data=sheet.get_all_records()
    return data
    

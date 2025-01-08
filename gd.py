
import gspread
from google.oauth2.service_account import Credentials

import os
#from dotenv import load_dotenv,dotenv_values

scopes = [ "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"]
#creds = Credentials.from_service_account_file("/etc/secrets/cred.json", scopes=scopes)#for deployment
creds = Credentials.from_service_account_file("cred.json", scopes=scopes)#local development
client = gspread.authorize(creds)

#sheet_id=os.getenv("GOOGLE_SHEET_ID")
sheet_id = "1v21AGPdkgt_TAC9y9XfVI5Hztr2JXPn6KF9QXo53l50"

spreadsheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}"
spreadsheet = client.open_by_url(spreadsheet_url)

sheet1 = client.open_by_url(spreadsheet_url).sheet1
sheet2 = spreadsheet.worksheet('Sheet2')

next_row=-1

# def add_row_to_sheet(values):
    
#         # מציאת השורה הבאה הפנויה
#     global next_row
#     if next_row==-1:
#         next_row = len(sheet.get_all_values()) + 1
     
#         # אם הרשימה היא רשימה של רשימות (כמה עמודות)
#     if isinstance(values[0], list):
#         sheet.insert_rows(values, next_row)
#         # אם הרשימה היא רשימה פשוטה (עמודה אחת)
#     else:
#         sheet.insert_row(values, next_row)
            
    #     print(f"נוספה שורה חדשה במיקום: {next_row}")
    # except Exception as e:
    #     print(f"שגיאה בהוספת השורה: {e}")


# הוספת כמה שורות בבת אחת
# row =  ["שורה1-ערך1", "שורה1-ערך2", "שורה1-ערך3"]
# add_row_to_sheet(row)

def return_data():
    sheet1 = client.open_by_url(spreadsheet_url).sheet1
    data=sheet1.get_all_records()
    return data

# def init_sheet_raw():
#     global next_row
#     next_row = len(sheet.get_all_values()) + 1
    
# def write_next_column(value):
#     """
#     כותבת ערך לעמודה הבאה הפנויה באותה שורה.
#     """
#     global next_row

#     # וודא ש-next_row מאותחל כראוי
#     if next_row < 1:
#         raise ValueError("next_row must be initialized and greater than 0")

#     # קבלת הערכים בשורה הנוכחית
#     row_values = sheet.row_values(next_row)

#     # חישוב העמודה הבאה הפנויה
#     next_column_index = len(row_values) + 1

#     # כתיבה לעמודה הבאה הפנויה
#     sheet.update_cell(next_row, next_column_index, value)
    
    
    
    ####try 
#     init_sheet_raw()
#     write_next_column("ערך חדש")
# write_next_column("עוד ערך")


# old: 4/1/25
def add_row_to_sheet(values):
        # מציאת השורה הבאה הפנויה
    global next_row
    next_row = len(sheet1.get_all_values()) + 1
     
        # אם הרשימה היא רשימה של רשימות (כמה עמודות)
    if isinstance(values[0], list):
        sheet1.insert_rows(values, next_row)
        # אם הרשימה היא רשימה פשוטה (עמודה אחת)
    else:
        sheet1.insert_row(values, next_row)

def return_next_row():
    next_row = len(sheet1.get_all_values())+ 1
    return next_row

def column_letter(column_index):
    letter = ""
    while column_index > 0:
        column_index, remainder = divmod(column_index - 1, 26)
        letter = chr(65 + remainder) + letter
    return letter

def add_data_to_the_row(row,values):
    last_column = column_letter(sheet1.col_count)
    sheet1.update(f'A{row}:{last_column}{row}', [['' for _ in range(sheet1.col_count)]])

    sheet1.insert_row(values, row)
    # num_columns = len(sheet1.row_values(1))
    # sheet1.update(f'A{row}:ZZ{row}', [values + [''] * (num_columns - len(values))])


        
def add_row_to_sheet2(values):
    #sheet2=client.open_by_url(spreadsheet_url).sheet2
    sheet2 = spreadsheet.worksheet('Sheet2')

        # מציאת השורה הבאה הפנויה
    global next_row
    next_row = len(sheet2.get_all_values()) + 1
     
        # אם הרשימה היא רשימה של רשימות (כמה עמודות)
    if isinstance(values[0], list):
        sheet2.insert_rows(values, next_row)
        # אם הרשימה היא רשימה פשוטה (עמודה אחת)
    else:
        sheet2.insert_row(values, next_row)



# add_row_to_sheet("hey")
# add_row_to_sheet("hey2")
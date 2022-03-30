import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('divine_cakes')


def get_sales_figures():	
    """
    Retrieve sales figures input from the operator in
    the terminal.
    """
    print("Please enter sales figures from last trading day")
    print("Enter seven figures separated by commas")
    print("For Example:10,20,30,40,50,60,70\n")

    figures_str = input("Enter Figures here:\n")
    print(f"The figures provided are {figures_str}")
  
get_sales_figures() 
        
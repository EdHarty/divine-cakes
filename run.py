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
    
    sales_figures = figures_str.split(",")
    validate_figures(sales_figures)
    
  
def validate_figures(values):
    """
    Within the try statement, all string values are converted to
    integers. If str aren't converted to int or 7 values are not 
    entered ValueError appears.
    """
    try:
        if len(values) != 7:
            raise ValueError(
                f"7 values required, you entered {len(values)}"
            )
    except ValueError as e:
        print(f"Incorrect entry: {e}, Please re-enter data.\n")

get_sales_figures() 
        
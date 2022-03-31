import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    the terminal throught the use of a while loop to 
    collect a valid string of seven figures separated 
    using commas. The string will end when entries are valid.
    """
    while True:
        print("Please enter sales figures from the last trading day")
        print("Enter seven figures separated by commas")
        print("For Example:10,20,30,40,50,60,70\n")

        figures_str = input("Enter Figures here:\n")
        
        sales_figures = figures_str.split(",")
        
        if validate_figures(sales_figures):
            print("Figures are valid.")
            break

    return sales_figures
    
  
def validate_figures(values):
    """
    Within the try statement, all string values are converted to
    integers. If str aren't converted to int or 7 values are not 
    entered ValueError appears.
    """
    try:
        [int(value) for value in values]
        if len(values) != 7:
            raise ValueError(
                f"7 values required, you entered {len(values)}"
            )
    except ValueError as e:
        print(f"Incorrect entry: {e}, Please re-enter figures.\n")
        return False

    return True
    
     
#def revise_sales_worksheet(figures):
 #   """
  #  Revise sales worksheet. New row of figures added.
   # """
   # print("revising sales worksheet...\n")
    #sales_worksheet = SHEET.worksheet("sales")
    #sales_worksheet.append_row(figures)
    #print("Sales worksheet revised.\n")


#def revise_surplus_worksheet(figures):
  #  """
   # Revise surplus worksheet. New row of figures added.
   # """
   # print("revising surplus worksheet...\n")
    #surplus_worksheet = SHEET.worksheet("surplus")
    #surplus_worksheet.append_row(figures)
    #print("Surplus worksheet revised.\n")


def revise_worksheet(figures, worksheet):
    """
    Latest figures added to appropriate sheet.
    """  
    print(f"revising {worksheet} worksheet...\n")
    worksheet_to_revise = SHEET.worksheet(worksheet)
    worksheet_to_revise.append_row(figures)
    print(f"{worksheet} worksheet revised.\n")


def calc_surplus_figures(sales_line):
    """
    Calculation for surplus. Sales-stock = surplus.
    A positive number shows excess was made.
    A negative number shows more cakes had to be made.
    """
    print("Calculating surplus figures...\n")
    stock = SHEET.worksheet("stock").get_all_values() 
    stock_line = stock[-1] 
    
    surplus_figures = []
    for stock, sales in zip(stock_line, sales_line):
        surplus = int(stock) - sales
        surplus_figures.append(surplus)
    
    return surplus_figures


def get_last_7_days_sales():
    """
    Gathers last 7 entries of figures from sales
    worksheet and presents as a list of lists.
    """
    sales = SHEET.worksheet("sales")
    
    colss = []
    for prn in range(1, 8):
        cols = sales.col_values(prn)
        colss.append(cols[-7:])
    
    return colss
        


def main():
    """
    Run functions.
    """
    figures = get_sales_figures()
    sales_figures = [int(num) for num in figures]
    revise_worksheet(sales_figures, "sales")
    current_surplus_figures = calc_surplus_figures(sales_figures)
    revise_worksheet(current_surplus_figures, "surplus")


print("Welcome to Divine Cakes")
# main()

sales_colss = get_last_7_days_sales()
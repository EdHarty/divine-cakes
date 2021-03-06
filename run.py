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
    the terminal throught the use of a while loop to 
    collect a valid string of seven figures separated 
    using commas. The string will end when entries are valid.
    """
    while True:
        print("Please enter sales figures from the last trading day.")
        print("Enter seven figures, each figure followed by a comma.")
        print("For Example:11,12,13,14,15,16,17.\n")

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
        print("Incorrect entry, Please re-enter figures.\n")
        return False

    return True


def revise_worksheet(figures, worksheet):
    """
    Latest figures added to appropriate sheet.
    """  
    print(f"revising {worksheet} worksheet...\n")
    worksheet_to_revise = SHEET.worksheet(worksheet)
    worksheet_to_revise.append_row(figures)
    print(f"{worksheet} worksheet revised view sheet at @ https://docs.google.com/spreadsheets/d/1dzgowTky9C5rmM2fRvdcFUReOVek7PjSfj04gYTDNio/edit?usp=sharing.\n")


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


def calc_stock_figures(figures):
    """
    Calculate the average stock needed for each cake,
    Increasing by 15%.
    """
    print("Calculating stock figures...\n")
    current_stock_figures = []

    for col in figures:
        int_col = [int(num) for num in col]
        ave = sum(int_col) / len(int_col)
        stock_num = ave * 1.15
        current_stock_figures.append(round(stock_num))

    return current_stock_figures
        

def main():
    """
    Run functions.
    """
    figures = get_sales_figures()
    sales_figures = [int(num) for num in figures]
    revise_worksheet(sales_figures, "sales")
    current_surplus_figures = calc_surplus_figures(sales_figures)
    revise_worksheet(current_surplus_figures, "surplus")
    sales_colss = get_last_7_days_sales()
    stock_figures = calc_stock_figures(sales_colss)
    revise_worksheet(stock_figures, "stock")


print("Welcome to Divine Cakes, a command line Data Automation programme.")
main()


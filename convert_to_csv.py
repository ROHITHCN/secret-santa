import pandas as pd

def convert_xlsx_to_csv(xlsx_file):
    # Load the .xlsx file
    data = pd.read_excel(xlsx_file)
    
    # Convert the data to a .csv file
    csv_file = xlsx_file.replace('.xlsx', '.csv')
    data.to_csv(csv_file, index=False)
    
    return csv_file

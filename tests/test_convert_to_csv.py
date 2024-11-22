import unittest
import os
from convert_to_csv import convert_xlsx_to_csv
import pandas as pd

class TestConvertToCSV(unittest.TestCase):
    def setUp(self):
        # Mock .xlsx file path for testing
        self.xlsx_file = 'data/test_employee.xlsx'
        self.csv_file = self.xlsx_file.replace('.xlsx', '.csv')
        
        # Creating mock xlsx file for testing
        data = {'Employee_Name': ['Alice', 'Bob'], 'Employee_EmailID': ['alice@example.com', 'bob@example.com']}
        pd.DataFrame(data).to_excel(self.xlsx_file, index=False)
        
    def tearDown(self):
        # Remove generated files after tests
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)
        if os.path.exists(self.xlsx_file):
            os.remove(self.xlsx_file)

    def test_convert_xlsx_to_csv(self):
        csv_file = convert_xlsx_to_csv(self.xlsx_file)
        self.assertTrue(os.path.exists(csv_file))
        self.assertEqual(csv_file, self.csv_file)

if __name__ == '__main__':
    unittest.main()

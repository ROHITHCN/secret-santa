import unittest
from main import read_employees_from_xlsx, read_previous_assignments_from_xlsx, write_assignments_to_csv
import os
import pandas as pd

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.employee_file = 'data/test_employee.xlsx'
        self.previous_assignments_file = 'data/test_previous_assignments.xlsx'
        self.output_file = 'data/test_output.csv'

        # Create mock data for testing
        pd.DataFrame([
            {'Employee_Name': 'Alice', 'Employee_EmailID': 'alice@example.com'},
            {'Employee_Name': 'Bob', 'Employee_EmailID': 'bob@example.com'}
        ]).to_excel(self.employee_file, index=False)
        
        pd.DataFrame([
            {'Employee_Name': 'Alice', 'Employee_EmailID': 'alice@example.com', 'Secret_Child_Name': 'Bob', 'Secret_Child_EmailID': 'bob@example.com'}
        ]).to_excel(self.previous_assignments_file, index=False)

    def tearDown(self):
        # Cleanup test files
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        if os.path.exists(self.employee_file):
            os.remove(self.employee_file)
        if os.path.exists(self.previous_assignments_file):
            os.remove(self.previous_assignments_file)

    def test_read_employees_from_xlsx(self):
        employees = read_employees_from_xlsx(self.employee_file)
        self.assertEqual(len(employees), 2)
        self.assertEqual(employees[0]['employee_name'], 'Alice')
        self.assertEqual(employees[1]['employee_name'], 'Bob')

    def test_read_previous_assignments_from_xlsx(self):
        previous_assignments = read_previous_assignments_from_xlsx(self.previous_assignments_file)
        self.assertEqual(len(previous_assignments), 1)
        self.assertEqual(previous_assignments[0]['employee_name'], 'Alice')
        self.assertEqual(previous_assignments[0]['secret_child_name'], 'Bob')

    def test_write_assignments_to_csv(self):
        assignments = [
            {'employee_name': 'Alice', 'employee_email': 'alice@example.com', 'secret_child_name': 'Bob', 'secret_child_email': 'bob@example.com'}
        ]
        write_assignments_to_csv(assignments, self.output_file)
        self.assertTrue(os.path.exists(self.output_file))

if __name__ == '__main__':
    unittest.main()

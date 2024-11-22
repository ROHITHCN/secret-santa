import unittest
from main import SecretSanta

class TestSecretSanta(unittest.TestCase):
    def setUp(self):
        # Mock data for employees and previous assignments
        self.employees = [
            {'employee_name': 'Alice', 'employee_email': 'alice@example.com'},
            {'employee_name': 'Bob', 'employee_email': 'bob@example.com'},
            {'employee_name': 'Charlie', 'employee_email': 'charlie@example.com'},
            {'employee_name': 'David', 'employee_email': 'david@example.com'}
        ]
        
        self.previous_assignments = [
            {'employee_name': 'Alice', 'employee_email': 'alice@example.com', 'secret_child_name': 'Bob', 'secret_child_email': 'bob@example.com'},
            {'employee_name': 'Bob', 'employee_email': 'bob@example.com', 'secret_child_name': 'Charlie', 'secret_child_email': 'charlie@example.com'},
            {'employee_name': 'Charlie', 'employee_email': 'charlie@example.com', 'secret_child_name': 'David', 'secret_child_email': 'david@example.com'},
            {'employee_name': 'David', 'employee_email': 'david@example.com', 'secret_child_name': 'Alice', 'secret_child_email': 'alice@example.com'}
        ]

    def test_generate_derangement(self):
        secret_santa = SecretSanta(self.employees, self.previous_assignments)
        n = len(self.employees)
        derangement = secret_santa.generate_derangement(n)
        
        # Assert each index has been assigned to a different index
        for i in range(n):
            self.assertNotEqual(i, derangement[i])

    def test_assign_secret_santas(self):
        secret_santa = SecretSanta(self.employees, self.previous_assignments)
        assignments = secret_santa.assign_secret_santas()
        
        # Check if each employee has a unique Secret Santa assignment
        assigned_children = {assignment['secret_child_email'] for assignment in assignments}
        self.assertEqual(len(assigned_children), len(self.employees))
        
        # Check no one is assigned the same child as last year
        for assignment in assignments:
            prev_child = next(
                (prev['secret_child_email'] for prev in self.previous_assignments if prev['employee_email'] == assignment['employee_email']),
                None
            )
            self.assertNotEqual(prev_child, assignment['secret_child_email'])

if __name__ == '__main__':
    unittest.main()

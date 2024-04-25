class HRManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee_id, name, position, department, salary):
        if employee_id in self.employees:
            return False
        self.employees[employee_id] = {'name': name, 'position': position, 'department': department, 'salary': salary}
        return True

    def remove_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            return True
        return False

    def update_employee(self, employee_id, employee_data):
        if employee_id in self.employees:
            self.employees[employee_id].update(employee_data)
            return True
        return False

    def get_employee(self, employee_id):
        return self.employees.get(employee_id, False)

    def list_employees(self):
        return self.employees

if __name__ == '__main__':
    import unittest

    class HRManagementSystemTestAddEmployee(unittest.TestCase):
        # Add Employee Test Cases

    class HRManagementSystemTestRemoveEmployee(unittest.TestCase):
        # Remove Employee Test Cases

    class HRManagementSystemTestUpdateEmployee(unittest.TestCase):
        # Update Employee Test Cases

    class HRManagementSystemTestGetEmployee(unittest.TestCase):
        # Get Employee Test Cases

    class HRManagementSystemTestListEmployees(unittest.TestCase):
        # List Employees Test Cases

    class HRManagementSystemTestMain(unittest.TestCase):
        # Main Test Cases

    unittest.main()

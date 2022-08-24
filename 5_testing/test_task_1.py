from task_1_testing_workshop import *
import datetime
from datetime import date
import unittest


class TestUser(unittest.TestCase):

    def test_payroll_date(self):
        """ Test if payroll day is today """
        pay_roll = PayrollCalculator(payroll_date=date.today().strftime("%Y-%m-%d"))
        result = pay_roll.date
        self.assertEqual(result, '2022-07-04', "The date have to be today")

    def test_employee_information(self):
        """ Test employee id, name and salary """
        employee = SalaryEmployee(employee_id=1, name="Justinas", salary=100)
        self.assertEqual(employee.id, 1, "Employee's ID is 1")
        self.assertEqual(employee.name, 'Justinas', "Employee's name is Justinas")
        self.assertEqual(employee.salary, 100, "Employee's salary is 100")

    def test_loyal_employee_information(self):
        """ Test employee id, name and salary """
        loyal_employee = LoyalEmployee(employee_id=3, name="Albertas", salary=300, loyalty_percent=5)
        self.assertEqual(loyal_employee.id, 3, "Employee's ID is 3")
        self.assertEqual(loyal_employee.name, 'Albertas', "Employee's name is Albertas")
        self.assertEqual(loyal_employee.salary, 300, "Employee's salary is 300")
        self.assertEqual(loyal_employee.loyalty_percent, 5, "Employee's salary is 5")

    def test_loyal_employee_salary(self):
        employee = HourlyEmployee(employee_id=1, name='A', hourly_rate=10, hours_worked=200)
        result = employee.calculate_earnings()
        self.assertEqual(result, 2000, "Salary does not match")

    def test_loyal_employee_salary_second(self):
        result = hourly_employee.calculate_earnings()
        self.assertEqual(result, 800, "Salary does not match")

    def test_payroll_information_for_many_employees(self):
        calculator = PayrollCalculator(payroll_date=date.today())
        result = calculator.calculate_payroll(employees=[salary_employee, hourly_employee])
        self.assertEqual(result[0]['name'], 'Justinas', "Salary does not match")
        self.assertEqual(result[0]['salary'], 100, "Salary does not match")
        self.assertEqual(result[1]['name'], 'Ne Gytis', "Salary does not match")
        self.assertEqual(result[1]['salary'], 800, "Salary does not match")


if __name__ == '__main__':
    unittest.main()

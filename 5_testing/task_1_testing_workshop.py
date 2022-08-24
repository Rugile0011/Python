from datetime import date
from abc import ABC, abstractmethod
import datetime
import unittest


class Employee(ABC):

    def __init__(self, employee_id: int, name: str):
        self.id = employee_id
        self.name = name

    @abstractmethod
    def calculate_earnings(self) -> int:
        raise NotImplementedError("Must implement")


class SalaryEmployee(Employee):

    def __init__(self, employee_id: int, name: str, salary: int):
        super().__init__(employee_id, name)
        self.salary = salary

    def calculate_earnings(self) -> int:
        return self.salary


class LoyalEmployee(SalaryEmployee):

    def __init__(self, employee_id: int, name: str, salary: int, loyalty_percent: int):
        super().__init__(employee_id, name, salary)
        self.loyalty_percent = loyalty_percent

    def calculate_earnings(self) -> int:
        earnings = super().calculate_earnings()
        return round(earnings * (1 + self.loyalty_percent / 100))


class HourlyEmployee(Employee):
    def __init__(self, employee_id: int, name: str, hourly_rate: int, hours_worked: int):
        super().__init__(employee_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_earnings(self) -> int:
        return self.hours_worked * self.hourly_rate


class PayrollCalculator:
    def __init__(self, payroll_date: date):
        self.date = payroll_date

    def calculate_payroll(self, employees: list[SalaryEmployee | HourlyEmployee | LoyalEmployee]):
        print(f"initiating function for {self.date}")
        calculated_payroll = []
        for employee in employees:
            calculated_payroll.append({
                'name': employee.name,
                'salary': employee.calculate_earnings(),
                'date': self.date.strftime("%Y-%m-%d")
            }
            )
        return calculated_payroll


salary_employee = SalaryEmployee(employee_id=1, name="Justinas", salary=100)
hourly_employee = HourlyEmployee(employee_id=2, name="Ne Gytis", hourly_rate=20, hours_worked=40)
loyal_employee = LoyalEmployee(employee_id=3, name="Albertas", salary=300, loyalty_percent=5)

payroll = PayrollCalculator(date.today())
# payroll.calculate_payroll([salary_employee, hourly_employee, loyal_employee])
print(payroll.calculate_payroll([salary_employee, hourly_employee, loyal_employee]))



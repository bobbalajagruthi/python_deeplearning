class Employee:
  EmployeeCount = 0
  TotalSalary = 0
  def __init__(self, name, family, department, salary):
    self.name = name
    self.family = family
    self.salary = salary
    self.department = department
    Employee.EmployeeCount += 1
    Employee.TotalSalary += salary
  def avgSalary(self):
#gives the employee count
    print("Employee Count",Employee.EmployeeCount)
#gives the average salary
    print('Total average salary is ', Employee.TotalSalary/Employee.EmployeeCount)
#instance of a class
class FulltimeEmployee(Employee):
  def __init__(self, name, family, department, salary):
    super(FulltimeEmployee, self).__init__(name, family, department, salary)
#calling instance of a class
emp1 = FulltimeEmployee('Jaggu', 'B', 'Software', 3000)
emp2 = FulltimeEmployee('Jagruthi', 'B', 'Backend', 6000)
emp3 = FulltimeEmployee('Bobbala', 'B', 'forntend', 9000)
#average salary
emp1.avgSalary()

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
    print(Employee.EmployeeCount)
    print('Total average salary is ', Employee.TotalSalary/Employee.EmployeeCount)


class FulltimeEmployee(Employee):
  def __init__(self, name, family, department, salary):
    super(FulltimeEmployee, self).__init__(name, family, department, salary)

emp1 = FulltimeEmployee('Jaggu', 'B', 'Software', 3000)
emp2 = FulltimeEmployee('Jagruthi', 'B', 'Backend', 6000)
emp3 = FulltimeEmployee('Bobbala', 'B', 'forntend', 9000)

emp1.avgSalary()

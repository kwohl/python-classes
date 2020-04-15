class Employee:

    def __init__(self, name, job_title, start_date):
        self.name = name
        self.job_title = job_title
        self.start_date = start_date

class Company:

    def __init__(self, business_name, address, industry_type):
        self.business_name = business_name
        self.address = address
        self.industry_type = industry_type
        self.employees = []

    def hire(self, employee):
        self.employees.append(employee)

    def employee_roster(self):
        print(f"{self.business_name} is in the {self.industry_type} industry and has the following employees:")
        for employee in self.employees:
            print(f"    *{employee.name}")

acme_explosives = Company("Acme Explosives", "123 Dynamite Street", "chemical")
jetways = Company("Jetways", "123 Sky Blvd", "transportation")

michael = Employee("Michael Chang", "President", "April 14, 2020")
martina = Employee("Martina Navritilova", "CEO", "April 14, 2020")
serena = Employee("Serena Williams", "Queen", "April 14, 2020")
roger = Employee("Roger Federer", "Executive Chef", "April 14, 2020")
pete = Employee("Pete Sampras", "Administrative Assistant", "April 14, 2020")


acme_explosives.hire(michael)
acme_explosives.hire(martina)
acme_explosives.employee_roster()

print()

jetways.hire(serena)
jetways.hire(roger)
jetways.hire(pete)
jetways.employee_roster()
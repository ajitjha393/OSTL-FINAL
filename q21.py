'''
For packages question we have to create various folders and then import all functions
for viewing the package folder directory go to this google drive link

https://drive.google.com/drive/folders/1gK4I5LDGctW0Em4fvQcQS_hSvSK2Sf5D
'''

from package_Details.sub_package_account.salary import *
from package_Details.sub_package_employee.profile import *
from package_Details.sub_package_employee.qualification import *

class Employee(object):
    def __init__(self,name,age,dob,degree,experience):
        self.name = name
        self.age = age
        self.dob = dob
        self.degree = degree
        self.experience = experience

    def display_details(self):
        print('Name = {} \n Age =  {} \n DOB =  {}'.format(*get_profile(self)))
        print('Degree = {} \n Experience = {} '.format(*get_qualifications(self)))

class Account(object):
    def __init__(self,pf,basic_pay,hra):
        self.pf = pf
        self.basic_pay = basic_pay
        self.hra = hra

    def calculate_salary(self):
        return get_basic(self) + get_hra(self) - get_pf(self)

emp = Employee('Emp-1',19,'27-05-2000','Bsc',5)
emp.display_details()

acc = Account(4000,36000,2500)
print('Salary = ',acc.calculate_salary())
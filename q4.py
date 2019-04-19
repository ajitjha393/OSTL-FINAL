class Employee(object):
    #--Class Variable----#
    empcount = 0

    def __init__(self,Id,dept,experience,salary):
        self.Id = Id
        self.dept = dept
        self.experience = experience
        self.salary = salary

    def setname(self,name):
        self.name = name

    def display(self):
        #-----C style format for printing ------#
        #-----Makes it more cleaner and cooler----#
        print('%-15s %-15s %-15s %-15s %-15s'%(self.name,self.Id,self.dept,self.experience,self.salary))

    @classmethod

    def set_emp_count(cls):
        cls.empcount += 1


employee_list = []

def Insert_employee():
    name,Id,dept,experience,salary = input('Enter the name,id,dept,experience,salary of Employee : ').split(',')
    employee_list.append(Employee(Id,dept,experience,salary))
    Employee.set_emp_count()
    employee_list[-1].setname(name) #---- -1 means last element --------#

def display_list_of_employees():
    print('%-15s %-15s %-15s %-15s %-15s'%('NAME','ID','DEPARTMENT','EXPERIENCE','SALARY'))
    for i in range(len(employee_list)):
        employee_list[i].display()

def display_avg_salary():
    avg = 0
    for emp in employee_list:
        avg = avg + int(emp.salary)
    print('Average salary => ',avg/Employee.empcount)

while(True):
    print('''
    1. Insert an employee to the list
    2. Display list of employees
    3. Display total number of employees
    4. Display Avg salary
    5. Exit
    ''')

    choice = int(input('Enter a choice : '))

    if(choice == 1):
        Insert_employee()
    elif(choice == 2):
        display_list_of_employees()
    elif(choice == 3):
        print('Total number of employees => ',Employee.empcount)
    elif(choice == 4):
        display_avg_salary()
    elif(choice == 5):
        break                
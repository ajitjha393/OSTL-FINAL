class Person(object):
    def __init__(self,*args,**kwargs):
        self.name ,self.gender ,self.roll_no = kwargs['name'],kwargs['gender'],kwargs['roll_no']
        
    def show_name(self):
        print('Name = ',self.name)

    def show_gender(self):
        print('Gender = ',self.gender)       

class Student(Person):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.roll_no = kwargs['roll_no']

    def set_college(self,college):
        self.college = college

    def show_college(self):
        print('College = ',self.college)

    def show_roll_no(self):
        print('Roll_no = ',self.roll_no)

class Employee(Person):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.emp_Id,self.name,self.gender,self.roll_no = kwargs['emp_Id'],kwargs['name'],kwargs['gender'],kwargs['roll_no']

    def show_empId(self):
        print('Emp-Id = ',self.emp_Id)

class Intern(Employee,Student):
    def __init__(self,*args,**kwargs):
        super().__init__(self,*args,**kwargs)
        self.tenure = kwargs['tenure']

    def show_tenure(self):
        print('Tenure = ',self.tenure)

    def display_details(self):
        self.show_name()
        self.show_gender()
        self.show_empId()
        self.show_college()
        self.show_roll_no()
        self.show_tenure()


myIntern = Intern(name = 'Ajit',gender = 'Male',roll_no = '62',emp_Id = '120',tenure = 5)
myIntern.set_college('TSEC')
myIntern.display_details()
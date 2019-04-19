
class Fail(Exception):
    def __init__(self, message):
        super().__init__(message)


class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def displayDetails(self):
        print('%-10s %-10s %-10s'%(self.name, self.roll_no, self.marks))
        try:
            if self.marks < 40:
                raise Fail('Student {} has Scored {} marks and has Failed  '.format(
                    self.name, self.marks))

        except Fail as f:
            print(f)


myStudentList = []

num = int(input('Enter the number of Students : '))
for i in range(num):
    roll_no, name, marks = input(
        'Enter Roll-no,Name,Marks of Student {} : '.format(i+1)).split(',')
    print('----------------------------------------')
    marks = int(marks)
    myStudentList.append(Student(roll_no, name, marks))

print('DETAILS OF STUDENTS ARE : ')

for i in range(num):
    myStudentList[i].displayDetails()
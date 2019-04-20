
import mysql.connector as mc
from tkinter import *

#---Here testDB should be created on your mysql database,or else create one-----#s
#---for creating a database in sql use command mysql -u root -p (for login)----#
#----then type CREATE DATABASE testDB---------#

mydb = mc.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "testDB" 
)

mycursor = mydb.cursor() #---USED FOR INTERACTING WITH DB
mycursor.execute("CREATE TABLE register (f_name VARCHAR(255),l_name VARCHAR(255),languages VARCHAR(255),Country VARCHAR(255),gender VARCHAR(255))")

register = []   
    

def save_detail():
    f_name = first_name.get()
    l_name = last_name.get()
    languages = []
    if checkbox1.get():
        languages.append('Java')
    if checkbox2.get():
        languages.append('Python')
        languages = ' '.join(languages)
    Country = country.get()
    if radio_button.get() == 1:
        gender = 'Male'
    else:
        gender = 'Female'

    register.append((f_name,l_name,languages,Country,gender)) 
    print(register)
    sqlFormula = "INSERT INTO register (f_name,l_name,languages,Country,gender) VALUES (%s,%s,%s,%s,%s)"
    #register.append((f_name,l_name,languages,Country,gender)) 
    mycursor.executemany(sqlFormula,register)
    mydb.commit() #---ONLY FOR MAKING PERMANENT CHANGE WHILE INSERTING----# 

    mycursor.execute('SELECT * FROM register')
    print('Details registered are : ')
    for row in mycursor.fetchall():
        print(row)


root = Tk()


root.geometry('400x400')
root.title('REGISTRATION')
root.resizable(width=False,height=False)
root.configure(background='grey')

first_name = StringVar()
last_name = StringVar()

Label(root,text='First Name : ',bg='grey').grid(row=0,column=0,padx=5,pady=20)
Entry(root,textvariable = first_name).grid(row = 0 ,column = 1 ,padx=5,pady=20)

Label(text='Last Name : ',bg='grey').grid(row=1,column=0,padx=5,pady=10)
Entry(root,textvariable = last_name).grid(row = 1 ,column = 1 ,padx=5,pady=10)

checkbox1 = BooleanVar()
Label(text='Languages : ',bg='grey').place(x=10,y=130,width=80,height=20)
Checkbutton(text='JAVA',offvalue=False,onvalue=True,variable=checkbox1,bg='grey').place(x=100,y=130,width=80,height=20)

checkbox2 = BooleanVar()
Checkbutton(text='PYTHON',offvalue=False,onvalue=True,variable=checkbox2,bg='grey').place(x=200,y=130,width=80,height=20)

Label(root,text='Country : ',bg='grey').place(x=10,y=230)
list1 = ['Canada','India','UK','Nepal','Iceland','South Africa']

country=StringVar()
droplist=OptionMenu(root,country, *list1)
droplist.config(width=10,bg='grey')
droplist.place(x=100,y=230)



radio_button = IntVar()
Label(text='Gender : ',bg='grey').place(x=10,y=180)
Radiobutton(text='M',variable=radio_button,value=1,bg='grey').place(x=110,y=180)
Radiobutton(text='F',variable=radio_button,value=2,bg='grey').place(x=210,y=180)

Button(root,text="Submit",command=save_detail).place(x=150,y=350)

root.mainloop()


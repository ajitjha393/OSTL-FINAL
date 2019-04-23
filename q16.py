import pickle
from tkinter import *

class Detail(object):
    def __init__(self,first_name,last_name,languages,country,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.languages = languages
        self.country = country
        self.gender = gender

    def display_detail(self):
        print('DETAILS ARE : ')
        print('%-15s %-15s %-15s %-15s %-15s\n'%('First name','Last name','Languages','Country','Gender'))

        print('%-15s %-15s %-15s %-15s %-15s\n'%(self.first_name,self.last_name,self.languages,self.country,self.gender))

def save_detail():
    f_name = first_name.get()
    l_name = last_name.get()
    languages = []
    if checkbox1.get():
        languages.append('Java')
    if checkbox2.get():
        languages.append('Python')
    Country = country.get()
    if radio_button.get() == 1:
        gender = 'Male'
    else:
        gender = 'Female'

    root.destroy()
    #--Create a new window ---#
    new_root =  Tk()
    new_root.geometry('400x400')
    new_root.title('ENTERED DETAILS')
    new_root.resizable(width=False,height=False)
    
    t = Text(new_root)
    t.place(x=20,y=50,width=300,height = 200)
    
    
    my_detail =  f'''
        
        First-Name = {f_name}
        Last-Name  = {l_name}
        Languages  = {languages}
        Country    = {Country}
        Gender     = {gender}
    
    '''    
    t.insert(END,my_detail)
    new_root.mainloop()


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


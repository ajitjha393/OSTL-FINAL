from tkinter import *

def is_palindrome():
    mystring =   entered_string.get().upper()
    entry.place(x=50,y=300,height=60,width=200)
    if mystring == mystring[::-1]:
        ans.set('{} is a palindrome ! '.format(mystring))
    else :
        ans.set('{} is not a palindrome ! '.format(mystring))    

def Reset():
    entry.place_forget()

def Exit():
    root.quit()
    


root = Tk()
root.geometry('400x400')
root.title('Palindrome Checker')
root.resizable(width=False,height=False)
root.configure(background='yellow')
ans = StringVar()
entry = Entry(root,textvariable=ans)


entered_string = StringVar()

Label(root,text='Enter string : ').grid(row=0,column=0,padx=5,pady=5)
Entry(root,textvariable=entered_string).grid(row=0,column=1,padx=5,pady=5)

Button(root,text='Is Palindrome',command=is_palindrome).place(x=50,y=200)
Button(root,text = 'Reset',command = Reset).place(x=200,y=200)
Button(root,text = 'Exit',command = Exit).place(x=300,y=200)
root.mainloop()
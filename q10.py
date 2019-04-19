from tkinter import *


root = Tk()
root.geometry('400x350')
root.title('CALCULATOR')
root.resizable(width=False,height=False)
root.configure(background='black')

ans = StringVar()
Entry(root,textvariable=ans).place(x=20,y=10,width=360,height=30)

Button(root,text="1",command = lambda:ans.set(ans.get()+'1')).place(x=20,y=60,width=40)
Button(root,text="2",command = lambda:ans.set(ans.get()+'2')).place(x=100,y=60,width=40)
Button(root,text="3",command = lambda:ans.set(ans.get()+'3')).place(x=180,y=60,width=40)
Button(root,text="+",command = lambda:ans.set(ans.get()+'+')).place(x=260,y=60,width=40)
Button(root,text="-",command = lambda:ans.set(ans.get()+'-')).place(x=340,y=60,width=40)


Button(root,text="4",command = lambda:ans.set(ans.get()+'4')).place(x=20,y=120,width=40)
Button(root,text="5",command = lambda:ans.set(ans.get()+'5')).place(x=100,y=120,width=40)
Button(root,text="6",command = lambda:ans.set(ans.get()+'6')).place(x=180,y=120,width=40)
Button(root,text="*",command = lambda:ans.set(ans.get()+'*')).place(x=260,y=120,width=40)
Button(root,text="/",command = lambda:ans.set(ans.get()+'/')).place(x=340,y=120,width=40)

Button(root,text="7",command = lambda:ans.set(ans.get()+'7')).place(x=20,y=180,width=40)
Button(root,text="8",command = lambda:ans.set(ans.get()+'8')).place(x=100,y=180,width=40)
Button(root,text="9",command = lambda:ans.set(ans.get()+'9')).place(x=180,y=180,width=40)
Button(root,text="(",command = lambda:ans.set(ans.get()+'(')).place(x=260,y=180,width=40)
Button(root,text=")",command = lambda:ans.set(ans.get()+')')).place(x=340,y=180,width=40)

Button(root,text="0",command = lambda:ans.set(ans.get()+'0')).place(x=20,y=240,width=120)
Button(root,text=".",command = lambda:ans.set(ans.get()+'.')).place(x=180,y=240,width=40)
Button(root,text="=",command = lambda: ans.set(eval(ans.get()))).place(x=260,y=240,width=120)


root.mainloop()

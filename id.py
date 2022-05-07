from tkinter import *

root=Tk()
root.title("Encapsulation")
root.geometry("800x600")

label=Label(root,text="name")
label.place(relx=0.2,rely=0.2,anchor=CENTER)

label1=Label(root,text="ID")
label1.place(relx=0.2,rely=0.4,anchor=CENTER)

labe2=Label(root,text="captcha")
label.place(relx=0.2,rely=0.6,anchor=CENTER)

input1=Entry(root)
input1.place(relx=0.4,rely=0.2)

input2=Entry(root)
input2.place(relx=0.4,rely=0.4)

input3=Entry(root)
input3.place(relx=0.4,rely=0.6)


class score():
    def __init__(self):
        self.__username="naman"
     
    def showscore(self):
      print(self.__username)
    def updateid(self):
       self._username=self.__Id+1
       print(self.__username)
       
name=username()
name.updateid()
player.catch()
player.updateid()       

btn=Button(root,text="update login detial",command=updateid)
btn.place(relx=0.2,rely=0.8,anchor=CENTER)

btn1=Button(root,text="show profile",command=showscore)
btn1.place(relx=0.4,rely=0.8,anchor=CENTER) 

root.mainloop()

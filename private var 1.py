from tkinter import*

root=Tk()
root.title("Encapsulation")
root.geometry("600x600")

name_label=Label(root,text="Name")
name_label.place(relx=0.3,rely=0.1)

name_text=Entry(root)
name_text.place(relx=0.5,rely=0.1)

password_label=Label(root,text="Password")
password_label.place(relx=0.3,rely=0.2)

password_text=Entry(root)
password_text.place(relx=0.5,rely=0.2)

captcha_label=Label(root,text="Captcha")
captcha_label.place(relx=0.3,rely=0.3)

captcha_text=Entry(root)
captcha_text.place(relx=0.5,rely=0.3)

button_login=Button(root,text="Update login",command=showUser)
button_login.place(relx=0.4,rely=0.4)

button_show=Button(root,text="Show profile",command=addUser)
button_show.place(relx=0.6,rely=0.4)

label_show_name=Label(root)
label_show_name.place(relx=0.5,rely=0.6)
label_show_password=Label(root)
label_show_password.place(relx=0.5,rely=0.7)
label_show_captcha=Label(root)
label_show_captcha.place(relx=0.5,rely=0.8)

class userDB():
    def __init__(self):
        self.__username="Vijay"
        self.__password="privacy486"
        self.__captcha="4hfS╝"
    def showUser(self):
        label_show_name["text"]="Name: "+self.__username
        label_show_password["text"]="Password: "+self.__password
        label_show_captcha["text"]="Captcha: "+self.__captcha
    def addUser(self):
        global user
        user.username["text"]=self.__username
        

user=userDB()
user.username=name_text.get()
user.password=password_text.get()
user.captcha=captcha_text.get()  

root.mainloop() 
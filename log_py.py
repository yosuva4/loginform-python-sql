from tkinter import *
from tkcalendar import Calendar
import sqlite3
from tkinter import messagebox as msg
class Log:
    def __init__(self):
        self.a = Tk()
        self.a.title("Login")
        self.a.geometry('1000x700')
        self.a.config(bg='#e6f5fd')
        #-------------------#Images#-------------------#
        self.img_bg=PhotoImage(file='log2.png')
        self.img_avatar=PhotoImage(file='avatar_head.png')
        self.img_bground=PhotoImage(file='round2.png')

        Label(self.a,image=self.img_bg,bd=0).place(x=100,y=200)
        Label(self.a,image=self.img_bground,bd=0).place(x=634,y=80)

        #database

        self.db=sqlite3.connect("log.db")
        self.cur=self.db.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS LOGIN(
                            Name VARCHAR(10) ,
                            UserName VARCHAR(10),
                            Password VARCHAR(10),
                            RePassword VARCHAR(10),
                            DoB VARCHAR)''')
    def check_qry(self):
        pass

    def log_process(self):
        user_Name=self.user.get()
        password_L =self.pswd.get()
        sql = 'SELECT * FROM LOGIN WHERE UserName = ? AND Password =?  '
        val = (user_Name,password_L)
        self.cur.execute(sql,val)
        v=self.cur.fetchall()
        if v:
            msg.showinfo("Result",'Login succesful')
        else:
            msg.showinfo("Result",'Login Unsuccesful')

    def frame_1(self):
        f=Frame(self.a,height=450,width=397,bg='#feab45',)
        f.place(x=500,y=150)

        Label(self.a,image=self.img_avatar,bd=0).place(x=654,y=98)
        Label(f,text='LOGIN PAGE',font=("Times",30,'bold','italic'),fg="#073a93",bg='#feab45').place(x=75,y=40)

        def onvalue_user(o):
            self.user.delete(0,END)
        def offvalue_user(o):
            user=self.user.get()
            if user == '':
                self.user.insert(0,"Username")
        def onvalue_pswd(o):
            self.pswd.delete(0,END)
            self.pswd.config(show='*')
        def offvalue_pswd(o):
            pswd=self.pswd.get()
            if pswd == '':
                self.pswd.insert(0,"Password")

        self.user=Entry(f,font=("Times",16,'italic'),bd=0,width=26,fg='#073a93')
        self.user.place(x=50,y=120,height=30)
        self.user.insert(0,"Username")
        self.user.bind('<FocusIn>',onvalue_user)
        self.user.bind("<FocusOut>",offvalue_user)

        self.pswd=Entry(f,font=("Times",16,'italic'),bd=0,width=26,fg='#073a93')
        self.pswd.place(x=50,y=210,height=30)
        self.pswd.insert(0,"Password")
        self.pswd.bind('<FocusIn>',onvalue_pswd)
        self.pswd.bind("<FocusOut>",offvalue_pswd)

        btn=Button(f,text='Sign In',font=("Times",16),bg='#073a93',fg='#feab45',bd=0,width=23,padx=3,command=self.log_process)
        btn.place(x=50,y=300)

        Label(f,text="Don't have an Account ? ",font=("Times",14,'italic'),fg='black',bg='#feab45').place(x=75,y=380)
        
        btn1=Button(f,text='Sign up',font=("Times",14,'italic'),bg='#feab45',fg='#073a93',bd=0,activebackground='#feab45',command=self.register)
        btn1.place(x=270,y=376)

    def register(self):
        f=Frame(self.a,height=450,width=397,bg='#feab45',)
        f.place(x=100,y=150)

        Label(f,text='Register',font=("Times",28,'italic','bold'),bg='#feab45',fg="#073a93").place(x=160,y=4)

        user_l = Label(f,text='Name',font=("Times",16,'italic'),bg='#feab45',fg='#073a93')
        user_l.place(x=10,y=100)

        user_n = Label(f,text='Username',font=("Times",16,'italic'),bg='#feab45',fg='#073a93')
        user_n.place(x=10,y=150)

        pswd = Label(f,text='Password',font=("Times",16,'italic'),bg='#feab45',fg='#073a93')
        pswd.place(x=10,y=200)

        re_pswd = Label(f,text='Re-Password',font=("Times",16,'italic'),bg='#feab45',fg='#073a93')
        re_pswd.place(x=10,y=250)

        DOB = Label(f,text='DOB',font=("Times",16,'italic'),bg='#feab45',fg='#073a93')
        DOB.place(x=10,y=300)

        self.name = Entry(f,font=("Times",16,'italic'),bd=0)
        self.name.place(x=170,y=100)

        self.U_name = Entry(f,font=("Times",16,'italic'),bd=0)
        self.U_name.place(x=170,y=150)

        def en_leve():
            name=self.name.get()
            user_name=self.U_name.get()
            pswd=self.pswd_r.get()
            re_pswd=self.re_pswd.get()
            dob = self.dob.get()
            l_pswd=len(pswd)
           
            if len(user_name) >=6 and len(user_name)<=10 and user_name[0].isupper():
                if l_pswd>=8 and (pswd[l_pswd-1].isdigit):
                    if (pswd == re_pswd):
                        self.get_values_reg()
                    else:
                        msg.showwarning("warning",'Username and Re-Password does"not match')
                else:
                    msg.showwarning("warning",'Please Strong Password')
            else:
                msg.showwarning("warning",'Username is incorrect')
        
        self.pswd_r = Entry(f,font=("Times",16,'italic'),bd=0)
        self.pswd_r.place(x=170,y=200)

        self.re_pswd = Entry(f,font=("Times",16,'italic'),bd=0)
        self.re_pswd.place(x=170,y=250)

        self.dob = Entry(f,font=("Times",16,'italic'),bd=0)
        self.dob.place(x=170,y=300)

        self.cl=PhotoImage(file='close.png')
        btn_x = Button(f,image=self.cl,relief=FLAT,bd=0,bg='#feab45',activebackground='#feab45',command=f.destroy)
        btn_x.place(x=374,y=0)

        def sel():
            self.calen.destroy()
            self.btns1.destroy()
            c=self.calen.get_date()
            self.dob.insert(END,c)

        def in_date(d):
            self.dob.delete(0,END)
            self.calen = Calendar(f,selectmode='day',year=2022,month=6,day=20)
            self.calen.place(x=140,y=160,height=160,width=200)
            self.btns1=Button(f,text='Select',font=("Times",14,'italic'),bg='#feab45',fg='#073a93',bd=0,activebackground='#feab45',command=sel)
            self.btns1.place(x=140,y=320,height=16)
        def out_date(o):
            self.calen.destroy()

        self.dob.bind("<Button>",in_date)
        #self.dob.bind("<FocusOut>",out_date)
        btn=Button(f,text='Register',font=("Times",16),bg='#073a93',fg='#feab45',bd=0,width=23,padx=3,command=en_leve)
        btn.place(x=50,y=350)

    def get_values_reg(self):
            name=self.name.get()
            user_name=self.U_name.get()
            pswd=self.pswd_r.get()
            re_pswd=self.re_pswd.get()
            dob = self.dob.get()

            qry='INSERT INTO LOGIN ( NAME,USERNAME,PASSWORD,REPASSWORD,DOB) VALUES (?,?,?,?,?)'
            val=(name,user_name,pswd,re_pswd,dob)
            self.cur.execute(qry,val)
            self.db.commit()
            msg.showinfo("Result",'Registration is succesful')

l=Log()
l.frame_1()
#l.register()
l.a.mainloop()
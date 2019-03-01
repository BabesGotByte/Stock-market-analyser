
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import time
import requests
import pandas as pd
import datetime
#===================================Function 2===================================
# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.

api_key = 'RI6YTAKWEWLAN2GO'
data=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&outputsize=full&apikey={}'.format(api_key));
data = data.json()
data = data['Time Series (1min)']
df=pd.DataFrame(columns=['date','open','high','low','close','volume'])
for d,p in data.items():
        date = datetime.datetime.strptime(d,'%Y-%m-%d %H:%M:%S')
        data_row=[date,float(p['1. open']),float(p['2. high']),float(p['3. low']),float(p['4. close']),int(p['5. volume'])]
        df.loc[-1,:]=data_row
        df.index=df.index+1
data=df.sort_values('date')
print(df)

def exit5():
	win5.destroy()
	global event
	event = -1
def exit6():
	win6.destroy()
	global event
	event = -1
def exit7():
	win7.destroy()
	global event
	event = -1
def exit2():
	win2.destroy()
	global event
	event = -1

def test_exit():
	win3.destory()
	global event
	event = 2

def main_win():
      win4.destroy()
      global event
      event=0

def data_display():
    #==================================Button 7======================================
    button1=Button(win7,font=('arial',10),text="Exit",width=20,command=exit7)
    button1.grid(row=1,column=1)
    
def data_feed():
    #===================================Label 6=======================================
    label1=Label(win6,text="Date of investment")
    label1.grid(row=0,column=0)
    label2=Label(win6,text="Stock company")
    label2.grid(row=0,column=1)
    label3=Label(win6,text="No of shares")
    label3.grid(row=0,column=2)
    label4=Label(win6,text="Rate")
    label4.grid(row=0,column=3)
    label5=Label(win6,text="Amount invested")
    label5.grid(row=0,column=4)
    #==================================Entry 6========================================
    a1=StringVar()
    a2=StringVar()
    a3=StringVar()
    entry_date=Entry(win6,font=('arial',10),textvariable=a1,width=20)
    entry_date.grid(row=1,column=0)
    entry_Stock_company=Entry(win6,font=('arial',10),textvariable=a1,width=20)
    entry_Stock_company.grid(row=1,column=1)
    entry_no_of_shares=Entry(win6,font=('arial',10),textvariable=a2,width=20)
    entry_no_of_shares.grid(row=1,column=2)
    entry_rate=Entry(win6,font=('arial',10),textvariable=a3,width=20)
    entry_rate.grid(row=1,column=3)
    entry_amount=Entry(win6,font=('arial',10),textvariable=a2,width=20)
    entry_amount.grid(row=1,column=4)
    #==================================Button 6======================================
    button1=Button(win6,font=('arial',10),text="Submit",width=20,command=set_data_option)
    button1.grid(row=4,column=1)
    button2=Button(win6,font=('arial',10),text="Submit and add another",width=20,command=set_data_feed)
    button2.grid(row=4,column=2)
    button3=Button(win6,font=('arial',10),text="Exit",width=20,command=exit6)
    button3.grid(row=4,column=3)

    
def data_option():
    #==================================Button 5======================================
    button1=Button(win5,font=('arial',10),text="Data_feed",width=20,command=set_data_feed)
    button1.grid(row=1,column=1)
    button2=Button(win5,font=('arial',10),text="Data_display",width=20,command=set_data_display)
    button2.grid(row=1,column=2)
    button3=Button(win5,font=('arial',10),text="Exit",width=20,command=exit5)
    button3.grid(row=1,column=3)


def login():
    #===================================Label 4=======================================
    label1=Label(win4,text="Enter you credentials:")
    label1.grid(row=0,column=0)
    label2=Label(win4,text="Username")
    label2.grid(row=2,column=1)
    label3=Label(win4,text="Password")
    label3.grid(row=3,column=1)
    #==================================Entry 4========================================
    a1=StringVar()
    a2=StringVar()
    entry1=Entry(win4,font=('arial',10),textvariable=a1,width=20)
    entry1.grid(row=2,column=2)
    entry2=Entry(win4,font=('arial',10),textvariable=a2,width=20,show="*")
    entry2.grid(row=3,column=2)
    #==================================Button 4======================================
    button1=Button(win4,font=('arial',10),text="Login",width=20,command=set_data_option)
    button1.grid(row=5,column=1)
    button2=Button(win4,font=('arial',10),text="Cancel",width=20,command=main_win)
    button2.grid(row=5,column=2)

    
def signup():
    label1c=Label(win3,text="Username")
    label1c.grid(row=1,column=1)
    label2c=Label(win3,text="First name")
    label2c.grid(row=2,column=1)
    label3c=Label(win3,text="Middle name")
    label3c.grid(row=3,column=1)
    label4c=Label(win3,text="Last name")
    label4c.grid(row=4,column=1)
    label5c=Label(win3,text="Email address")
    label5c.grid(row=5,column=1)
    label6c=Label(win3,text="Mobile number")
    label6c.grid(row=6,column=1)
    label7c=Label(win3,text="Password")
    label7c.grid(row=7,column=1)
    label8c=Label(win3,text="Confirm password")
    label8c.grid(row=8,column=1)
    c1=StringVar()
    c2=StringVar()
    c3=StringVar()
    c4=StringVar()
    c5=StringVar()
    c6=StringVar()
    c7=StringVar()
    c8=StringVar()
    entry1c=Entry(win3,font=('arial',10),textvariable=c1).grid(row=1,column=2)
    entry2c=Entry(win3,font=('arial',10),textvariable=c2).grid(row=2,column=2)
    entry3c=Entry(win3,font=('arial',10),textvariable=c3).grid(row=3,column=2)
    entry4c=Entry(win3,font=('arial',10),textvariable=c4).grid(row=4,column=2)
    entry5c=Entry(win3,font=('arial',10),textvariable=c5).grid(row=5,column=2)
    entry6c=Entry(win3,font=('arial',10),textvariable=c6).grid(row=6,column=2)
    entry7c=Entry(win3,font=('arial',10),textvariable=c7,show="*").grid(row=7,column=2)
    entry8c=Entry(win3,font=('arial',10),textvariable=c8,show="*").grid(row=8,column=2)
    button1c=Button(win3,text="Submit",width=20,command=set_login)
    button1c.grid(row=10,column=1)
    button1c=Button(win3,text="Cancel",width=20,command=set_exit)
    button1c.grid(row=10,column=2)
def main():
    win1 = Tk()
    win1.title("Restaraunt Bill")
    win1.geometry("5000x5000+0+0")
    w=Scale(win1, from_=0, to=5,orient=VERTICAL)
    w.grid(row=1,column=0)
    y=w.get()
    labele1 = Label(win1,text="RATE FROM 0 TO 5",fg="black",font=('arial',20,'bold'))
    labele1.grid(row=0,column=0)
    #=================================List1 functions=================================
    def open1():
        open2=filedialog.askopenfile()
        open3=open2.name
        open4=open(open3)
        label4 = Label(win1,text=open4.read())
        label4.grid(row=0)
    def save1():
        save2 = messagebox.askyesno(title="Save file",message="Do you want to save the file")
    def delete1():
        messagebox.askyesno(title="Delete file",message="Are you sure to delete the file")
    def quit1():
        quit2 = messagebox.askyesno(title="Quit",message="Do you want to quit")
        if quit2 == 1:
            win1.destroy()
    #==================================Button functions================================
    def button1a():
        entry1a=float(entryv1.get())
        entry2a=float(entryv2.get())
        entry3a=float(entryv3.get())
        entry4a=float(entryv4.get())
        entry5a=float(entryv5.get())

        entry1b=entry1a*10
        entry2b=entry2a*20
        entry3b=entry3a*30
        entry4b=entry4a*40
        entry5b=entry5a*50

        meal_cost=entry1b + entry2b + entry3b + entry4b + entry5b
        gst_tax=meal_cost*0.05
        ser_tax=meal_cost*2.5
        tip=100
        total=meal_cost +gst_tax +ser_tax+tip
        entryv6.set(meal_cost)
        entryv7.set(gst_tax)
        entryv8.set(ser_tax)
        entryv9.set(tip)
        entryv10.set(total)

    def button2a():
        entryv1.set(0)
        entryv2.set(0)
        entryv3.set(0)
        entryv4.set(0)
        entryv5.set(0)
        entryv6.set("")
        entryv7.set("")
        entryv8.set("")
        entryv9.set("")
        entryv10.set("")

    def button3a():
        win1.destroy()
    #=================================Radio button functions==========================    
    def radio1():
        a=v.get()
        if(a==1):
            Label(win1,text="You choose CASH mode",font=('arial',15)).grid(row=2)
        elif(a==2):
            Label(win1,text="You choose DEBIT CARD mode",font=('arial',15)).grid(row=2)
        elif(a==3):
            Label(win1,text="You choose ONLINE PAYMENT mode",font=('arial',15)).grid(row=2)
        elif(a==4):
            Label(win1,text="You choose PAYTM mode",font=('arial',15)).grid(row=2)
        elif(a==5):
            Label(win1,text="You choose TEZ mode",font=('arial',15)).grid(row=2)
    #==================================Heading=========================================
    label1 = Label(win1,text="XYZ Hotel",fg="black",font=('arial',40,'bold'))
    label1.grid(row=0,column=3)
    label2 = Label(win1,text="Thanks for visiting",fg="black",font=('arial',25,'bold'))
    label2.grid(row=1,column=3)
    #==================================Time============================================
    time1 = time.asctime(time.localtime(time.time()))
    label3 = Label(win1,text=time1,font=('arial',20,'bold'))
    label3.grid(row=2,column=3)
    #================================Radio button======================================
    v=IntVar()
    v.set(1)
    Label(win1,text="Choose your payment mode",anchor=W).grid(row=3)
    Radiobutton(win1,text="Cash",padx=25,indicatoron=0,width=15,variable=v,value=1,command=radio1).grid(row=4)
    Radiobutton(win1,text="Debit card",padx=25,indicatoron=0,width=15,variable=v,value=2,command=radio1).grid(row=5)
    Radiobutton(win1,text="Online banking",padx=25,indicatoron=0,width=15,variable=v,value=3,command=radio1).grid(row=6)
    Radiobutton(win1,text="Paytm",padx=25,indicatoron=0,width=15,variable=v,value=4,command=radio1).grid(row=7)
    Radiobutton(win1,text="Tez",padx=25,indicatoron=0,width=15,variable=v,value=5,command=radio1).grid(row=8)


    
    #==================================Menubar=========================================
    menulist1 = Menu()

    list1 = Menu()
    list1.add_command(label="New File")
    list1.add_command(label="Open",command=open1)
    list1.add_command(label="Print")
    list1.add_command(label="Save",command=save1)
    list1.add_command(label="Delete",command=delete1)
    list1.add_command(label="Quit",command=quit1)

    list2 = Menu()
    list2.add_command(label="Contact details")
    list2.add_command(label="Staff")

    list3 = Menu()
    list3.add_command(label="Dishes")
    list3.add_command(label="Price list")
    list3.add_command(label="Crocery list")

    menulist1.add_cascade(label="File",menu=list1)
    menulist1.add_cascade(label="About us",menu=list2)
    menulist1.add_cascade(label="Hotel Menu",menu=list3)
    #=================================Entry list 1======================================

    label6=Label(win1,font=('arial',16,'bold'),text="Burger").grid(row=10,column=2)
    label7=Label(win1,font=('arial',16,'bold'),text="Pizza").grid(row=11,column=2)
    label8=Label(win1,font=('arial',16,'bold'),text="Chicken").grid(row=12,column=2)
    label9=Label(win1,font=('arial',16,'bold'),text="Ice cream").grid(row=13,column=2)
    label10=Label(win1,font=('arial',16,'bold'),text="Cold drink").grid(row=14,column=2)

    entryv1=StringVar()
    entryv2=StringVar()
    entryv3=StringVar()
    entryv4=StringVar()
    entryv5=StringVar()
    entryv1.set(0)
    entryv2.set(0)
    entryv3.set(0)
    entryv4.set(0)
    entryv5.set(0)
    entry1 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv1,width=20).grid(row=10,column=3)
    entry2 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv2,width=20).grid(row=11,column=3)
    entry3 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv3,width=20).grid(row=12,column=3)
    entry4 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv4,width=20).grid(row=13,column=3)
    entry5 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv5,width=20).grid(row=14,column=3)

    #=================================Entry list 2==========================================
    label11=Label(win1,font=('arial',16,'bold'),text="Meal cost",anchor=W).grid(row=10,column=5)
    label12=Label(win1,font=('arial',16,'bold'),text="GST",anchor=W).grid(row=11,column=5)
    label13=Label(win1,font=('arial',16,'bold'),text="Service tax",anchor=W).grid(row=12,column=5)
    label14=Label(win1,font=('arial',16,'bold'),text="Tip",anchor=W).grid(row=13,column=5)
    label15=Label(win1,font=('arial',16,'bold'),text="Total price",anchor=W).grid(row=14,column=5)
    label16=Label(win1,font=('arial',16,'bold'),text="COSTUMER NAME",anchor=W).grid(row=16,column=1)

    entryv6=StringVar()
    entryv7=StringVar()
    entryv8=StringVar()
    entryv9=StringVar()
    entryv10=StringVar()
    entryv11=StringVar()
    entry6 =Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv6,width=20).grid(row=10,column=6)
    entry7 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv7,width=20).grid(row=11,column=6)
    entry8 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv8,width=20).grid(row=12,column=6)
    entry9 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv9,width=20).grid(row=13,column=6)
    entry10 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv10,width=20).grid(row=14,column=6)
    entry11 = Entry(win1,font=('arial',16,'bold'),bd=6,textvariable=entryv11,width=20).grid(row=16,column=2)
    #=================================Buttons===============================================
    button1 = Button(win1,font=('arial',16,'bold'),text="Total",bd=6,width=15,command=button1a).grid(row=15,column=3)
    button2 = Button(win1,font=('arial',16,'bold'),text="Reset",bd=6,width=15,command=button2a).grid(row=15,column=5)
    button3 = Button(win1,font=('arial',16,'bold'),text="Quit",bd=6,width=15,command=button3a).grid(row=15,column=6)
    win4.destroy()
    win1.config(menu=menulist1)
    win1.mainloop()
#=================================Button 2======================================
def set_signup():
	win2.destroy()
	global event
	event = 1

def set_login():
	win3.destroy()
	global event
	event = 2

def set_data_display():
	win5.destroy()
	global event
	event = 5
	
def set_data_option():
	win4.destroy()
	global event
	event = 3

def set_data_feed():
	win5.destroy()
	global event
	event = 4

def direct_login():
        win2.destroy()
        global event
        event = 2

def set_exit():
	win3.destroy()
	global event
	event = -1

def define_win2():
        button1b=Button(win2,font=('arial',10),text="Signup",width=20,command=set_signup)
        button1b.grid(row=2,column=1)
        button2b=Button(win2,font=('arial',10),text="Login",width=20,command=direct_login)
        button2b.grid(row=3,column=1)
        button3b=Button(win2,font=('arial',10),text="Exit",width=20,command=exit2)
        button3b.grid(row=4,column=1)
        

if __name__ == '__main__':
	global win2
	global win3
	global win4
	global win5
	global win6
	global win7
	global event
	event = 0
	while True:
		if event == 0:
			win2 = Tk()
			win2.title("Welcome Window")
			win2.geometry("500x300+0+0")
			define_win2()
			win2.mainloop()
		elif event == 1:	
			win3=Tk()
			win3.title("Signup")
			win3.geometry("500x300+0+0")
			signup()
			win3.mainloop()
		elif event == 2:
			win4 = Tk()
			win4.title("Login")
			win4.geometry("500x300+0+0")
			login()
			win4.mainloop()
		elif event == 3:
			win5 = Tk()
			win5.title("Data_option")
			win5.geometry("500x300+0+0")
			data_option()
			win5.mainloop()
		elif event == 4:
			win6 = Tk()
			win6.title("Data_feed")
			win6.geometry("500x300+0+0")
			data_feed()
			win6.mainloop()
		elif event == 5:
			win7 = Tk()
			win7.title("Data_display")
			win7.geometry("500x300+0+0")
			data_display()
			win7.mainloop()
		elif event == -1:
			break

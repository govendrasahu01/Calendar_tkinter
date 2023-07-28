# Import Required Library
from tkinter import *
from tkcalendar import Calendar
from datetime import date
 
# Create Object
root = Tk()
 
# Set geometry
root.geometry("600x600")
 
# Add Calendar of current month
today = str(date.today())
c_year, c_month,c_day = list(map(int,today.split("-")))

cal = Calendar(root, selectmode = 'day',
               year =c_year, month=c_month,day= c_day)
 
cal.pack(pady = 30)
 
def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())


# Add Button and Label
Button(root, text = "Get Date",
       command = grad_date).pack(pady = 10)


date = Label(root, text = "")
date.pack(pady = 30)
 

# Execute Tkinter
root.mainloop()
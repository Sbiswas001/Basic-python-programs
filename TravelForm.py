#TRAVEL FORM & Entry Widget
from tkinter import *
def getValue():
    print("Submitting form...")
    print(f"{name_val.get(),phone_val.get(),gender_val.get(),emergency_contact_val.get(),payment_mode_val.get(),foodservice_val.get()}")
    with open("records.txt","a") as f:
        f.write(f"{name_val.get(),phone_val.get(),gender_val.get(),emergency_contact_val.get(),payment_mode_val.get(),foodservice_val.get()}\n")

root=Tk()
root.geometry("310x270")
root.minsize(310,270)
root.maxsize(310,270)
root.title("travel Form")
Label(root,text="ABC Travel Agency",font=" helvetica 14 bold",pady=12).grid(row=0,column=3)
name_label=Label(root,text="Name:").grid(row=1)
phone_label=Label(root,text="Phone:").grid(row=2)
gender_label=Label(root,text="Gender:").grid(row=3)
emergency_contact_label=Label(root,text="Emergency Contact:").grid(row=4)
payment_mode_label=Label(root,text="Payment Mode:").grid(row=5)
name_val=StringVar()
phone_val=StringVar()
gender_val=StringVar()
emergency_contact_val=StringVar()
payment_mode_val=StringVar()
foodservice_val=IntVar()#for a check box
name_entry=Entry(root,textvariable=name_val).grid(row=1,column=3)
phone_entry=Entry(root,textvariable=phone_val).grid(row=2,column=3)
gender_entry=Entry(root,textvariable=gender_val).grid(row=3,column=3)
emergency_contact_entry=Entry(root,textvariable=emergency_contact_val).grid(row=4,column=3)
payment_mode_entry=Entry(root,textvariable=payment_mode_val).grid(row=5,column=3)
#checkboxes
foodservice_button=Checkbutton(text="Do you want food service?",variable=foodservice_val,pady=5).grid(row=6,column=3)
#submit button
Button(text="Submit",command=getValue).grid(row=7,column=3)
root.mainloop()

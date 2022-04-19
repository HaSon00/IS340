from tkinter import *

root = Tk()
root.geometry('400x400')

root.resizable(0,0)
root.title('Contact Book')

contactlist = []


FName = StringVar()
LName = StringVar()
Address = StringVar()
Email = StringVar()
Phone = StringVar()

frame = Frame(root)
frame.pack(side = RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)

#display selected item
def Selected():
    return int(select.curselection()[0])

def Add():
    contactlist.append([FName.get(), LName.get(), Address.get(), Email.get(), Phone.get()])
    Select_set()
    #clear boxes after add
    reset()

def EDIT():
    contactlist[Selected()] = [FName.get(), LName.get(), Address.get(), Email.get(), Phone.get()]
    Select_set()


def DELETE():
    del contactlist[Selected()]
    Select_set()



def VIEW():
    FNAME, LNAME, ADDRESS, EMAIL, PHONE = contactlist[Selected()]
    FName.set(FNAME)
    LName.set(LNAME)
    Address.set(ADDRESS)
    Email.set(EMAIL)
    Phone.set(PHONE)

def reset():
    #clear text boxes
    FName.set('')
    LName.set('')
    Address.set('')
    Email.set('')
    Phone.set('')

def EXIT():
    root.destroy()


def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for lname, FName, address, email, phone in contactlist :
        select.insert (END, FName + ', ' + lname)
Select_set()

#first name
Label(root, text = 'First Name').place(x= 30, y=20)
Entry(root, textvariable = FName).place(x= 100, y=20)

#last name
Label(root, text = 'Last Name').place(x= 30, y=50)
Entry(root, textvariable = LName).place(x= 100, y=50)

#address
Label(root, text = 'Address').place(x= 30, y=80)
Entry(root, textvariable = Address).place(x= 100, y=80)

#email
Label(root, text = 'Email').place(x= 30, y=110)
Entry(root, textvariable = Email).place(x= 100, y=110)

#phone
Label(root, text = 'Phone').place(x= 30, y=140)
Entry(root, textvariable = Phone).place(x= 100, y=140)

#add button
Button(root,text="ADD", command = Add).place(x= 50, y=180)

#edit button
Button(root,text="EDIT",command = EDIT).place(x= 50, y=210)

#delete button
Button(root,text="DELETE",command = DELETE).place(x= 50, y=240)

#view button
Button(root,text="VIEW", command = VIEW).place(x= 50, y=270)

#exit button
Button(root,text="EXIT", command = EXIT).place(x= 300, y=320)

Button(root,text="RESET", command = reset).place(x= 50, y=300)
root.mainloop()
from tkinter import *
import sqlite3

root = Tk()
root.title('Contact book')
root.geometry("500x300")

# connect to the database
conn = sqlite3.connect('contact.db')

# get cursor
cur = conn.cursor()

#create table
'''
cur.execute("""CREATE TABLE contact (
        first_name text, 
        last_name text,
        address text,
        phone integer
        ) """)
'''

#create submit function
def submit():
    # clear text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    phone.delete(0, END)

#create text boxes
f_name = Entry(root, width=30)
f_name.grid(row = 0, column = 1, padx = 20)

l_name = Entry(root, width=30)
l_name.grid(row = 1, column = 1)

address = Entry(root, width=30)
address.grid(row = 2, column = 1)

phone = Entry(root, width=30)
phone.grid(row = 3, column = 1)

#create text box labels
f_name_label = Label(root, text = "First Name")
f_name_label.grid(row = 0, column = 0)

l_name_label = Label(root, text = "Last Name")
l_name_label.grid(row = 1, column = 0)

address_label = Label(root, text = "Address")
address_label.grid(row = 2, column = 0)

phone_label = Label(root, text = "Phone")
phone_label.grid(row = 3, column = 0)

#create Submit button
submit_btn = Button(root, text="Add", command=submit)
submit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# commit changes
conn.commit()

#close connection
conn.close()

root.mainloop()

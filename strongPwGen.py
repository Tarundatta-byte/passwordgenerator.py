# Python program to generate random
# password using Tkinter module
import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

# Function for calculation of password
def low():
	entry.delete(0, END)

	# Get the length of password
	length = var1.get()

	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*abcdefghijklmnopqrstuvwxyz0123456789"
	password = " "

	# if strength selected is low
	if var.get() == 2:
		for i in range(0, length):
			password = password + random.choice(lower)
		return password

	# if strength selected is medium
	elif var.get() == 1:
		for i in range(0, length):
			password = password + random.choice(upper)
		return password

	# if strength selected is strong
	elif var.get() == 0:
		for i in range(0, length):
			password = password + random.choice(digits)
		return password
	else:
		print("Please choose an option")


# Function for generation of password
def generate():
	password1 = low()
	entry.insert(10, password1)


# Function for copying password to clipboard
def copy1():
	random_password = entry.get()
	pyperclip.copy(random_password)


# Main Function

# create GUI window
root = Tk()
var = IntVar()
var1 = IntVar()

# Title of your GUI window
root.title("Strong Password Generator | Developed By TARUN DATTA")
root.geometry("600x200")
root['bg']="lightblue"
# create label and entry to show
# password generated
Random_password = Label(root, text="Password")
Random_password.place(x=140,y=60)
entry = Entry(root)
entry.place(x=200,y=60)

# create label for length of password
c_label = Label(root, text="Select Length")
c_label.place(x=140,y=30)

# create Buttons Copy which will copy
# password to clipboard and Generate
# which will generate the password
copy_button = Button(root, text="Copy Password", command=copy1)
copy_button.place(x=200,y=90)
generate_button = Button(root, text="Generate Password", command=generate)
generate_button.place(x=400,y=30)

# Radio Buttons for deciding the
# strength of password
# Default strength is Medium
radio_low = Radiobutton(root, text="Low", variable=var, value=2)
radio_low.place(x=350,y=90)
radio_middle = Radiobutton(root, text="Medium", variable=var, value=1)
radio_middle.place(x=350,y=120)
radio_strong = Radiobutton(root, text="Strong", variable=var, value=0)
radio_strong.place(x=350,y=150)
combo = Combobox(root, textvariable=var1)

# Combo Box for length of your password
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
				17, 18, 19, 20, 21, 22, 23, "Length")
combo.current(0)

combo.place(x=220,y=30)

# start the GUI
root.mainloop()

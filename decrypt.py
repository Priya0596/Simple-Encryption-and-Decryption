from tkinter import *
from tkinter import messagebox
import base64
import os

def update_message(message):
    # This function updates the text widget with the provided message
    text2.delete(1.0, END)  # Clear the text area before inserting new content
    text2.insert(END, message)  # Insert the new message into the text widget

def decrypt():
    password = code.get()
    if password == "priya":
        message = text1.get(1.0, END)
        try:
            decode_message = message.encode("ascii")
            base64_bytes = base64.b64decode(decode_message)
            decrypt_message = base64_bytes.decode("ascii")
            update_message(f"Decrypted Message:\n{decrypt_message}")
        except Exception as e:
            update_message("Invalid input for decryption.")
            print(f"Error: {e}")
    elif password == "":
        messagebox.showerror("Encryption", "Input Password")
    else:
        messagebox.showerror("Encryption", "Invalid Password")

def encrypt():
    password = code.get()
    if password == "priya":
        message = text1.get(1.0, END)
        try:
            encode_message = message.encode("ascii")
            base64_bytes = base64.b64encode(encode_message)
            encrypt_message = base64_bytes.decode("ascii")
            update_message(f"Encrypted Message:\n{encrypt_message}")
        except Exception as e:
            update_message("Invalid input for encryption.")
            print(f"Error: {e}")
    elif password == "":
        messagebox.showerror("Encryption", "Input Password")
    else:
        messagebox.showerror("Encryption", "Invalid Password")

def main_screen():
    global screen
    global code
    global text1
    global text2  # Added to be able to update the text widget

    screen = Tk()
    screen.geometry("375x398")
    screen.title("PctApp")

    def reset():
        code.set("")
        text1.delete(1.0, END)
        text2.delete(1.0, END)  # Clear the result text area when resetting

    Label(text="Enter text for Encryption and Decryption", fg="black", font=("arial", 14)).place(x=10, y=10)
    text1 = Text(font="calbri 18", bg="grey", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter the key for Encryption and Decryption", fg="black", font=("arial", 14)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    # Result text box for displaying encrypted or decrypted message
    text2 = Text(font="calbri 14", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text2.place(x=10, y=340, width=355, height=50)

    screen.mainloop()

main_screen()

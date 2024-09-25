import tkinter
from tkinter import messagebox

# Initialize the main application window
root = tkinter.Tk()
root.title("Tkinter Window")

root.geometry("380x440")
root.configure(bg="#333333")

def loginNow():
    username =["hira","asra","tani","sara"]
    entered_username= user_field.get()
    password_ = ["1234","7895","5264","23231"]
    password_enter= password.get()
    if entered_username in username and password_enter in password_:
        messagebox.showinfo(title="Successfully Login", message="You are logged in")
    else:
        messagebox.showinfo(title="Unsucessful Login", message="Aw,try later")

frame = tkinter.Frame(root, bg="#333333")

# Title label
login = tkinter.Label(frame, text="Login Form", font=("Arial",30), pady= 20, bg="#333333",  fg="#FFFFFF")
login.grid(row=0, column=1, columnspan=2)

# Username label and entry
username_field = tkinter.Label(frame, text="Enter your Name: ", font=("Arial",15),bg="#333333", pady=40 , fg="#FFFFFF")
username_field.grid()

user_field = tkinter.Entry(frame, font=("Arial",14))
user_field.grid(row=1,column=2)

# Password label and entry
password_field = tkinter.Label(frame, text="Password: ",pady=40, font=("Arial",15),bg="#333333", fg="#FFFFFF")
password_field.grid()

password = tkinter.Entry(frame, show="*", font=("Arial", 14))
password.grid(row=2, column=2)

submit_btn = tkinter.Button(frame, text="Please Login", command = loginNow, font=("Arial",14), pady=15, fg="#FFFFFF", bg= "#333333")
submit_btn.grid(row=3, column=1, columnspan=2)


frame.pack()

# Start the Tkinter event loop
root.mainloop()

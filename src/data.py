import os
import tkinter as tk


def login(name, password):

    file = open("username_info.txt", "w")
    file.write(name + "\n")
    file.write(password)
    file.close()

    label = tk.Label(text="Registration Success")
    label.pack()


def main():
    window = tk.Tk()
    window.geometry("700x700")
    window.title("Data Entry")

    frame = tk.Frame()
    frame.pack()

    label = tk.Label(master=frame, text="Log in")
    label.pack()

    label = tk.Label(master=frame, text="User Name")
    label.pack()

    entry_name = tk.Entry(master=frame)
    name = entry_name.get()
    entry_name.pack()

    label = tk.Label(master=frame, text="Password")
    label.pack()

    entry_pass = tk.Entry(master=frame)
    password = entry_pass.get()
    entry_pass.pack()

    button = tk.Button(window, text="Log In", command=login(password, name))
    button.pack()

    window.mainloop()

    return password, name


main()

version = "v2.0.0"

from tkinter import ttk
from tkinter import * 


window = Tk()
window.title("Settings")
window.geometry("700x500")


Label(window,text="Speedtest Benchmarker {version}",font=('Helvetica',18,'bold')).grid(row=0,column=3)
Label(window,text="Username:").grid(row=2,column=2)
Label(window,text="Password:").grid(row=4,column=2)

#Entry Fields
e1 = Entry(window)
e1.grid(row=2,column=4)
e2 = Entry(window,show="*")
e2.grid(row=4,column=4)

#Focus on Username entry field
e1.focus()

#Buttons
btnExit=ttk.Button(window,text="Exit")
btnExit.grid(row=6,column=2)
btnExit.config(command=exit)
btnReset=ttk.Button(window,text="Reset")
btnReset.grid(row=6,column=3)
btnReset.config(command=reset)
btnLogin=ttk.Button(window,text="Login")
btnLogin.grid(row=6,column=4)
btnLogin.config(command=login)


window.mainloop()
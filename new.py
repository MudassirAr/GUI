
from tkinter  import*
root = Tk()
root.geometry("700x400")
root.title("My GUI with TKINTER")



title_label = Label( text='''
\nPython offers multiple options for developing GUI (Graphical User Interface).
\nOut of all the GUI methods, tkinter is most commonly used method. It is a
\nstandard Python interface to the Tk GUI toolkit shipped with Python. Python
\nwith tkinter outputs the fastest and easiest way to create the GUI applications.
\nCreating a GUI using tkinter is an easy task.''', bg="light blue", fg="black", padx=15, pady=90, font="Helvetica  8 bold",
                     borderwidth=10, relief=GROOVE)

title_label.pack(side=LEFT,  fill = Y, padx = 20, pady = 18)

photo = PhotoImage(file="photo.png")


ayan_label= Label(image=photo)
ayan_label.pack()







root.mainloop()
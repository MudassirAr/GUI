# Attributes Of Label & Pack


from tkinter  import*
root = Tk()
root.geometry("700x400")
root.title("My GUI with TKINTER")

# important Label Options
# text - adds the text
#bd - background
# fg - foreground
# font - sets the font
# 1. font= ("font name(arial", font size(20), bold, itallic)
# 2. font = "font name font size bold"
# ex = "arial 20 italic"
#
# padx- x padding
# pady - y padding
# relief - boprder style - SUNKEN, RAISED, GROOVE, RIDGE


title_label = Label( text='''
\nPython offers multiple options for developing GUI (Graphical User Interface). 
\nOut of all the GUI methods, tkinter is most commonly used method. It is a 
\nstandard Python interface to the Tk GUI toolkit shipped with Python. Python 
\nwith tkinter outputs the fastest and easiest way to create the GUI applications.
\nCreating a GUI using tkinter is an easy task.''', bg="light blue", fg="black", padx=15, pady=90, font="Helvetica  8 bold",
                     borderwidth=10, relief=GROOVE)


#IMPORTANT PACK OPTIONS
#anchor = new
#side = TOP, BOTTOM, LEFT, RIGHT
# FILL
# PADX
# PADY


title_label.pack(side=LEFT,  fill = Y, padx = 20, pady = 18)






root.mainloop()
from tkinter import*
name_root= Tk()

name_root.geometry("455x244")
photo = PhotoImage(file="photo.png")

ayan_label= Label(image=photo)
ayan_label.pack()


name_root.mainloop()


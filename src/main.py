from tkinter import *
from tkinter import ttk
import Agency
import Employee


root = Tk()

# actual size of window
root.configure(height=1000, width=1000)

# window constraints for sizing
root.minsize(height=500, width=500)
root.maxsize(height=1500, width=1500)
root.configure(background='lightgray')
root.title("Add Agency")


# button = Button(root, text="Click me")
# button.pack()



root.mainloop()

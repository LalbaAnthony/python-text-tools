from tkinter import Tk
from view import pttView
from controller import pttController

if __name__ == "__main__":
    root = Tk()
    view = pttView(root)
    controller = pttController(view)
    root.mainloop()

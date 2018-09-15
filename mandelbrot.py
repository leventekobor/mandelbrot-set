from tkinter import *

def setup():
    root = Tk()
    root.geometry('500x500')

    canvas = Canvas(root, height = 500, width = 500)
    canvas.pack()

    root.mainloop()

if __name__ == '__main__':
    setup()

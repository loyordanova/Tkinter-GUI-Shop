from tkinter import Tk, Canvas



def create_root():
    root = Tk()
    root.geometry('700x600')
    root.resizable(False, False)
    root.title('GUI Shop')


    return root


def create_frame():
    frame = Canvas(root, width=700, height=700)
    frame.grid(row=0, column=0)

    return frame


root = create_root()
frame = create_frame()
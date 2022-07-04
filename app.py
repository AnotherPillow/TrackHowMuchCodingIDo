from tkinter import *
from PIL import ImageTk
from file import main as write

def get_text(window,tl,dl,ll,fl,tl_input,dl_input,ll_input,fl_input):
    tl_text = tl_input.get()
    dl_text = dl_input.get()
    ll_text = ll_input.get()
    fl_text = fl_input.get()
    write(tl_text,dl_text,ll_text,fl_text)
    #clear the text boxes
    tl_input.delete(0,END)
    dl_input.delete(0,END)
    ll_input.delete(0,END)
    fl_input.delete(0,END)


window = Tk()
window.title("Project Tracker")
window.geometry('400x800')

tl = Label(window, text="Enter title of project:")
tl.pack()
tl_input = Entry(window, width=50)
tl_input.pack()

dl = Label(window, text="Enter date (DD-MM-YYYY):")
dl.pack()
dl_input = Entry(window, width=50)
dl_input.pack()

ll = Label(window, text="Enter amount of lines:")
ll.pack()
ll_input = Entry(window, width=50)
ll_input.pack()

fl = Label(window, text="Enter amount of files:")
fl.pack()
fl_input = Entry(window, width=50)
fl_input.pack()

button = Button(window, text="Write", command=lambda: get_text(window,tl,dl,ll,fl,tl_input,dl_input,ll_input,fl_input))
image = ImageTk.PhotoImage(file='py.png')

imgl = Label(window, image = image)
imgl.pack(fill = "both", expand = "yes")

button.pack()
window.mainloop()
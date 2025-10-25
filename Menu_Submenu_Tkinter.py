#Menu & Submenu
from tkinter import *
def func_new():
    print("You clicked on new")
def func_open():
    print("You clicked on open")
def func_save():
    print("You clicked on save")
def func_print():
    print("You clicked on print")
def func_undo():
    print("You clicked on undo")
def func_redo():
    print("You clicked on redo")
def func_cut():
    print("You clicked on cut")
def func_copy():
    print("You clicked on copy")
def func_paste():
    print("You clicked on paste")

root = Tk()
root.title("Menu & Submenu")
root.geometry("400x400")
#Use this to create a non dropdown menu
# menu1 = Menu(root)
# menu1.add_command(label="File", command=file_func)
# menu1.add_command(label="Exit", command=quit)
# root.config(menu=menu1)
main_menu=Menu(root)
m1=Menu(main_menu,tearoff=0)
m1.add_command(label="New",command=func_new)
m1.add_command(label="Open",command=func_open)
m1.add_separator()
m1.add_command(label="Save",command=func_save)
m1.add_command(label="Print",command=func_print)
main_menu.add_cascade(label="File",menu=m1)

root.config(menu=main_menu)
m2=Menu(main_menu,tearoff=1)
m2.add_command(label="Undo",command=func_undo)
m2.add_command(label="Redo",command=func_redo)
m2.add_separator()
m2.add_command(label="Cut",command=func_cut)
m2.add_command(label="Copy",command=func_copy)
m2.add_command(label="Paste",command=func_paste)
main_menu.add_cascade(label="Edit",menu=m2)

root.mainloop()

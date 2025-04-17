from tkinter import *

root = Tk()
root.geometry('600x400')

menubar = Menu(root)

# File menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_command(label='Save')
filemenu.add_command(label='Save As')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
menubar.add_cascade(label='File', menu=filemenu)

# Edit menu
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label='Undo')
editmenu.add_command(label='Redo')
editmenu.add_separator()
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')
editmenu.add_command(label='Delete')
editmenu.add_command(label='Select All')
menubar.add_cascade(label='Edit', menu=editmenu)

# View menu
viewmenu = Menu(menubar, tearoff=0)
viewmenu.add_command(label='Zoom In')
viewmenu.add_command(label='Zoom Out')
viewmenu.add_command(label='Full Screen')
menubar.add_cascade(label='View', menu=viewmenu)

# Help menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='Documentation')
helpmenu.add_command(label='About')
menubar.add_cascade(label='Help', menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
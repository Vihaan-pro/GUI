import tkinter
from tkinter.filedialog import *

root = tkinter.Tk()
root.title("Memo")
root.geometry("400x400")

def open_file():
    fin = askopenfile(title="Open")
    if fin:
        listbox.delete(0, tkinter.END)
        items = fin.readlines()
        for item in items:
            listbox.insert(tkinter.END, item.strip())

def save_file():
    fout = asksaveasfile(title="Save")
    if fout:
        items = listbox.get(0, tkinter.END)
        for item in items:
          print(item.strip(),file=fout)

def add_item():
    item_text = item.get()
    if item_text:
        listbox.insert(tkinter.END, item_text)
        item.delete(0, tkinter.END)

def delete_item():
    index = listbox.curselection()
    if index:
        listbox.delete(index)

f_open = tkinter.Button(root, text="Open", command=open_file)
f_open.pack(pady=5)
f_save = tkinter.Button(root, text="Save", command=save_file)
f_save.pack(pady=5)
f_add = tkinter.Button(root, text="Add", command=add_item)
f_add.pack(pady=5)
f_delete = tkinter.Button(root, text="Delete", command=delete_item)
f_delete.pack(pady=5)   

item = tkinter.Entry(root, width=30)
item.pack(pady=5)
listbox = tkinter.Listbox(root, width=50, height=10)
listbox.pack(pady=5)

root.mainloop()


       
    




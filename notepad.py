from tkinter import *
import tkinter.scrolledtext as ScrolledText 
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import os

root=Tk()
root.title("NOTEPAD")
root.geometry("300x150")
frame=Frame(root)

def new():
    if len(textarea.get("1.0",END+'-1c'))!=0:
        if messagebox.askyesno("Save","Do you wish to save existing file?"):
           save()
        else :
           textarea.delete("1.0",END)
    else :
        textarea.delete("1.0",END)
def open():
    textarea.delete("1.0",END)
    file=askopenfile(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")]) 
    root.title(os.path.basename(file.name) + " - Notepad")
    if file!=None:
        contents=file.read()
        textarea.insert('1.0',contents)
        file.close()
       
def save():
    if len(textarea.get("1.0",END+'-1c'))==0:
        messagebox.showinfo("Empty Document","Write something")
    else:   
        file=asksaveasfile(mode='w')
        if file!=None:
           contents=textarea.get('1.0',END)
           file.write(contents)
           file.close()
           root.title(os.path.basename(file.name) + " - Notepad")   
         
def cut():
        textarea.event_generate("<<Cut>>") 

def copy():
        textarea.event_generate("<<Copy>>")
        
def paste():
        textarea.event_generate("<<Paste>>")
        
def knowmore():
        label=messagebox.showinfo("HELLO",message="This is a python application for Notepad")
        
def search():
    findword=askstring("findword","Enter the word:")
    word=textarea.get("1.0",END)
    count=word.count(findword)
    if word.count(findword)>0:
       messagebox.showinfo("Count",count)

def exitapp():
    if messagebox.askyesno("Quit","ARE YOU SURE YOU WANT TO EXIT?"):
       root.destroy()

def delete():
    textarea.delete("1.0",END)


textarea=ScrolledText.ScrolledText(frame)
textarea.pack()
scrollbar=Scrollbar(textarea)
menu=Menu(root)
root.configure(menu=menu)
button1=Button(text="SAVE", font=("Arial",10,"bold"),command=save,fg="black",bg="white",height=2,width=10)
button2=Button(text="Delete",font=("Arial",10,"bold"),command=delete,fg="black",bg="white",height=2,width=10)


submenu1=Menu(root) 
submenu2=Menu(root)
submenu3=Menu(root)
submenu4=Menu(root)

menu.add_cascade(label="File",menu=submenu1)
menu.add_cascade(label="Edit",menu=submenu2)
menu.add_cascade(label="Extra",menu=submenu3)
menu.add_cascade(label="About",menu=submenu4)


submenu1.add_command(label="New",command=new)
submenu1.add_separator()
submenu1.add_command(label="Open",command=open)
submenu1.add_separator()
submenu1.add_command(label="Save",command=save)
submenu1.add_separator()
submenu1.add_command(label="Saveas",command=save)
submenu1.add_separator()
submenu1.add_command(label="Exit",command=exitapp)

submenu2.add_command(label="Cut",command=cut)
submenu2.add_command(label="Copy",command=copy)
submenu2.add_command(label="Paste",command=paste)

submenu3.add_command(label="Search",command=search)
submenu4.add_command(label="Know more",command=knowmore)


button1.pack(padx=5,pady=5,side=BOTTOM)
button2.pack(padx=5,pady=5,side=BOTTOM)
frame.pack(fill=BOTH,expand=True)

root.mainloop()    

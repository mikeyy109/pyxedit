'''
Author: Mike Clarke 13/09/14
'''

import Tkinter as tk
import ScrolledText
import tkFileDialog
import tkMessageBox

main = tk.Tk(className=" Pyxedit")
text_area = ScrolledText.ScrolledText(main, width=100, height=80)

def open_cmd():
    file = tkFileDialog.askopenfile(parent=main, mode='rb', title='Select a file')
    if file != None:
        contents = file.read()
        text_area.insert('1.0', contents)
        file.close()

def save_cmd(self):
    file = tkFileDialog.asksaveasfile(mode='w')
    data = self.text_area.get('1.0')
    file.write(data)
    file.close()

def exit():
    if tkMessageBox.askokcancel('Exit', 'Are you sure?'):
        main.destroy()

def dummy():
    pass

menu = tk.Menu(main)
main.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=dummy)
filemenu.add_command(label="Open...", command=open_cmd)
filemenu.add_command(label="Save", command=save_cmd)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit())
helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=dummy)
# end of menu creation

text_area.pack()
main.mainloop()



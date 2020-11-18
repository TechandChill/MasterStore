from tkinter import *

from art import text2art

import config
import update

print(text2art("MasterStore"))
print("App started.")


root = Tk() 
  
root.title("Project MasterStore-Dev") 
root.geometry('900x720')

if(config.check_for_updates == True):
    update.check_version()
else:
    pass

title = Label(root, text = f"Project Masterstore v{config.version}", fg="#f93434", font=("Helvetica", 18))
title.grid(row=0, column=0)


root.mainloop()

from tkinter import messagebox
import config

def check_version():
    if(config.version >= config.latest_version):
        messagebox.showinfo("Info", "Masterstore is updated.")
    else:
        messagebox.showwarning("Warning", f"MasterStore is not up-to-date\nYou should upgrade to have access to more apps and a\nbetter experience.\n\nYour version: {config.version}.\n\nThe latest version: {config.latest_version}.")


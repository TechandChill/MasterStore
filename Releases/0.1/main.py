import htmlPy
import os

app = htmlPy.AppGUI(title=u"Project MasterStore-Dev", maximized=True)

app.template_path = os.path.abspath(".")
app.static_path = os.path.abspath(".")

app.template = ("index.html", {"username": "htmlPy_user"})

from art import text2art

import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)


print(text2art("MasterStore"))
print("App started.")

app.start()
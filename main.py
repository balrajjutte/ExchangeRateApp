import requests
import csv
import tkinter as tk
import re
from tkinter import messagebox

code_country = {}
window_dict = {}
drop_down_list = []
f = open("country_codes.txt")
csv_file = csv.reader(f)
for row in csv_file:
    name, code = row
    code_country[code] = name
    drop_down_list.append(f"{code}, {name}")
    window_dict[f"{code}, {name}"] = code
f.close()



url = "http://data.fixer.io/api/latest?access_key=67dabe04a605431de7fa9dc3c6134360"
response = requests.get(url)
rates = response.json()["rates"]


def calculator(base_eur_rate, target_eur_rate, base_code, target_code):
    exchange_rate = target_eur_rate/base_eur_rate
    exchange_label["text"] = f"Exchange Rate:\n{base_code} to {target_code}\n{exchange_rate:.3f}"
    moneyin_label["text"] = f"Input:   ({base_code})"
    moneyout_label["text"] = f"Output: ({target_code})"

def datafetch():
    base_currency = lbxbase.get(tk.ACTIVE)
    base_code = window_dict[base_currency]
    base_eur_rate = rates[base_code]
    target_currency = lbxtarget.get(tk.ACTIVE)
    target_code = window_dict[target_currency]
    target_eur_rate = rates[target_code]
    calculator(base_eur_rate, target_eur_rate, base_code, target_code)

def get_exchange(input):
    text = exchange_label["text"]
    try:
        output = float(input) * float(text[26:])
        moneyoutput_label["text"] = output
    except:
        moneyoutput_label["text"] = ""

HEIGHT = 400
WIDTH = 700
black = "black"
green = "#00FF00"
white = "white"

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg=black, bd=5)
canvas.pack()

base_frame = tk.Frame(root, bg=green, bd=5)
base_frame.place(relx=0.01, rely=0.01, relwidth=0.49, relheight=0.48)
labelbase = tk.Label(base_frame, text="Base Currency", font=("Verdana", 12), bg=black, fg=white)
labelbase.place(relwidth=1, relheight=0.17)
sbrbase = tk.Scrollbar(base_frame)
sbrbase.place(relx=0.95, rely=0.2, relwidth=0.05, relheight=0.6)
lbxbase = tk.Listbox(base_frame, font=("Verdana", 12), bg=black, fg=white)
lbxbase.place(relx=0, rely=0.2, relwidth=0.95, relheight=0.6)
n = 0
for element in drop_down_list:
    lbxbase.insert(n, element)
    n += 1

sbrbase.config(command=lbxbase.yview)
lbxbase.config(yscrollcommand=sbrbase.set)

btnbase = tk.Button(base_frame, text="Select", bg= black, fg=white, font=("Verdana", 16), command=datafetch)
btnbase.place(relx=0.4, rely=0.82, relwidth=0.2, relheight=0.18)


target_frame = tk.Frame(root, bg=green, bd=5)
target_frame.place(relx=0.51, rely=0.01, relwidth=0.48, relheight=0.48)

labeltarget = tk.Label(target_frame, text="Target Currency", fg=white, font=("Verdana", 12), bg=black)
labeltarget.place(relheight=0.17, relwidth=1)
sbrtarget = tk.Scrollbar(target_frame)
sbrtarget.place(relx=0.95, rely=0.2, relwidth=0.05, relheight=0.6)
lbxtarget = tk.Listbox(target_frame, font=("Verdana", 12), bg=black, fg=white)
lbxtarget.place(relx=0, rely=0.2, relwidth=0.95, relheight=0.6)
n = 0
for element in drop_down_list:
    lbxtarget.insert(n, element)
    n += 1

sbrtarget.config(command=lbxbase.yview)
lbxtarget.config(yscrollcommand=sbrtarget.set)

btntarget = tk.Button(target_frame, text="Select", bg= black, fg=white, font=("Verdana", 16), command=datafetch)
btntarget.place(relx=0.4, rely=0.82, relwidth=0.2, relheight=0.18)

exchange_frame = tk.Frame(root, bg=green, bd=5)
exchange_frame.place(relx=0.51, rely=0.51, relwidth=0.48, relheight=0.48)
exchange_label = tk.Label(exchange_frame, fg=white, bg=black, font=("Verdana", 28), text="Exchange Rate:")
exchange_label.place(relheight=1, relwidth=1)

money_frame = tk.Frame(root, bg=green, bd=5)
money_frame.place(relx=0.01, rely=0.51, relwidth=0.49, relheight=0.48)
money_label = tk.Label(money_frame, bg=black, fg=white, font=("Verdana", 16), text="CASH EXCHANGE")
money_label.place(relheight=0.3, relwidth=0.6)
moneyin_label = tk.Label(money_frame, bg=black, fg=white, font=("Verdana", 20), text=f"Input:   ()", justify="left", anchor="w")
moneyin_label.place(rely=0.35, relheight=0.30, relwidth=0.6)
moneyout_label = tk.Label(money_frame, bg=black, fg=white,font=("Verdana", 20), text=f"Output: ()", justify="left", anchor="w")
moneyout_label.place(rely=0.69, relheight=0.30, relwidth=0.6)
entry = tk.Entry(money_frame, bg=black,fg=white, font=("Verdana", 16))
entry.place(relx= 0.62, rely=0.35, relheight=0.3, relwidth=0.38)
xch = tk.Button(money_frame, bg=black, font=("Verdana", 20),fg=white, text="XCH", command=lambda : get_exchange(entry.get()))
xch.place(relx= 0.62, relheight=0.3, relwidth=0.38)
moneyoutput_label = tk.Label(money_frame, bg=black, font=("Verdana", 16), justify="left", anchor="w", fg=white)
moneyoutput_label.place(relx= 0.62, rely=0.69, relheight=0.3, relwidth=0.38)
root.mainloop()


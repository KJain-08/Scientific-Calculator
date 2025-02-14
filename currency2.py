from tkinter import *
import requests as requests

guiWindow = Tk()
input_value = StringVar(guiWindow)
output_value = StringVar(guiWindow)
input_value.set("currency")
output_value.set("currency")

def RealTimeCurrencyConversion():
    from_currency = input_value.get()
    to_currency = output_value.get()
    api_key = "YOUR-API-KEY"
    base_url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    main_url = f"{base_url}&from_currency={from_currency}&to_currency={to_currency}&apikey={api_key}"

    try:
        req_ob = requests.get(main_url, verify=True)
        result = req_ob.json()

        exchange_rate = float(result["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
        try:
            amount = float(input_field.get())
        except ValueError:
            output_field.delete(0, END)
            output_field.insert(0, "Invalid Input")
            return
        
        fromcountry = result["Realtime Currency Exchange Rate"]["2. From_Currency Name"]
        tocountry = result["Realtime Currency Exchange Rate"]["4. To_Currency Name"]
        to_country.config(text=tocountry)
        from_country.config(text=fromcountry)

        new_amount = round(amount * exchange_rate, 3)
        output_field.delete(0, END)
        output_field.insert(0, str(new_amount))

    except KeyError:
        output_field.delete(0, END)
        output_field.insert(0, "Invalid Currency Pair")

def clear_all():
    input_field.delete(0, END)
    output_field.delete(0, END)

guiWindow.title("Real-Time Currency Converter")
guiWindow.geometry("500x600")
guiWindow.resizable(width=False, height=False)
guiWindow.configure(bg="#232323")

header_frame = Frame(guiWindow, bg="#232323")
header_frame.pack(expand=True, fill="both", ipady=20)
body_frame = Frame(guiWindow, bg="#232323")
body_frame.pack(expand=True, fill="both", pady=30)

header_label = Label(header_frame, text="REAL-TIME CURRENCY CONVERTER", font=("Georgia", 18, "bold"), bg="#16a085",fg="#e8f6f3",wraplength=400)
header_label.pack(expand=True, fill="both")

input_label = Label(body_frame, text="From:", font=("Georgia", 18, "bold"), bg="#232323", fg="white")
input_label.grid(row=1, column=0, padx=15)
output_label = Label(body_frame,text="To:",font=("Georgia", 18, "bold"),bg="#232323",fg="white")
output_label.grid(row=5, column=0, padx=15)

input_field = Entry(body_frame, font=('Georgia', 12, 'bold'), fg='black', width=20, bd=1, justify="center", border=2)
input_field.grid(row=1, column=1, padx=20, pady=10, ipady=5)

output_field = Entry(body_frame, font=('Georgia', 12, 'bold'), fg='black', width=20, bd=1, justify="center", border=2)
output_field.grid(row=5, column=1, padx=20, ipady=5)

CurrenyCode_list = ["AED","AUD","BDT","CAD","CHF","CNY","COP","EGP","EUR","HKD","IDR","ILS","INR","IQD","IRR","JPY","KES","KHR","KPW","KRW","KWD","LBP","LKR","MXN","MYR","NOK","NPR","NZD","OMR","PHP","PKR","QAR","RON","RSD","RUB","SGD","SYP","TRY","USD","YER","ZAR","ZWL"]

input_menu = OptionMenu(body_frame, input_value, *CurrenyCode_list)
output_menu = OptionMenu(body_frame, output_value, *CurrenyCode_list)
input_menu.config(font=("Georgia", 8, "bold"), width=8, bg="#232323", border=0, fg="white")
output_menu.config(font=("Georgia", 8, "bold"), bg="#232323", fg="white", width=8)

input_menu.grid(row=2, column=1, padx = 10,pady=5,ipadx=2, ipady=4)
output_menu.grid(row=3, column=1,padx=10,pady=5,ipadx=2, ipady=4)

from_country = Label(body_frame, text="", bg="#232323",fg="white", font=("Georgia", 12, "bold"))
from_country.grid(row=1, column=3)

to_country = Label(body_frame, text="", bg = "#232323",fg="white", font=("Georgia", 12, "bold"))
to_country.grid(row=5, column=3)

convert_button = Button(body_frame, font=("Georgia", 12, "bold"), text="CONVERT", bg="#16a085", fg="#ffffff",
                        command=RealTimeCurrencyConversion)
reset_button = Button(body_frame, font=("Georgia", 12, "bold"), text="RESET", bg="#16a085", fg="#ffffff", command=clear_all)

convert_button.grid(row=4, column=1, pady=15, ipady=5, ipadx=20)
reset_button.grid(row=6, column=1, pady=15, ipady=5, ipadx=32)

guiWindow.mainloop()

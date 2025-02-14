import tkinter as tk
import subprocess

def open_sci_calculator():
    try:
        subprocess.run(["python", "page3.py"])
    except Exception as e:
        print(f"Error running Scientific Calculator: {e}")

def open_currency_converter():
    try:
        subprocess.run(["python", "currency2.py"])
    except Exception as e:
        print(f"Error running currency Converter: {e}")

def open_unit_converter():
    try:
        subprocess.run(["python", "unit.py"])
    except Exception as e:
        print(f"Error running unit converter: {e}")

def exit_application():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Welcome to Calculator")
root.geometry("500x300")
root.configure(bg="#232323")

# Welcome Label
welcome_label = tk.Label(root, text="Welcome to Calculator", font=("Georgia", 18,"bold"), bg="#232323",fg="white", pady=20)
welcome_label.pack()

# Buttons
button_frame = tk.Frame(root, bg="#232323")
button_frame.pack()

sci_cal_button = tk.Button(button_frame, text="Sci Calculator",width=14,  command=open_sci_calculator, font=("Georgia", 14,"bold"), padx=10, pady=5, bg="#4CAF50", fg="white")
sci_cal_button.grid(row=0, column=0, padx=10, pady=10,ipadx=5,ipady=5)

currency_button = tk.Button(button_frame, text="Currency Converter",width=14,  command=open_currency_converter, font=("Georgia", 14,"bold"), padx=10, pady=5, bg="#3498db", fg="white")
currency_button.grid(row=0, column=1, padx=10, pady=10,ipadx=5,ipady=5)

unit_converter_button = tk.Button(button_frame, text="Unit Converter",width=14,  command=open_unit_converter, font=("Georgia", 14,"bold"), padx=10, pady=5, bg="#e67e22", fg="white")
unit_converter_button.grid(row=1, column=0, padx=10, pady=10,ipadx=5,ipady=5)

exit_button = tk.Button(button_frame, text="Exit", width=14, command=exit_application, font=("Georgia", 14,"bold"), padx=10, pady=5, bg="#e74c3c", fg="white")
exit_button.grid(row=1, column=1, padx=10, pady=10,ipadx=5,ipady=5)

# Run the GUI
root.mainloop()

import tkinter as tk
from time import sleep
from tkinter import messagebox

def on_calculate():
    calc_type = type_var.get()
    if calc_type == "Compounding":
        calc_deposit = deposit_var.get()
        calc_rate = rate_var.get() / 100
        calc_length = length_var.get() / 12
        calc_compounding = compounding_var.get()
        if calc_compounding == "Yearly":
            calc_terms = 1
        if calc_compounding == "Monthly":
            calc_terms = 12 
        if calc_compounding == "Daily":
            calc_terms = 365
        print("calc_terms = ", calc_terms)
        calc_earned = round((calc_deposit * (1 + calc_rate / calc_terms) ** (calc_terms * calc_length) - calc_deposit), 2)
        print("calc_earned (compounding) = ", calc_earned)
    else:
        calc_deposit = deposit_var.get()
        calc_rate = rate_var.get() / 100
        calc_length = length_var.get() / 12

        calc_earned = round(calc_deposit * calc_rate * calc_length, 2)
        print("calc_earned (normal) = ", calc_earned)

    calc_total = round(calc_deposit + calc_earned, 2)
    earned_entry.delete(0, tk.END)
    earned_entry.insert(0, f"{calc_earned}")
    total_entry.delete(0, tk.END)
    total_entry.insert(0, f"{calc_total}")
  

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        print("Exiting...")
        root.destroy()

if __name__ == "__main__":
    if messagebox.askokcancel("Interest & Compound Interest Rate Calculator", "This is a term deposit calculator. For a normal interest rate, the total amount is paid at the end of the term based on the initial deposit. For a compounded rate, the interest is calculated based on the terms agreed to every day, month, or year. Compounding a deposit every day may sound appealing, but often hidden fees or a less attractive rate may be involved. Be sure to confirm with your bank before locking your money away for a long time."):
        root = tk.Tk()
        root.title("Interest & Compound Interest Rate Calculator")
    
        deposit_var = tk.DoubleVar(value=1000)
        rate_var = tk.DoubleVar(value=5)
        length_var = tk.IntVar(value=12)
        
        types_var = ['Normal', 'Compounding']
        type_var = tk.StringVar()
        type_var.set(types_var[0])
        
        compoundings_var = ['Yearly', 'Monthly', 'Daily']
        compounding_var = tk.StringVar()
        compounding_var.set(compoundings_var[0])
        
        earned_var = tk.DoubleVar(value=50)
        total_var = tk.DoubleVar(value=1050)

        deposit_label = tk.Label(root, text="Deposit Amount ($): ", font=("Arial", 14), padx=20)
        rate_label = tk.Label(root, text="Interest Rate (%): ", font=("Arial", 14), padx=20)
        length_label = tk.Label(root, text="Length (months): ", font=("Arial", 14), padx=20)
        type_label = tk.Label(root, text="Interest Type: ", font=("Arial", 14), padx=20)
        compounding_label = tk.Label(root, text="Compounding: ", font=("Arial", 14), padx=20)
        calculate_button = tk.Button(root, text="Calculate", command=on_calculate)
        earned_label = tk.Label(root, text="Earned: ", font=("Arial", 14), padx=20)
        total_label = tk.Label(root, text="Total: ", font=("Arial", 14), padx=20)
    
        deposit_entry = tk.Entry(root, textvariable=deposit_var, font=("Arial", 18), width=14)
        rate_entry = tk.Entry(root, textvariable=rate_var, font=("Arial", 18), width=14)
        length_entry = tk.Entry(root, textvariable=length_var, font=("Arial", 18), width=14)
        type_option = tk.OptionMenu(root, type_var, *types_var)
        compounding_option = tk.OptionMenu(root, compounding_var, *compoundings_var)
        earned_entry = tk.Entry(root, textvariable=earned_var, font=("Arial", 18), width=14)
        total_entry = tk.Entry(root, textvariable=total_var, font=("Arial", 18), width=14)

        type_option.config(width=16)
        type_option.config(height=1)
        type_option.config(bg='yellow')

        compounding_option.config(width=16)
        compounding_option.config(height=1)
        compounding_option.config(bg='yellow')

        deposit_entry.config(bg='light blue')
        rate_entry.config(bg='light blue')
        length_entry.config(bg='light blue')
        earned_entry.config(bg='light blue')
        total_entry.config(bg='light blue')

        calculate_button.config(bg='orange')

        deposit_label.grid(row=0, column=0)
        deposit_entry.grid(row=0, column=1)
        rate_label.grid(row=1, column=0)
        rate_entry.grid(row=1, column=1)
        length_label.grid(row=2, column=0)
        length_entry.grid(row=2, column=1)
        type_label.grid(row=3, column=0)
        type_option.grid(row=3, column=1)
        compounding_label.grid(row=4, column=0)
        compounding_option.grid(row=4, column=1)
        calculate_button.grid(row=5, column=0)
        earned_label.grid(row=6, column=0)
        earned_entry.grid(row=6, column=1)
        total_label.grid(row=7, column=0)
        total_entry.grid(row=7, column=1)

        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=on_closing)
        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)
    
    while True: # mainloop()
        root.update_idletasks()
        root.update()
        root.protocol("WM_DELETE_WINDOW", on_closing)
        sleep(0.1)



import tkinter as tk
from tkinter import ttk

# Ana pencere
root = tk.Tk()
root.title("Hesap Makinesi")
root.geometry("300x400")

# Ekran (display)
display = tk.Entry(root, font=("Arial", 24), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Butonlar
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*',
    '1','2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, font=("Arial", 18),
            command=lambda b=button: click(b)).grid(row=row_val, column=col_val, sticky="nsew")
    col_val +=1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Temel Fonksiyonlar
def click(button):
    if button == '=':
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(0, "Hata!")
    elif button == 'C':
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, button)

# Temizle butonu
tk.Button(root, text="C", font=("Arial", 18), 
          command=lambda: display.delete(0, tk.END)).grid(row=5, column=0, columnspan=2, sticky='nsew')

# Pencereyi başlat
root.mainloop()



                                                    
        
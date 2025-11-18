import tkinter as tk
from tkinter import ttk
from math import sqrt
import random

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Калькулятор")
        self.master.geometry("450x200")

        self.signature_label = ttk.Label(
            self.master,
            text="Выполнил: Семенков Роман",
            font=("Georgia", 10),
            foreground="dark blue"
        )
        self.signature_label.place(relx=1.0, rely=-0.02, anchor="ne", x=-6.5, y=9)

        self.number_entry = ttk.Entry(self.master, width=35, font=("Arial", 12))
        self.number_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w")

        style = ttk.Style()
        style.configure("Large.TButton", font=("Arial", 11), padding=8)

        self.button_1 = ttk.Button(self.master, text="1", command=lambda: self.button_click(1), style="Large.TButton")
        self.button_2 = ttk.Button(self.master, text="2", command=lambda: self.button_click(2), style="Large.TButton")
        self.button_3 = ttk.Button(self.master, text="3", command=lambda: self.button_click(3), style="Large.TButton")
        self.button_4 = ttk.Button(self.master, text="4", command=lambda: self.button_click(4), style="Large.TButton")
        self.button_5 = ttk.Button(self.master, text="5", command=lambda: self.button_click(5), style="Large.TButton")
        self.button_6 = ttk.Button(self.master, text="6", command=lambda: self.button_click(6), style="Large.TButton")
        self.button_7 = ttk.Button(self.master, text="7", command=lambda: self.button_click(7), style="Large.TButton")
        self.button_8 = ttk.Button(self.master, text="8", command=lambda: self.button_click(8), style="Large.TButton")
        self.button_9 = ttk.Button(self.master, text="9", command=lambda: self.button_click(9), style="Large.TButton")
        self.button_0 = ttk.Button(self.master, text="0", command=lambda: self.button_click(0), style="Large.TButton")
        self.button_clear = ttk.Button(self.master, text="C", command=self.button_clear, style="Large.TButton")
        self.button_add = ttk.Button(self.master, text="+", command=self.button_add, style="Large.TButton")
        self.button_equal = ttk.Button(self.master, text="=", command=self.button_equal, style="Large.TButton")
        self.button_subtract = ttk.Button(self.master, text="-", command=self.button_subtract, style="Large.TButton")
        self.button_multiply = ttk.Button(self.master, text="*", command=self.button_multiply, style="Large.TButton")
        self.button_divide = ttk.Button(self.master, text="/", command=self.button_divide, style="Large.TButton")
        self.button_floor_div = ttk.Button(self.master, text="//", command=self.button_floor_div, style="Large.TButton")
        self.button_modulus = ttk.Button(self.master, text="%", command=self.button_modulus, style="Large.TButton")
        self.button_sqrt = ttk.Button(self.master, text="√", command=self.button_sqrt_with_effect, style="Large.TButton")
        self.button_neg = ttk.Button(self.master, text="+/-", command=self.button_neg, style="Large.TButton")

        self.button_1.grid(row=1, column=0, padx=3, pady=3)
        self.button_2.grid(row=1, column=1, padx=3, pady=3)
        self.button_3.grid(row=1, column=2, padx=3, pady=3)
        self.button_add.grid(row=1, column=3, padx=3, pady=3)
        self.button_floor_div.grid(row=1, column=4, padx=3, pady=3)

        self.button_4.grid(row=2, column=0, padx=3, pady=3)
        self.button_5.grid(row=2, column=1, padx=3, pady=3)
        self.button_6.grid(row=2, column=2, padx=3, pady=3)
        self.button_subtract.grid(row=2, column=3, padx=3, pady=3)
        self.button_modulus.grid(row=2, column=4, padx=3, pady=3)

        self.button_7.grid(row=3, column=0, padx=3, pady=3)
        self.button_8.grid(row=3, column=1, padx=3, pady=3)
        self.button_9.grid(row=3, column=2, padx=3, pady=3)
        self.button_multiply.grid(row=3, column=3, padx=3, pady=3)
        self.button_sqrt.grid(row=3, column=4, padx=3, pady=3)

        self.button_clear.grid(row=4, column=0, padx=3, pady=3)
        self.button_0.grid(row=4, column=1, padx=3, pady=3)
        self.button_equal.grid(row=4, column=2, padx=3, pady=3)
        self.button_divide.grid(row=4, column=3, padx=3, pady=3)
        self.button_neg.grid(row=4, column=4, padx=3, pady=3)

        self.f_num = 0
        self.math = ""

    def create_splash_effect(self):
        canvas = tk.Canvas(self.master, width=450, height=200, bg='white', highlightthickness=0)
        canvas.place(x=0, y=0)
        
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']
        
        for _ in range(50):
            x = random.randint(0, 450)
            y = random.randint(0, 200)
            size = random.randint(5, 20)
            color = random.choice(colors)
            
            canvas.create_oval(x, y, x+size, y+size, fill=color, outline=color)
        
        def remove_effect():
            canvas.destroy()
        
        self.master.after(1000, remove_effect)

    def button_sqrt_with_effect(self):
        self.create_splash_effect()
        self.button_sqrt()

    def button_click(self, number):
        current = self.number_entry.get()
        self.number_entry.delete(0, tk.END)
        self.number_entry.insert(0, str(current) + str(number))

    def button_clear(self):
        self.number_entry.delete(0, tk.END)

    def button_add(self):
        try:
            first_number = float(self.number_entry.get())
            self.math = "addition"
            self.f_num = first_number
            self.number_entry.delete(0, tk.END)
        except ValueError:
            self.number_entry.delete(0, tk.END)
            self.number_entry.insert(0, "Ошибка ввода")

    def button_equal(self):
        try:
            second_number_str = self.number_entry.get()
            if not second_number_str:
                return

            second_number = float(second_number_str)
            self.number_entry.delete(0, tk.END)

            if self.math == "addition":
                result = self.f_num + second_number

            elif self.math == "subtraction":
                result = self.f_num - second_number

            elif self.math == "multiplication":
                result = self.f_num * second_number

            elif self.math == "division":
                if second_number == 0:
                    self.number_entry.insert(0, "Деление на ноль")
                    return
                result = self.f_num / second_number

            elif self.math == "floor_div":
                if second_number == 0:
                    self.number_entry.insert(0, "Деление на ноль")
                    return
                result = self.f_num // second_number

            elif self.math == "modulus":
                if second_number == 0:
                    self.number_entry.insert(0, "Деление на ноль")
                    return
                result = self.f_num % second_number

            else:
                result = second_number

            if result == int(result):
                self.number_entry.insert(0, int(result))
            else:
                self.number_entry.insert(0, round(result, 10))

        except ValueError:
            self.number_entry.insert(0, "Ошибка ввода")
        except Exception as e:
            self.number_entry.insert(0, f"Ошибка: {str(e)}")

    def button_subtract(self):
        try:
            first_number = float(self.number_entry.get())
            self.math = "subtraction"
            self.f_num = first_number
            self.number_entry.delete(0, tk.END)
        except ValueError:
            self.number_entry.delete(0, tk.END)
            self.number_entry.insert(0, "Ошибка ввода")

    def button_multiply(self):
        try:
            first_number = float(self.number_entry.get())
            self.math = "multiplication"
            self.f_num = first_number
            self.number_entry.delete(0, tk.END)
        except ValueError:
            self.number_entry.delete(0, tk.END)
            self.number_entry.insert(0, "Ошибка ввода")

    def button_divide(self):
        try:
            first_number = float(self.number_entry.get())
            self.math = "division"
            self.f_num = first_number
            self.number_entry.delete(0, tk.END)
        except ValueError:
            self.number_entry.delete(0, tk.END)
            self.number_entry.insert(0, "Ошибка ввода")

    def button_floor_div(self):
        try:
            first_number = float(self.number_entry.get())
            self.math = "floor_div"
            self.f_num = first_number
            self.number_entry.delete(0, tk.END)
        except ValueError:
            self.number_entry.delete(0, tk.END)
            self.number_entry.insert(0, "Ошибка ввода")

    def button_modulus(self):
        try:
            first_number = float(self.number_entry.get())
            self.math = "modulus"
            self.f_num = first_number
            self.number_entry.delete(0, tk.END)
        except ValueError:
            self.number_entry.delete(0, tk.END)
            self.number_entry.insert(0, "Ошибка ввода")

    def button_sqrt(self):
        try:
            number_str = self.number_entry.get()
            if not number_str:
                return

            number = float(number_str)
            if number < 0:
                self.number_entry.delete(0, tk.END)
                self.number_entry.insert(0, "Нельзя вычесть корень из отрицательного",)
                return

            result = sqrt(number)
            if result.is_integer():
                self.number_entry.delete(0, tk.END)
                self.number_entry.insert(0, int(result))
            else:
                self.number_entry.delete(0, tk.END)
                self.number_entry.insert(0, round(result, 10))
        except ValueError:
            self.number_entry.delete(0, tk.END)
            self.number_entry.insert(0, "Ошибка ввода")
        except Exception as e:
            self.number_entry.delete(0, tk.END)
            self.number_entry.insert(0, f"Ошибка: {str(e)}")

    def button_neg(self):
        try:
            current = self.number_entry.get()
            if current in ["Ошибка ввода", "Деление на ноль", "Нельзя вычесть корень из отрицательного", "Неизвестная операция"]:
                self.number_entry.delete(0, tk.END)
                return

            if current.startswith("-"):
                current = current[1:]
            elif current:
                current = "-" + current
            self.number_entry.delete(0, tk.END)
            self.number_entry.insert(0, current)
        except:
            self.number_entry.delete(0, tk.END)
            self.number_entry.insert(0, "Ошибка ввода")

if __name__ == '__main__':
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
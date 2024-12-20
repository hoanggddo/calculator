import tkinter as tk
from tkinter import messagebox

def arithmetic_operations():
    def calculate():
        try:
            left = int(entry_left.get())
            right = int(entry_right.get())
            operation = operation_var.get()

            if operation == "Addition":
                result = left + right
            elif operation == "Subtraction":
                result = left - right
            elif operation == "Multiplication":
                result = left * right
            elif operation == "Division":
                result = left / right
            elif operation == "Floor Division":
                result = left // right
            elif operation == "Modulo":
                result = left % right
            elif operation == "Exponentiation":
                result = left ** right
            else:
                raise ValueError("Invalid operation selected")

            messagebox.showinfo("Result", f"The result is: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    arithmetic_window = tk.Toplevel(root)
    arithmetic_window.title("Arithmetic Operations")

    tk.Label(arithmetic_window, text="Left Number:").grid(row=0, column=0, padx=10, pady=5)
    entry_left = tk.Entry(arithmetic_window)
    entry_left.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(arithmetic_window, text="Right Number:").grid(row=1, column=0, padx=10, pady=5)
    entry_right = tk.Entry(arithmetic_window)
    entry_right.grid(row=1, column=1, padx=10, pady=5)

    operation_var = tk.StringVar(value="Addition")
    tk.Label(arithmetic_window, text="Operation:").grid(row=2, column=0, padx=10, pady=5)
    operations_menu = tk.OptionMenu(
        arithmetic_window, operation_var, "Addition", "Subtraction", "Multiplication", "Division", "Floor Division", "Modulo", "Exponentiation"
    )
    operations_menu.grid(row=2, column=1, padx=10, pady=5)

    tk.Button(arithmetic_window, text="Calculate", command=calculate).grid(row=3, columnspan=2, pady=10)

def quadratic_solver():
    def solve():
        try:
            a = int(entry_a.get())
            b = int(entry_b.get())
            c = int(entry_c.get())

            discriminant = (b ** 2 - 4 * a * c) ** 0.5
            root1 = (-b - discriminant) / (2 * a)
            root2 = (-b + discriminant) / (2 * a)

            messagebox.showinfo("Result", f"The roots are: {root1}, {root2}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    quadratic_window = tk.Toplevel(root)
    quadratic_window.title("Quadratic Equation Solver")

    tk.Label(quadratic_window, text="Coefficient a:").grid(row=0, column=0, padx=10, pady=5)
    entry_a = tk.Entry(quadratic_window)
    entry_a.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(quadratic_window, text="Coefficient b:").grid(row=1, column=0, padx=10, pady=5)
    entry_b = tk.Entry(quadratic_window)
    entry_b.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(quadratic_window, text="Coefficient c:").grid(row=2, column=0, padx=10, pady=5)
    entry_c = tk.Entry(quadratic_window)
    entry_c.grid(row=2, column=1, padx=10, pady=5)

    tk.Button(quadratic_window, text="Solve", command=solve).grid(row=3, columnspan=2, pady=10)

def gcd_solver():
    def find_gcd():
        try:
            big = int(entry_big.get())
            small = int(entry_small.get())

            while small != 0:
                big, small = small, big % small

            messagebox.showinfo("Result", f"The GCD is: {big}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    gcd_window = tk.Toplevel(root)
    gcd_window.title("Greatest Common Denominator")

    tk.Label(gcd_window, text="Larger Number:").grid(row=0, column=0, padx=10, pady=5)
    entry_big = tk.Entry(gcd_window)
    entry_big.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(gcd_window, text="Smaller Number:").grid(row=1, column=0, padx=10, pady=5)
    entry_small = tk.Entry(gcd_window)
    entry_small.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(gcd_window, text="Find GCD", command=find_gcd).grid(row=2, columnspan=2, pady=10)

root = tk.Tk()
root.title("Texas Instruments")

name_label = tk.Label(root, text="Welcome! Enter your name:")
name_label.pack(pady=10)

name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Button(root, text="Arithmetic", command=arithmetic_operations).pack(pady=5)
tk.Button(root, text="Quadratic Equation Solver", command=quadratic_solver).pack(pady=5)
tk.Button(root, text="Greatest Common Denominator", command=gcd_solver).pack(pady=5)

root.mainloop()

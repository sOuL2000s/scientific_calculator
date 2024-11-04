
import tkinter as tk
from math import sin, cos, tan, sqrt, log, log10, exp, pow

def add_to_expression(value):
    expression_field.insert(tk.END, value)

def clear_expression():
    expression_field.delete(0, tk.END)

def evaluate_expression():
    try:
        result = eval(expression_field.get())
        clear_expression()
        expression_field.insert(tk.END, result)
    except Exception as e:
        clear_expression()
        expression_field.insert(tk.END, "Error")

def calculate_function(func):
    try:
        value = float(expression_field.get())
        result = func(value)
        clear_expression()
        expression_field.insert(tk.END, result)
    except:
        clear_expression()
        expression_field.insert(tk.END, "Error")

def create_button(frame, text, command, bg_color):
    return tk.Button(frame, text=text, command=command, width=5, height=2, bg=bg_color, font=("Arial", 12))

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.config(bg="#2E3440")

expression_field = tk.Entry(root, font=("Arial", 18), bd=5, insertwidth=4, width=18, justify="right")
expression_field.grid(row=0, column=0, columnspan=5, pady=20)

button_frame = tk.Frame(root, bg="#3B4252")
button_frame.grid(row=1, column=0, columnspan=5)

buttons = [
    ('7', '8', '9', '/', 'sin'),
    ('4', '5', '6', '*', 'cos'),
    ('1', '2', '3', '-', 'tan'),
    ('0', '.', '=', '+', 'sqrt'),
    ('(', ')', 'log', 'log10', 'exp'),
    ('C', '**', 'pi', 'e', 'clr')
]

bg_colors = {
    'num': "#D08770",
    'op': "#88C0D0",
    'func': "#A3BE8C",
    'eq': "#EBCB8B",
    'clr': "#BF616A"
}

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text.isdigit() or text == '.':
            color = bg_colors['num']
            cmd = lambda x=text: add_to_expression(x)
        elif text in "+-*/()":
            color = bg_colors['op']
            cmd = lambda x=text: add_to_expression(x)
        elif text == '=':
            color = bg_colors['eq']
            cmd = evaluate_expression
        elif text == 'C':
            color = bg_colors['clr']
            cmd = clear_expression
        elif text == 'sin':
            color = bg_colors['func']
            cmd = lambda: calculate_function(sin)
        elif text == 'cos':
            color = bg_colors['func']
            cmd = lambda: calculate_function(cos)
        elif text == 'tan':
            color = bg_colors['func']
            cmd = lambda: calculate_function(tan)
        elif text == 'sqrt':
            color = bg_colors['func']
            cmd = lambda: calculate_function(sqrt)
        elif text == 'log':
            color = bg_colors['func']
            cmd = lambda: calculate_function(log)
        elif text == 'log10':
            color = bg_colors['func']
            cmd = lambda: calculate_function(log10)
        elif text == 'exp':
            color = bg_colors['func']
            cmd = lambda: calculate_function(exp)
        else:
            color = bg_colors['func']
            cmd = lambda x=text: add_to_expression(x)

        btn = create_button(button_frame, text, cmd, color)
        btn.grid(row=i, column=j, padx=5, pady=5)

root.mainloop()

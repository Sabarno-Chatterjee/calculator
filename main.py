# import art
# print(art.logo)
#
# def add(n1, n2):
#   return n1 + n2
#
# def subtract(n1, n2):
#   return n1 -  n2
#
# def multiply(n1, n2):
#   return n1 * n2
#
# def divide(n1, n2):
#   return n1/n2
#
#
# def calculations():
#   n1 = float(input("\nWhats the first number?\n"))
#
#   more_operations = True
#
#   while more_operations:
#       operator = input("\nWhats the operator? ('+', '-', '*', '/')\n")
#       n2 = float(input("\nWhats the next number?\n"))
#
#       calci = {
#         "+" :  add(n1,n2),
#         "-" :  subtract(n1, n2),
#         "*" :  multiply(n1, n2),
#         "/" :   divide(n1, n2),
#         }
#
#       operation = calci[operator]
#       print(f"\n{n1} {operator} {n2} = {operation}")
#       n1 = operation
#       if input(("\nPress enter to perform calculations with the same number or press N to start a new calculator.").lower()) == "n":
#         more_operations = False
#         calculations()
#
# calculations()


from tkinter import *

# Application Constants:
HEIGHT = 410
WIDTH = 310
window_bg = "#D8D9CF"
screen_bg = "#EDEDED"
black = "#000000"
white = "#FFFFFF"


# Setting up window and icon:
window = Tk()
window.title("Calculator")
icon = PhotoImage(file="icon.png")
window.iconphoto(False, icon)
window.config(padx=10, pady=10, bg=window_bg)

# Screen canvas:
screen_canvas = Canvas(width=300, height=70, bg=screen_bg)
screen_canvas.grid(row=0, column=0, columnspan=4, pady=10)

seven_button = Button(width=4, height=1, text="7", font=("arial", 20,"bold"), bg=black, fg=white)
seven_button.grid(row=1, column=0)

eight_button = Button(width=9, height=3)
eight_button.grid(row=1, column=1)

nine_button = Button(width=9, height=3)
nine_button.grid(row=1, column=2)

divide_button = Button(width=9, height=3)
divide_button.grid(row=1, column=3)

# 456* 123- 0C=+
four_button = Button(width=9, height=3)
four_button.grid(row=2, column=0)

five_button = Button(width=9, height=3)
five_button.grid(row=2, column=1)

six_button = Button(width=9, height=3)
six_button.grid(row=2, column=2)

multiply_button = Button(width=9, height=3)
multiply_button.grid(row=2, column=3)

one_button = Button(width=9, height=3)
one_button.grid(row=3, column=0)

two_button =Button(width=9, height=3)
two_button.grid(row=3, column=1)

three_button =Button(width=9, height=3)
three_button.grid(row=3, column=2)

minus_button =Button(width=9, height=3)
minus_button.grid(row=3, column=3)

zero_button =Button(width=9, height=3)
zero_button.grid(row=4, column=0)

clear_button =Button(width=9, height=3)
clear_button.grid(row=4, column=1)

equals_button =Button(width=9, height=3)
equals_button.grid(row=4, column=2)

add_button = Button(width=9, height=3)
add_button.grid(row=4, column=3)
# screen_canvas = Canvas(width=320, height=65, bg=screen2_bg, highlightthickness=0)
# screen_canvas.pack()


window.mainloop()

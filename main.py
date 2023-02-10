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
HEIGHT = 400
WIDTH = 300
window_bg = "#D8D9CF"
screen_bg = "#EDEDED"
black = "#000000"

# Setting up window and icon:
window = Tk()
window.title("Calculator")
icon = PhotoImage(file="icon.png")
window.iconphoto(False, icon)
window.config(padx=10, pady=10, bg=window_bg)

# Screen canvas:
screen_canvas = Canvas(width=300, height=60, bg=screen_bg)
screen_canvas.grid(row=0, column=0)




# screen_canvas = Canvas(width=320, height=65, bg=screen2_bg, highlightthickness=0)
# screen_canvas.pack()


window.mainloop()
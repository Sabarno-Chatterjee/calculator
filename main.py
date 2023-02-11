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
x_position = 280
y_position = 50
number = ""
# Setting up window and icon:
window = Tk()
window.title("Calculator")
icon = PhotoImage(file="icon.png")
window.iconphoto(False, icon)
window.config(padx=10, pady=10, bg=window_bg)


# Button functionality:
def AC():
    # screen_canvas.create_text(280,50, text="0", font=("arial", 30, "bold"))

    screen_canvas.itemconfig(display_number, text="0")
def seven():
    global number
    number = number + "7"
    screen_canvas.delete("all")
    screen_canvas.create_text(x_position, y_position, text=number, font=("arial", 30, "bold"))

def eight():
    global number
    number = number + "8"
    screen_canvas.delete("all")
    screen_canvas.create_text(x_position, y_position, text=number, font=("arial", 30, "bold"))
# Screen canvas:
screen_canvas = Canvas(width=310, height=70, bg=screen_bg)
display_number = screen_canvas.create_text(280,50, text="", font=("arial", 30, "bold"))
screen_canvas.grid(row=0, column=0, columnspan=4, pady=10)

seven_button = Button(width=4, height=1, text="7", font=("arial", 20, "bold"), bg=black, fg=white, command=seven)
seven_button.grid(row=1, column=0)

eight_button = Button(width=4, height=1, text="8", font=("arial", 20, "bold"), bg=black, fg=white, command=eight)
eight_button.grid(row=1, column=1)

nine_button = Button(width=4, height=1, text="9", font=("arial", 20, "bold"), bg=black, fg=white)
nine_button.grid(row=1, column=2)

divide_button = Button(width=4, height=1, text="/", font=("arial", 20, "bold"), bg=black, fg=white)
divide_button.grid(row=1, column=3)

# 456* 123- 0C=+
four_button = Button(width=4, height=1, text="4", font=("arial", 20, "bold"), bg=black, fg=white)
four_button.grid(row=2, column=0)

five_button = Button(width=4, height=1, text="5", font=("arial", 20, "bold"), bg=black, fg=white)
five_button.grid(row=2, column=1)

six_button = Button(width=4, height=1, text="6", font=("arial", 20, "bold"), bg=black, fg=white)
six_button.grid(row=2, column=2)

multiply_button = Button(width=4, height=1, text="*", font=("arial", 20, "bold"), bg=black, fg=white)
multiply_button.grid(row=2, column=3)

one_button = Button(width=4, height=1, text="1", font=("arial", 20, "bold"), bg=black, fg=white)
one_button.grid(row=3, column=0)

two_button = Button(width=4, height=1, text="2", font=("arial", 20, "bold"), bg=black, fg=white)
two_button.grid(row=3, column=1)

three_button = Button(width=4, height=1, text="3", font=("arial", 20, "bold"), bg=black, fg=white)
three_button.grid(row=3, column=2)

minus_button = Button(width=4, height=1, text="-", font=("arial", 20, "bold"), bg=black, fg=white)
minus_button.grid(row=3, column=3)

zero_button = Button(width=4, height=1, text="0", font=("arial", 20, "bold"), bg=black, fg=white)
zero_button.grid(row=4, column=0)

clear_button = Button(width=4, height=1, text="AC", font=("arial", 20, "bold"), bg=black, fg=white, command=AC)
clear_button.grid(row=4, column=1)

equals_button = Button(width=4, height=1, text="=", font=("arial", 20, "bold"), bg=black, fg=white)
equals_button.grid(row=4, column=2)

add_button = Button(width=4, height=1, text="+", font=("arial", 20, "bold"), bg=black, fg=white)
add_button.grid(row=4, column=3)


# screen_canvas = Canvas(width=320, height=65, bg=screen2_bg, highlightthickness=0)
# screen_canvas.pack()

def AC():
    screen_canvas.create_text(text="0")


window.mainloop()

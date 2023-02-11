from tkinter import *

# Application Constants:
HEIGHT = 410
WIDTH = 310
window_bg = "#D8D9CF"
screen_bg = "#EDEDED"
black = "#000000"
white = "#FFFFFF"
x_position = 280
x_change = 0
y_position = 50
number = ""
operator = ""
# Setting up window and icon:
window = Tk()
window.title("Calculator")
icon = PhotoImage(file="icon.png")
window.iconphoto(False, icon)
window.config(padx=10, pady=10, bg=window_bg)


def addition(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


#       operation = calci[operator]
#       print(f"\n{n1} {operator} {n2} = {operation}")
#       n1 = operation
#       if input(("\nPress enter to perform calculations with the same number or press N to start a new calculator.").lower()) == "n":
#         more_operations = False
#         calculations()
#
# calculations()


# Button functionality:
def AC():
    # screen_canvas.create_text(280,50, text="0", font=("arial", 30, "bold"))
    global number, x_position, x_change
    screen_canvas.delete("all")
    number = ""
    x_position = 280
    x_change = 0
    switch("0")


def switch(num):
    global number, x_position, x_change, operator
    if num in ["+", "-", "*", "/"]:
        operator = num
    x_position -= x_change
    x_change = 10
    number = number + num
    # if len(number) > 12
    screen_canvas.delete("all")
    screen_canvas.create_text(x_position, y_position, text=number, font=("arial", 30, "bold"))


def calculations():
    global number, x_position, x_change
    num = number.split(operator)
    print(num)
    n1 = int(num[0])
    n2 = int(num[-1])

    calci = {
        "+": addition(n1, n2),
        "-": subtract(n1, n2),
        "*": multiplication(n1, n2),
        "/": division(n1, n2),
    }
    operation = calci[operator]
    print(operation)
    screen_canvas.delete("all")
    screen_canvas.create_text(x_position, y_position, text=operation, font=("arial", 30, "bold"))



def seven():
    switch("7")


def eight():
    switch("8")


def nine():
    switch("9")


def divide():
    switch("/")


def four():
    switch("4")


def five():
    switch("5")


def six():
    switch("6")


def multiply():
    switch("*")


def one():
    switch("1")


def two():
    switch("2")


def three():
    switch("3")


def minus():
    switch("-")


def zero():
    switch("0")


def equals():
    pass


def add():
    switch("+")


# Screen canvas:
screen_canvas = Canvas(width=310, height=70, bg=screen_bg)
display_number = screen_canvas.create_text(280, 50, text="", font=("arial", 30, "bold"))
screen_canvas.grid(row=0, column=0, columnspan=4, pady=10)

seven_button = Button(width=4, height=1, text="7", font=("arial", 20, "bold"), bg=black, fg=white, command=seven)
seven_button.grid(row=1, column=0)

eight_button = Button(width=4, height=1, text="8", font=("arial", 20, "bold"), bg=black, fg=white, command=eight)
eight_button.grid(row=1, column=1)

nine_button = Button(width=4, height=1, text="9", font=("arial", 20, "bold"), bg=black, fg=white, command=nine)
nine_button.grid(row=1, column=2)

divide_button = Button(width=4, height=1, text="/", font=("arial", 20, "bold"), bg=black, fg=white, command=divide)
divide_button.grid(row=1, column=3)

# 456* 123- 0C=+
four_button = Button(width=4, height=1, text="4", font=("arial", 20, "bold"), bg=black, fg=white, command=four)
four_button.grid(row=2, column=0)

five_button = Button(width=4, height=1, text="5", font=("arial", 20, "bold"), bg=black, fg=white, command=five)
five_button.grid(row=2, column=1)

six_button = Button(width=4, height=1, text="6", font=("arial", 20, "bold"), bg=black, fg=white, command=six)
six_button.grid(row=2, column=2)

multiply_button = Button(width=4, height=1, text="*", font=("arial", 20, "bold"), bg=black, fg=white, command=multiply)
multiply_button.grid(row=2, column=3)

one_button = Button(width=4, height=1, text="1", font=("arial", 20, "bold"), bg=black, fg=white, command=one)
one_button.grid(row=3, column=0)

two_button = Button(width=4, height=1, text="2", font=("arial", 20, "bold"), bg=black, fg=white, command=two)
two_button.grid(row=3, column=1)

three_button = Button(width=4, height=1, text="3", font=("arial", 20, "bold"), bg=black, fg=white, command=three)
three_button.grid(row=3, column=2)

minus_button = Button(width=4, height=1, text="-", font=("arial", 20, "bold"), bg=black, fg=white, command=minus)
minus_button.grid(row=3, column=3)

zero_button = Button(width=4, height=1, text="0", font=("arial", 20, "bold"), bg=black, fg=white, command=zero)
zero_button.grid(row=4, column=0)

clear_button = Button(width=4, height=1, text="AC", font=("arial", 20, "bold"), bg=black, fg=white, command=AC)
clear_button.grid(row=4, column=1)

equals_button = Button(width=4, height=1, text="=", font=("arial", 20, "bold"), bg=black, fg=white,
                       command=calculations)
equals_button.grid(row=4, column=2)

add_button = Button(width=4, height=1, text="+", font=("arial", 20, "bold"), bg=black, fg=white, command=add)
add_button.grid(row=4, column=3)

# screen_canvas = Canvas(width=320, height=65, bg=screen2_bg, highlightthickness=0)
# screen_canvas.pack()


window.mainloop()

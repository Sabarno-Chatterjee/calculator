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


import pygame
import random

# Application Constants:
HEIGHT = 400
WIDTH = 300
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
display_x = 10
display_y = 10
KEY_HEIGHT = 67
KEY_WIDTH = 62
fps = 60
keys = [7, 8, 9, '/', 4, 5, 6, '*', 1, 2, 3, '-', 0, '.', '=', '+']

pygame.init()

# Design the screen.
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Calculator")
background = BLACK
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()
# Design of display area:


running = True

while running:
    timer.tick(fps)
    screen.fill(background)
    # Display area:
    display = pygame.draw.rect(screen, WHITE, [display_x, display_y, 280, 60])
    key_x = 10
    key_y = 80
    i = 1
    for key in range(4):
        generate_key = pygame.draw.rect(screen, WHITE, [key_x, key_y, KEY_WIDTH, KEY_HEIGHT])
        key_x += 72

    # key_x += 10
    # key_y = 200
    # for key in range(4):
    #     generate_key = pygame.draw.rect(screen, WHITE, [key_x, key_y, KEY_WIDTH, KEY_HEIGHT])
    #     key_x += 72

    # Design the keys and display area:
    #

    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False


    pygame.display.flip()

pygame.quit()


# Design functions.
# Add functionality to keys.

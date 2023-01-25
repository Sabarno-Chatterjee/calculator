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
font = pygame.font.Font('freesansbold.ttf', 40)
timer = pygame.time.Clock()
# Design of display area:


running = True

while running:
    timer.tick(fps)
    screen.fill(background)
    # Display area:
    display = pygame.draw.rect(screen, WHITE, [display_x, display_y, 280, 60])

    # Keys display:
    seven = pygame.draw.rect(screen, WHITE, [10, 90, KEY_WIDTH, KEY_HEIGHT])
    seven_text = font.render("7", True, BLACK, WHITE)
    screen.blit(seven_text, (30,105))
    eight = pygame.draw.rect(screen, WHITE, [82, 90, KEY_WIDTH, KEY_HEIGHT])
    eight_text = font.render("8", True, BLACK, WHITE)
    screen.blit(eight_text, (102, 105))
    nine = pygame.draw.rect(screen, WHITE, [154, 90, KEY_WIDTH, KEY_HEIGHT])
    nine_text = font.render("9", True, BLACK, WHITE)
    screen.blit(nine_text, (174, 105))
    divide = pygame.draw.rect(screen, WHITE, [226, 90, KEY_WIDTH, KEY_HEIGHT])
    divide_text = font.render("/", True, BLACK, WHITE)
    screen.blit(divide_text, (246, 105))
    four = pygame.draw.rect(screen, WHITE, [10, 167, KEY_WIDTH, KEY_HEIGHT])
    four_text = font.render("4", True, BLACK, WHITE)
    screen.blit(four_text, (30, 183))
    five = pygame.draw.rect(screen, WHITE, [82, 167, KEY_WIDTH, KEY_HEIGHT])
    five_text = font.render("5", True, BLACK, WHITE)
    screen.blit(five_text, (102, 183))
    six = pygame.draw.rect(screen, WHITE, [154, 167, KEY_WIDTH, KEY_HEIGHT])
    six_text = font.render("6", True, BLACK, WHITE)
    screen.blit(six_text, (174, 183))
    multiply = pygame.draw.rect(screen, WHITE, [226, 167, KEY_WIDTH, KEY_HEIGHT])
    multiply_text = font.render("*", True, BLACK, WHITE)
    screen.blit(multiply_text, (246, 187))
    one = pygame.draw.rect(screen, WHITE, [10, 244, KEY_WIDTH, KEY_HEIGHT])
    one_text = font.render("1", True, BLACK, WHITE)
    screen.blit(one_text, (30, 260))
    two = pygame.draw.rect(screen, WHITE, [82, 244, KEY_WIDTH, KEY_HEIGHT])
    two_text = font.render("2", True, BLACK, WHITE)
    screen.blit(two_text, (102, 260))
    three = pygame.draw.rect(screen, WHITE, [154, 244, KEY_WIDTH, KEY_HEIGHT])
    three_text = font.render("3", True, BLACK, WHITE)
    screen.blit(three_text, (174, 260))
    minus = pygame.draw.rect(screen, WHITE, [226, 244, KEY_WIDTH, KEY_HEIGHT])
    minus_text = font.render("-", True, BLACK, WHITE)
    screen.blit(minus_text, (250, 255))
    zero = pygame.draw.rect(screen, WHITE, [10, 321, KEY_WIDTH, KEY_HEIGHT])
    zero_text = font.render("0", True, BLACK, WHITE)
    screen.blit(zero_text, (30, 340))
    period = pygame.draw.rect(screen, WHITE, [82, 321, KEY_WIDTH, KEY_HEIGHT])
    period_text = font.render(".", True, BLACK, WHITE)
    screen.blit(period_text, (107, 330))
    equals = pygame.draw.rect(screen, WHITE, [154, 321, KEY_WIDTH, KEY_HEIGHT])
    equals_text = font.render("=", True, BLACK, WHITE)
    screen.blit(equals_text, (174, 335))
    add = pygame.draw.rect(screen, WHITE, [226, 321, KEY_WIDTH, KEY_HEIGHT])
    add_text = font.render("+", True, BLACK, WHITE)
    screen.blit(add_text, (246, 335))






    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False


    pygame.display.flip()

pygame.quit()


# Design functions.
# Add functionality to keys.

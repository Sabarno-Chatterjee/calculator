import art
print(art.logo)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 -  n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1/n2


def calculations():
  n1 = float(input("\nWhats the first number?\n"))
  
  more_operations = True
  
  while more_operations:
      operator = input("\nWhats the operator? ('+', '-', '*', '/')\n")
      n2 = float(input("\nWhats the next number?\n"))
      
      calci = {
        "+" :  add(n1,n2),
        "-" :  subtract(n1, n2),
        "*" :  multiply(n1, n2),
        "/" :   divide(n1, n2),
        }
      
      operation = calci[operator]
      print(f"\n{n1} {operator} {n2} = {operation}")
      n1 = operation
      if input(("\nPress enter to perform calculations with the same number or press N to start a new calculator.").lower()) == "n":
        more_operations = False
        calculations()

calculations()
      
  

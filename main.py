import art 
print (art.logo)

def add (n1, n2): 
  return n1 + n2 
def subtract (n1, n2): 
  return n1 - n2 
def multiply (n1, n2): 
  return n1 * n2 
def divide (n1, n2): 
  return n1 / n2 

operations = {
  "+": add, 
  "-": subtract, 
  "*":multiply, 
  "/":divide 
} 

def calculator():
  userYes = True
  num1 = input("What is the first number?")
  num1 = float (num1)
  
  while (userYes == True):
    for op in operations: 
      print (op)
    operation_symbol = input("Pick an operation from the line above:")
    num2 = input ("What is the next number?")
    num2 = float (num2)
    if operation_symbol == "+": 
      answer = add(num1, num2)
    elif operation_symbol == "-": 
      answer =subtract(num1, num2)
    elif operation_symbol == "*": 
      answer =multiply(num1, num2)
    elif operation_symbol == "/": 
      answer = divide(num1, num2)
    else: 
      print ("Incorrect symbol chose, start again")
    
    
    print (f"{num1} {operation_symbol} {num2} = {answer}")
  
    user_cont = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")
    user_cont = user_cont.lower()
    if user_cont == "y":
      num1 = answer 
    elif user_cont == "n": 
      userYes = False 
      calculator()

calculator()
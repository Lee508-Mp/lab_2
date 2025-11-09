# Global variables
history = []
operations_count = 0
memory = 0

# Part 1: Implement Basic Arithmetic Functions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        print("Error: Division by zero")
        return "Error: Division by zero"
    return num1 / num2

def modulus(num1, num2):
    if num2 == 0:
        print("Error: Modulus by zero")
        return "Error: Modulus by zero"
    return num1 % num2

# Part 2: Implement Input Handling
def get_number_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a number.")
#part 3: implement history tracking 
def update_history(num1, operation, num2,result):
    

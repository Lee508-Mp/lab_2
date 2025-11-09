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
        print("Error: unified ")
        return "Error: unified "
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
    history.append(f"{num1} {operation} {num2} = {result}")
    global operations_count
    operations_count += 1

def display_history():
    if not history:
        print("History is empty.")
    else:
        for entry in history:
            print(entry)

# Part 4: Test Your Calculator
def test_calculator():
    # Test operations
    print("Testing operations...")
    print(add(2, 3))
    print(subtract(5, 2))
    print(multiply(4, 5))
    print(divide(10, 2))
    print(modulus(10, 3))

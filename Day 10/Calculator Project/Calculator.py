import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    result = 0
    choice = ""
    should_accumulate = True
    first_number = int(input("Enter the first number: "))
    for operator in operations:
        print(f"{operator}")
    while should_accumulate:
        operator = input("Enter the operator: ")
        second_number = int(input("Enter the second number: "))
        if operator in operations:
            result = operations[operator](first_number, second_number)
            print(f"{first_number} {operator} {second_number} = {result}")
        choice =  input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation : ")
        if choice == "y":
            first_number = result
        else:
            should_accumulate = False
            print("\n" * 20)
            print(art.logo)
            calculator()

calculator()
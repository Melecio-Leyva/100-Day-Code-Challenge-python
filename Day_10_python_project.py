#Logo for starting UI
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
#Add first number and second number
def add(number1,number2):
    return number1 + number2
#subtract second number from first number
def subtract(number1,number2):
    return number1 - number2
#Divide first number by second number
def divide(number1,number2):
    return number1 / number2
#multiply first number by second number
def multiply(number1,number2):
    return number1 * number2

operations = {"+": add, "-": subtract, "*": multiply,"/": divide,}
def calculator():
    print(logo)
    number_one = float(input("What is your first number?: "))

    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:

        operations_symbols = input("Pick an operationa.")

        number_two = float(input("What's the next number?: "))
        calculation_function = operations[operations_symbols]
        answer = calculation_function(number_one, number_two)

        print(f"{number_one} {operations_symbols} {number_two} = {answer}")
        
        if input(f"Type 'y' if you want to continue with {answer}, or type 'n' to start a new calculation") == 'y':
            number_one = answer
        else:
            should_continue = False
            calculator()
calculator()
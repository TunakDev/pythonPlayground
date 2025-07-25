import warnings


class Bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        # Warnings won't stop the program like a "raise" would do but still print a red message in the log
        warnings.warn("Dividing a number by zero does not lead to a result")
    else:
        return x / y


# Extract method for user input
def get_nums():
    x = float(input('Enter 1st number: '))
    y = float(input('Enter 2nd number: '))
    return x, y


# Let the calculator ask for another input after calculation
while True:
    print("-------------------------------")
    print("Select an operation to perform:")
    print("'1': ADD")
    print("'2': SUBTRACT")
    print("'3': MULTIPLY")
    print("'4': DIVIDE")
    print("'exit': exit the calculator")
    print("-------------------------------")

    operation = input()
    # Let the calculator be stoppable by user input
    if operation == 'exit':
        break
    numbers = get_nums()

    if operation == '1':
        print(f'The result of the addition of {numbers[0]} and {numbers[1]} is')
        print(f'{Bcolors.OKGREEN} {addition(numbers[0], numbers[1])}{Bcolors.ENDC}')
    elif operation == '2':
        print(f'The result of the subtraction of {numbers[0]} and {numbers[1]} is')
        print(f'{Bcolors.OKGREEN} {subtraction(numbers[0], numbers[1])} {Bcolors.ENDC}')
    elif operation == '3':
        print(f'The result of the multiplication of {numbers[0]} and {numbers[1]} is')
        print(f'{Bcolors.OKGREEN} {multiplication(numbers[0], numbers[1])}{Bcolors.ENDC}')
    elif operation == '4':
        print(f'The result of the division of {numbers[0]} and {numbers[1]} is')
        print(f'{Bcolors.OKGREEN} {division(numbers[0], numbers[1])}{Bcolors.ENDC}')
    else:
        print("Invalid entry!")

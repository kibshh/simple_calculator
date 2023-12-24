def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def get_float_input(prompt):
    while True:
        try:
            float_value = float(input(prompt))
            break
        except ValueError:
            print("Please enter a valid number.")
    return float_value


def get_operation():
    op_input = ''
    while op_input not in ['+', '-', '*', '/']:
        op_input = input("Pick an operation ( + , - , * , / ): ")
    return op_input


calc_functions = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
continue_or_new = 'n'
first_num = 0

print('WELCOME TO THE CALCULATOR PROGRAM!\n')

while True:
    if continue_or_new == 'n':
        first_num = get_float_input(prompt="What's the first number? ")
    elif continue_or_new == 'q':
        print("\nThank you for using our calculator!\n")
        break
    operation = get_operation()
    second_num = get_float_input(prompt="What's the next number? ")
    if operation == '/' and second_num == 0:
        print("Result undefined, divide by zero forbidden.")
    else:
        first_num = calc_functions[operation](first_num, second_num)
        print(f"RESULT: {first_num}")
    continue_or_new = input(f"'c' to continue calculating with {first_num}\n'n' for new calculation\n'q' for quit\nTYPE HERE:  ").lower()

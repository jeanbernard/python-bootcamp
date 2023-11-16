import calculator_art

print(calculator_art.logo)

# Add
def add(n1, n2):
    return n1 + n2
# Sub
def sub(n1, n2):
    return n1 - n2
# Multi
def mult(n1, n2):
    return n1 * n2
# Div
def div(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

def choose_operation():
    print("list of operators: ")
    for op in operations:
        print(op)
    return input("chose operator: ")

def calculate(num1, num2, chosen_op):
    calc_func = operations[chosen_op]
    answer = calc_func(num1, num2)
    print(f"{num1} {chosen_op} {num2} = {answer}")
    return answer

def ask_for_num(digit):
    return float(input(f"{digit} number?: "))

num1 = ask_for_num("1st")
chosen_op = choose_operation()
num2 = ask_for_num("2nd")
answer = calculate(num1, num2, chosen_op)

continue_calc = True
while continue_calc:
    keep_calc = input("would you like compute a follow up number? 'yes' or 'no' or 'restart' ").lower()
    if keep_calc == "yes":
        chosen_op = choose_operation()
        num2 = ask_for_num("follow up")
        answer = calculate(answer, num2, chosen_op)
    elif keep_calc == "restart":
        num1 = ask_for_num("1st")
        chosen_op = choose_operation()
        num2 = ask_for_num("2nd")
        answer = calculate(num1, num2, chosen_op)
    else:
        print(f"final answer: {answer}")
        continue_calc = False
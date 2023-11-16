def multiply(num1, num2):
    return num1 * num2

def format_name(f_name, l_name):
    """Take a 1st and last name and format it"""
    f1 = f_name.title()
    f2 = l_name.title()
    return f"{f1} {f2}"

rslt = multiply(2, 2)
print(rslt)
print(format_name("jeAn", "bErnArd"))

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    print("This Will not be Printed") #


print(format_name(input("What is your first name?: "), input("What is your last name?: ")))


def add(n1 , n2):
    return n1 + n2

my_favorite_number = add 
"""
my_favorite_number is now a reference to the
add function and not trying to call it 
because there are no parentheses
"""
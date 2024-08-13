def format_name(f_name, l_name):
    return f"{f_name.capitalize()} {l_name.capitalize()}"

formatted_name = format_name("LiRoNe", "FiToUsSi")
# print(formatted_name)



# .capitalize():

# .title():

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("Hello"))
print(output)
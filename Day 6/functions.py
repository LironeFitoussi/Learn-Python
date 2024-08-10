print("Hello World!")
num_char = len("Hellow")
print(num_char)

def name():
    """
    Purpose: 
    """
    
# end def

def my_function(name ):
    print(f"My name is: {name}")

# my_function("Lirone")

def calc_bmi(height, weight):
    bmi = round((weight / (height ** 2)), 2)
    
    print(bmi)
    if bmi < 18.5:
        print("uderweight")
    elif 18.5 <= bmi < 25:
        print("You BMI is ok")
    else:
        print("overweight")
    
calc_bmi(1.76, 80)

for i in range (6):
    print(i)
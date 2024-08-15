try: 
    age = int(input("Enter your age: "))
except ValueError:
    print("You have typed in an invalid number. Please try again with a numerical response such as 15.")
    age = int(input("Enter your age: "))
    
if age > 18:
    print(f"You can drive at age {age}.")

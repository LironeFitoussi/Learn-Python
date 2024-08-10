#Data Types

# Strings:
print("Hello"[0])

print("123" + "456")

# Integer: 
print(123 + 456)

print(123_456_789)
print(123456789)

# Float:
print(3.1564)

# Boolean: 
True;

False;

street_name = "Abbey Road"
print(street_name[4] + street_name[7])

# Data Type:
type(3)
type("Hello")

# Convert Data Type:
# str(45) //"45" 
# int("45") // 45
# int("45.5") // 45
# float("45.5") // 45.5

# num_char = len(input("What is your name?\n"));
# print("Your name has " + str(num_char) + " characters")

# print(type(num_char))

a = 123
print(type(a))
a = str(a)
print(type(a))
print(a)

print(70 + float("100.5"))
print(str(70) + str(100))


# to_digit_number = input()
two_digit_number = "45"
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
print(first_digit + second_digit);
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# Math
3 + 5  //8
7 - 4  //3
3 * 2  //6
6 / 3  //2.0
2 ** 2  //4
2 ** 3  //8

# PEMDAS
# ()
# **
# * /
# + -

print(3 * 3 + 3 / 3 - 3)





print(round(2.6666666, 2))
print(8 // 3)

score = 0
# User scores a point
score += 1
print(score)

# User lose a point
score -= 1
print(score)

# f-string
score = 42
height = 1.75
isWinning = True
print(f"your score {score}, your height is {height}, you are winning {isWinning}")

# #! File Not Found Error
# # with open('a_file.txt') as file:
# #     file.read()

# #? With try and except
# try:
#     file = open('a_file.txt')
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['key']) # This will raise a key error but beacuse of try and except it will not stop the program
# # except: # Not recommended to use except without specifying the error
# except FileNotFoundError:
#     # print('File not found') // This is a general error message
#     file = open('a_file.txt', 'w') # This will create a file if it doesn't exist
#     file.write('Something') 
# except KeyError as error_message:
#     print(f'That key {error_message} does not exist')
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print('File was closed')
#     raise KeyError('This is an error that I made up') # This will raise an error
    
# #! Key Error
# # a_dictionary = {'key': 'value'}
# # value = a_dictionary['non_existent_key']

# #! Index Error
# # fruit_list = ['Apple', 'Banana', 'Pear']
# # fruit = fruit_list[3]

# #! Type Error
# # text = "abc"
# # print(text + 5)


height = float(input("Height: "))
if height > 3:
    raise ValueError("Human height should not be over 3 meters")

weight = int(input("Weight: "))
if weight > 250:
    raise ValueError("Human weight should not be over 250 pounds")


bmi = weight / height ** 2
print(bmi)
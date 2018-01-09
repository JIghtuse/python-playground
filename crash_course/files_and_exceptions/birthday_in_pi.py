import os

data_file_path = os.path.join('data', 'pi_million_digits.txt')

pi_string = ''
with open(data_file_path) as file_object:
    for line in file_object:
        pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


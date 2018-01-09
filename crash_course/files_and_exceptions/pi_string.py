import os

data_file_path = os.path.join('data', 'pi_million_digits.txt')

pi_string = ''
with open(data_file_path) as file_object:
    for line in file_object:
        pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

import os

data_file_path = os.path.join('data', 'learning_python.txt')

with open(data_file_path) as file_object:
    for line in file_object:
        print(line.replace('Python', 'C').rstrip())


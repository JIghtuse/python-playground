import os

data_file_path = os.path.join('data', 'pi_digits.txt')

print(f"Reading entire file {data_file_path}")
with open(data_file_path) as file_object:
    contents = file_object.read()
    print(contents)

print(f"\nReading file {data_file_path} line by line")
with open(data_file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

print(f"\nReading list of lines from {data_file_path} file")
with open(data_file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

name = input("Please enter your name: ")

with open('guest.txt', 'w') as output_file:
    output_file.write(name)
    output_file.write('\n')

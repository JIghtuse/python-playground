age = 12

if age < 4:
    admission = 0
elif age < 18:
    admission = 5
elif age < 65:
    admission = 10
else:
    admission = 1

print(f"Your admission cost is ${admission}.")
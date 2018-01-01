guests = ['Dan Simmons', 'Stephen King', 'Robert Sheckley']
print(f"Dear {guests[0]}, please join our dinner today.")
print(f"Dear {guests[1]}, please join our dinner today.")
print(f"Dear {guests[2]}, please join our dinner today.")

cant_make_the_dinner = 'Robert Sheckley'
new_guest = 'Neal Stephenson'
print(f"\n{cant_make_the_dinner} will not join us, unfortunately.")
guests.remove(cant_make_the_dinner)
guests.append(new_guest)
print(f"Dear {guests[0]}, please join our dinner today.")
print(f"Dear {guests[1]}, please join our dinner today.")
print(f"Dear {guests[2]}, please join our dinner today.")

print("\nDear guests, we found a bigger dinner table!")
guests.insert(0, 'George Martin')
guests.insert(3, 'Neil Gaiman')
guests.append('William Gibson')
print(f"Dear {guests[0]}, please join our dinner today.")
print(f"Dear {guests[1]}, please join our dinner today.")
print(f"Dear {guests[2]}, please join our dinner today.")
print(f"Dear {guests[3]}, please join our dinner today.")
print(f"Dear {guests[4]}, please join our dinner today.")
print(f"Dear {guests[5]}, please join our dinner today.")
print(f"We are inviting {len(guests)} people to dinner.")

print("\nDear guests, our table won't arrive in time for the dinner. We can only invite two people.")
guest = guests.pop()
print(f"Dear {guest}, sorry, but we can't invite you to dinner.")
guest = guests.pop()
print(f"Dear {guest}, sorry, but we can't invite you to dinner.")
guest = guests.pop()
print(f"Dear {guest}, sorry, but we can't invite you to dinner.")
guest = guests.pop()
print(f"Dear {guest}, sorry, but we can't invite you to dinner.")
print(f"Dear {guests[0]}, please join our dinner today.")
print(f"Dear {guests[1]}, please join our dinner today.")

del guests[1]
del guests[0]
print(guests)

# nesting example: list of dictionaries

aliens = [
    {'color': 'green', 'points': 5},
    {'color': 'yellow', 'points': 10},
    {'color': 'red', 'points': 15},
]

for alien in aliens:
    print(alien)


# Generating aliens
aliens = []
for alien_number in range(30):
    aliens.append({'color': 'green', 'points': 5, 'speed': 'slow'})

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")
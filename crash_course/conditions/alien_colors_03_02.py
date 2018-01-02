alien_color = 'yellow'

if alien_color == 'green':
    points_earned = 5
elif alien_color == 'yellow':
    points_earned = 10
elif alien_color == 'red':
    points_earned = 15
else:
    points_earned = None

print(f"You earned {points_earned} points!")

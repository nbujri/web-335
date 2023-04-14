"""
  title: bujri_hobbies.py
  author: ngi bujri
  date: april 14 2023
  description: exercise 5.3 - conditionals, lists, loops
"""

hobbies = ['soccer', 'gaming', 'cooking', 'drawing', 'reading']

# print each item to console
for hobby in hobbies:
    print(hobby)

days = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
    ]

for day in days:
    # if weekend, print a message indicating a day off
    # else print it is a work day
    if day == 'Sunday' or day == 'Saturday':
        print(f'It is {day}, your day off. Enjoy your hobbies.')
    else:
        print(f'It is {day}, a work day.')
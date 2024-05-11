date = input('Enter todays date: ')
mood = input('How do you rate your mood today from 1 to 10? ')
thoughts = input('Let you thoughts flow: \n')

with open(f'../journal/{date}.txt', 'w') as file:
    file.write(mood + '\n\n')
    file.write(thoughts)

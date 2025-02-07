import sys
import random

if len(sys.argv) < 2:
    print('Usage: python game.py <your_guess>')
    sys.exit(1)

try:
    user_guess = int(sys.argv[1])
except ValueError:
    print('Please enter a valid number between 1 and 10')
    sys.exit(1)

if not (1 <= user_guess <= 10):
    print('Please enter a valid number between 1 and 10')
    sys.exit(1)

random_number = random.randint(1, 10)
print(f'Your guess is: {user_guess}, random number is: {random_number}')

if  user_guess == random_number:
    print('🎉 You guessed right!')
else:
    print('❌ Try again!')

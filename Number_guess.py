import random
number = random.randint(1, 10)

player_name = input('Hello, Player Enter Your name:')
number_of_guesses = 0
print('*'*50)
print('\tYou Have Only Three Chance')
print('\tGuess the Number between(1 to 10)')
print('\tLets Play The Game')
print('*'*50)

while number_of_guesses < 3:
    guess = int(input('enter the number:'))
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low, go up a little.')
    if guess > number:
        print('Your guess is too high, go down a bit.')
    if guess == number:
        break
if guess == number:
    print( 'Congratulations {}, you guessed the number in {} tries.'.format(player_name, number_of_guesses))
else:
    print('\nGame Over \nthe number is={}.'.format(number))

import random

number = random.randint(1,100)

player_name = input("Hello, What's your name?")


print('okay! ' + player_name + ' I am Guessing a number between 1 and 100:')

guess = int(input())
number_of_guesses = 1


while number != guess:

    if(number_of_guesses != 1):
       print('Enter your guessed number')
       guess = int(input())
     
    
    number_of_guesses += 1

    if guess < number:
        print('Your guess is too low.')

    elif guess > number:
        print('Your guess is too high.')

    else:
        break

if guess == number:
        print('Congratulations, ' + player_name + '!You guesses the number in ' + str(number_of_guesses) + ' tries!')
else:
        print('Sorry, ' + player_name + ', you did not guess the number. The number was ' + str(number))



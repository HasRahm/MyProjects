import random
secret_value = random.randint(1,100)
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    guess = int(input('Enter the value: '))
    guess_count += 1
    if guess == secret_value:
        print('You won!')
        break
    elif guess < secret_value:
        print('Too low!')
    elif guess > secret_value:
        print('Too high!')
else:
     print('Sorry better luck next time.')
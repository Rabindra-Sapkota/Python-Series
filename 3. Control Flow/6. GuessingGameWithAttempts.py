# Move file. Send Mail and so on
import random

total_attempt = 6
random_number = random.randint(1, 100)

print(random_number)
while total_attempt > 0:
    print()
    user_input = input('Guess Any Number between 1 and 100: ')
    user_input_int = int(user_input)
    if user_input_int == random_number:
        print('\n' + '-'*200)
        print('Congratulation!! You won. Your point is:', total_attempt * 10)
        break

    total_attempt = total_attempt - 1

    if total_attempt == 0:
        print(f'You lost. The number was {random_number}')
    elif random_number > user_input_int:
        print(f'Wrong!. Please guess bigger number. You have {total_attempt} attempts left')
    else:
        print(f'Wrong!. Please guess smaller number. You have {total_attempt} attempts left')
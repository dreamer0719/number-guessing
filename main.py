import random

valid_level = {'1':'easy',
               '2':'medium',
               '3':'hard'}
attempts_limit = {'1':10, '2':5,'3':3}

def main():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.\n")
    print('Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n')
    while True:
        user_level = input('Enter your choice (1,2,3): ').strip()
        if user_level in valid_level:
            break
        else:
            print('Please type in a valid level\n')
    print(f"\nGreat! You have selected the {valid_level[user_level]} difficullty level.\nLet's start the game!\n")
    guessing(user_level)
    
      
def guessing(user_level):
    answer =  random.randint(1,100)
    amount_used = 0
    max_attempts = attempts_limit[user_level]
    while amount_used < max_attempts:
        try:
            user_try = int(input('Type in your guess: '))
            if user_try > 100 or user_try < 1:
                print('Be sneaker :)\n')
                continue
        except ValueError:
            print('Please type in a number\n')
            continue   
        if user_try > answer:
            print('Too large!\n') 
            amount_used += 1
        elif user_try < answer:
            print('Too small!\n')
            amount_used +=1
        else: 
            print(f'Just right! The answer is {answer}\n')
            break
    if amount_used == max_attempts:
        print(f"Game over\nThe correct answer is {answer}\n")
    
main()

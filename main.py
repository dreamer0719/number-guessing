import random

valid_level = {'1':'easy',
               '2':'medium',
               '3':'hard'}

def main():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.")
    print()
    print('Please selecte the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)')
    print()
    while True:
        user_level = input('Enter your choice (1,2,3): ')
        if user_level not in valid_level:
            print('Please type in a valid level')
            ... # Reprompt the user
        elif user_level in valid_level:
            break
    print()
    print(f"Great! You have selected the {valid_level[user_level]} difficullty level.\nLet's start the game!")
    guessing(user_level)
    return user_level
    
def guessing(user_level):
    answer =  random.randint(1,100)
    amount_try = 0
    
    if user_level == '1':
        while True:
            if amount_try < 10:
                try:
                    user_try = int(input('Type in your guess: '))
                    if user_try > 100:
                        print('Be sneaker')
                except ValueError:
                    print('Please type in a number')
                    ... #Reprompt the user
                    
                if user_try > answer:
                    print('Too large!') 
                    amount_try += 1
                elif user_try < answer:
                    print('Too small!')
                    amount_try +=1
                else: 
                    print(f'Just right! The answer is {answer}')
                    break
            elif amount_try == 10:
                print(f"Game over\nThe correct answer is {answer}")
                break
    
    elif user_level == '2':
        while True:
            if amount_try < 5:
                try:
                    user_try = int(input('Type in your guess: '))
                    if user_try > 100:
                        print('Be sneaker')
                except ValueError:
                    print('Please type in a number')
                    ... #Reprompt the user
                    
                if user_try > answer:
                    print('Too large!') 
                    amount_try += 1
                elif user_try < answer:
                    print('Too small!')
                    amount_try +=1
                else: 
                    print(f'Just right! The answer is {answer}')
                    break
            elif amount_try == 5:
                print(f"Game over\nThe correct answer is {answer}")
                break
            
    else:
        while True:
            if amount_try < 3:
                try:
                    user_try = int(input('Type in your guess: '))
                    if user_try > 100:
                        print('Be sneaker :)')
                except ValueError:
                    print('Please type in a number')
                    ... #Reprompt the user
                    
                if user_try > answer :
                    print('Too large!') 
                    amount_try += 1
                elif user_try < answer:
                    print('Too small!')
                    amount_try +=1
                else: 
                    print(f'Just right! The answer is {answer}')
                    break
            elif amount_try == 3:
                print(f"Game over\nThe correct answer is {answer}")
                break
    
main()

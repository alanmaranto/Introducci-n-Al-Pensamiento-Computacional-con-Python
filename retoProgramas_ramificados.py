name1 = input('What is the name of player 1: ')
age1 = input('What is your age of player 1: ')
name2 = input('What is the name of player 2: ')
age2 = input('What is your age of player 2: ')

if age1 > age2:
    print(
        f'The age of {name1} is {age1} and is more old than {name2} with {age2}'
    )
elif age1 < age2:
    print(
        f'The age of {name1} is {age1} and is less old than {name2} with {age2}'
    )
else:
    print(
        f'{name1} and {name2} have the same age'
    )

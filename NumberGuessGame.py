import random

random_number = random.randint(0, 100)
no_of_chances = 3
print('''This is a number guessing game, you can choose any number between 0-100
if the number you chosen will match with the number chosen by the computer you will win.
You have 3 chance, Best of luck!''')
while no_of_chances > 0:
    user_input = int(input("Enter the number between 0-100: "))
    if user_input == random_number:
        print("Congratulations! you won")
    else:
        no_of_chances -= 1
        if no_of_chances == 0:
            break
        print("Sorry! try again")
print("Sorry! your chances are over")

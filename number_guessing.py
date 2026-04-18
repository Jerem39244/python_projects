import random

numbers = [20,38,59,72,13,67,92]

list.sort(numbers)

chosen_number = random.choice(numbers)
print("A number has been chosen")
print(f"This is the list that you can pick from {numbers}")

the_guess = int(input("Enter you guess:"))
if the_guess == chosen_number:
    print("You were correct")
else:
    print("You were not correct")
    print(f"The correct answer was {chosen_number}")




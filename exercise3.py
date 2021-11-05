import random

from_where = int(input("From 0 to what do you want to play =="))
stop = False
our_random_number = random.randint(0, from_where)
user_number = int(input("Enter your guess ="))
while stop == False:
    if user_number == our_random_number:
        print("Congrulations!")
        stop = True
    elif user_number < our_random_number :
        print("Please increas your number")
        user_number = int(input("Enter your guess again="))
    elif our_random_number < user_number:
        print("Please decrease your number")
        user_number = int(input("Enter your guess again="))
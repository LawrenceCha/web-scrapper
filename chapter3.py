# winner = 10

# if winner < 10:
#     print("Run!")

# elif winner == 10:
#     print("Run!Run!")

# else:
#     print("Stop!")

from random import randint

print("Welcome to Python Casino")
pc_choice = randint(1, 100)

playing = True

while playing:
    user_choice = int(input("Enter your guess (1 - 100): "))
    if user_choice == pc_choice:    
        print("You win!")
        playing = False
    elif user_choice < pc_choice:
        print("Too low!")
    elif user_choice > pc_choice:
        print("Too high!")
    


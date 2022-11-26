import random
rock = "🪨"
scissor = "✂️"
paper = "📄"
signs = [rock,scissor,paper]
user_data  = int(input("Enter 0 for rock OR 1 for scissor OR 2 for paper:\t"))
computer_data  = random.randint(0,2)
if user_data >= 3 or user_data < 0:
    print("User has given a wrong number!")
else:
    print(f"User has chosen:\t {signs[user_data]}")
    print(f"Computer has chosen:\t {signs[computer_data]}")
    if (user_data == 0 and computer_data == 0) or (user_data == 1 and computer_data == 1) or ((user_data == 2 and computer_data == 2)):
        print("Match is DRAW")
    elif user_data == 0 and computer_data == 1:
        print("You Win!")
    elif user_data == 0 and computer_data == 2:
        print("Computer Win!")
    elif user_data == 1 and computer_data == 0:
        print("Computer Win!")
    elif user_data == 1 and computer_data == 2:
        print("You Win!")
    elif user_data == 2 and computer_data == 0:
        print("You Win!")
    elif user_data == 2 and computer_data == 1:
        print("Computer Win!")
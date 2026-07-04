import random
choice_item=["Rock","Paper","Scissor"]
user_choice = input("Enter your move= Rock,Paper,Scissor")
com_choice = random.choice(choice_item)
print(f"User choice = {user_choice},Computer choice = {com_choice}")
if user_choice == com_choice:
    print("Both chose same :Match Tie")
elif user_choice == "Rock":
    if com_choice == "Paper":
        print("rock smashes scissor :You Win")
elif user_choice == "Paper":
    if com_choice == "Scissor":
        print("Scissor cuts the paper:Computer Win")
    else:
        print("paper covers rock:You Win")
elif user_choice == "Scissor":
    if com_choice == "Rock":
        print("Rock smashes the Scissor:Computer Win")
    else:
        print("Scissor cuts paper: You Win")
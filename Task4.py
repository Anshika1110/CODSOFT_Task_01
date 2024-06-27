import random

def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def rock_vs(choice):
    return choice == "scissors"

def paper_vs(choice):
    return choice == "rock"

def scissors_vs(choice):
    return choice == "paper"

def determine_winner(user_choice, computer_choice):
    win_conditions = {
        "rock": rock_vs,
        "paper": paper_vs,
        "scissors": scissors_vs
    }
    
    if user_choice == computer_choice:
        return "tie"
    elif win_conditions[user_choice](computer_choice):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

def main():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, winner)
        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()



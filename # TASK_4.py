import random
def game(player, pc):
    if (player == pc):
        return "The game is tie"
    elif (player == "rock" and pc == "scissors"):
        return "You win :)"
    elif (player == "scissors" and pc == "paper"):
        return "You win :)"
    elif (player == "paper" and pc == "rock"):
        return "You win :)"
    else:
        return "You lose!"
def main():
    playerscore = 0
    pcscore = 0
    while True:
        print("Welcome to Rock, Paper, and Scissors :)")
        player = input("Enter your choice: rock/paper/scissors/exit :  ")
        if (player == "exit"):
            print("Thanks for playing!")
            break
        elif player not in ["rock", "paper", "scissors"]:
            print("Enter valid choice")
            continue
        pc = random.choice(["rock", "paper", "scissors"])
        result = game(player, pc)
        print(result)
        if result == "You win :)":
            playerscore += 1
        elif result == "You lose!":
            pcscore += 1
        print(f"Scores: You - {playerscore}, Computer - {pcscore}")
if __name__ == "__main__":
    main()

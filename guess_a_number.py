import random
import webbrowser

character = input("Choose your level: [e]asy, [m]edium, [h]ard: ")

tries = 0
if character == "e" or character == "m" or character == "h":
    if character == "e":
        tries = random.randint(6, 15)
    elif character == "m":
        tries = random.randint(5, 12)
    elif character == "h":
        tries = random.randint(3, 9)

    computer_number = random.randint(1, 100)
    guesses = 0
    correct = 0

    while True:
        player_input = input("Guess the number (1, 100): ")
        if not player_input.isdigit():
            print("Invalid input. Try again...")
            continue
        player_number = int(player_input)
        if player_number == computer_number:
            print("You guess it!")
            if player_number == computer_number:
                print("Let's Try (1-200) now!")

                computer_number = random.randint(1, 200)
                guesses = 0
                correct = 0

                while True:
                    player_input = input("Guess the number (1, 200): ")
                    if not player_input.isdigit():
                        print("Invalid input. Try again...")
                        continue
                    player_number = int(player_input)
                    if player_number == computer_number:
                        print("You guess it!")
                        webbrowser.open_new("https://www.youtube.com/watch?v=skVg5FlVKS0")
                        break
                    elif player_number > computer_number:
                        print("Too High!")
                        guesses += 1
                    else:
                        print("Too Low!")
                        guesses += 1

                        if guesses > tries:
                            print("Too Many Guesses! Try again...")
                            break
            break
        elif player_number > computer_number:
            print("Too High!")
            guesses += 1
        else:
            print("Too Low!")
            guesses += 1

            if guesses > tries:
                print("Too Many Guesses! Try again...")
                break
else:
    print("Invalid character name! Try again..")

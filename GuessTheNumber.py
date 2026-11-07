from random import randint
import sys
import time

start_time = time.perf_counter()
max_attempt = {"easy" : 10, "medium" : 5, "hard" : 3}
high_scores = {"easy" : None, "medium" : None, "hard" : None}

while True:
    print("Welcome to GUESS THE NUMBER!!!")
    value = randint(1, 100)
    score = 0
    start_time = time.perf_counter()

    difficulty = str(input("Choose your difficulty level: Easy, Medium, Hard: ")).lower()
    hard = 3
    medium = 5
    easy = 10

    attempts = max_attempt[difficulty]
    if difficulty == "easy":
        attempts = easy
    elif difficulty == "medium":
        attempts = medium
    elif difficulty == "hard":
        attempts = hard


    while difficulty != "easy" and difficulty != "medium" and difficulty != "hard":
        print("Incorrect Operator")
        difficulty = str(input("Choose your difficulty level: Easy, Medium, Hard: ")).lower()
        if difficulty == "easy":
            attempts = easy
        elif difficulty == "medium":
            attempts = medium
        elif difficulty == "hard":
            attempts = hard

        quit = str(input("F to quit or Enter to continue:")).lower()
    guess = int(input(f"You have {attempts} attempts to guess the number between 1 and 100: "))

    while len(str(guess)) >= 3:
        print("Please Guess Numbers from 1 to 100!")
        guess = int(input(f"You have {attempts} attempts to guess the number between 1 and 100: "))
        break

    if quit == "f":
        print("You quited!")
        sys.exit()   

    while guess != value:
        attempts -= 1
        if attempts <= 0 or attempts == 0:
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            print(f"Time: {execution_time:.2f} seconds")
            print("Game Over!")
            break
        if quit == "f":
            print("You quited!")
            sys.exit()
        
        if guess < value:
            print(f"Incorrect! The number is greater than {guess}.")
            quit = str(input("F to quit or Enter to continue:")).lower()
            if quit == "f":
                    print("You quited!")
                    end_time = time.perf_counter()
                    execution_time = end_time - start_time
                    print(f"Time: {execution_time:.2f} seconds")
                    sys.exit()
            guess = int(input(f"You have {attempts} attempts: "))

        else:
            print(f"Incorrect! The number is less than {guess}")
            quit = str(input("F to quit or Enter to continue:")).lower()
            if quit == "f":
                print("You quited!")
                end_time = time.perf_counter()
                execution_time = end_time - start_time
                print(f"Time: {execution_time:.2f} seconds")
                sys.exit()
            guess = int(input(f"You have {attempts} attempts: "))
        if guess == value:
            break
    

    if guess == value:
        score = max_attempt[difficulty] - attempts + 1
        best = high_scores[difficulty]
    if best is None or score < best:
        high_scores[difficulty] = score
        print("New high score!")

    print(f"---Good Job! You guessed Right!---")
    print(f"Guesses used: {score}")
    print(f"Best for {difficulty}: {high_scores[difficulty]} guesses")

    if attempts == 0 or guess == value:
        ask = str(input("Do you want to play again? y/n: ")).lower()
    if ask == "y":
        continue
    elif ask == "n":
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Time: {execution_time:.2f} seconds")
        sys.exit()

    while ask != "n" and ask != "y":
        print("incorrect operative!")
        ask = str(input("Do you want to play again? y/n: ")).lower()
        if ask == "y":
             break
        elif ask == "n":
             break


    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")
    execution_time = 0
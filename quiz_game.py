def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        answered = None
        print("----------------------")
        print(key)
        print("----------------------")
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D):\n").upper()
        for j in range(3):
            while True:
                if guess == "A".upper() or guess == "B".upper() or guess == "C".upper() or guess == "D".upper():
                    answered = True
                    break
                else:
                    print("Please enter a valid answer!")
                    guess = input("Enter (A, B, C, or D):\n").upper()
                    break
            if answered:
                question_num += 1
                guesses.append(guess)
                correct_guesses += check_answer(questions.get(key), guess)
                break
        else:
            from sys import exit
            print("You failed to enter a valid answer 3 times!\nGoodbye!")
            exit()
    display_score(correct_guesses, guesses)
    play_again()


def check_answer(*args):
    from time import sleep
    if args[0] == args[1]:
        print("You were correct! Well done!")
        sleep(2)
        return 1
    elif args[0] != args[1]:
        print("You were incorrect. Nice Try!")
        sleep(2)
        return 0


def display_score(*args):
    print("----------------------")
    print("RESULTS:")
    print("----------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in args[1]:
        print(i, end=" ")
    print()
    print("Your score is {:.2f}%!".format(args[0]/num_of_questions()*100))


def num_of_questions():
    num = 0
    for i in questions:
        num += 1
    return num


def play_again():
    response = input("Would you like to take the quiz again? Yes or no?\n")
    for i in range(3):
        if response == "Yes".lower():
            break
        elif response == "No".lower():
            print("Thanks for taking the quiz!")
            from sys import exit
            exit()
        else:
            response = input("Please answer with yes or no. Would you like to take the quiz again?\n")
            continue
    else:
        print("No valid response given. Exiting quiz.")
        from sys import exit
        exit()
    new_game()


questions = {
    "Who created Python?": "A",
    "What year was Python created?": "B",
    "Python is attributed to which comedy group?": "C",
    "Is the Earth round?": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]


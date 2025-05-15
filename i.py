#lil guessing game type shii
secret = "munyai"
guess = ""
tries = 0
limit = 3
out_of_tries = False
play_again = True
print("Guess the best new age bloodline/famiy")

while play_again == True:  
    while guess != secret and not(out_of_tries):
        if tries < limit:
            guess= input("Enter guess: ")
            tries += 1
        else:
            out_of_tries = True
        if tries == 1:
            print("Hint 1: It is a new South African family")
        elif tries == 2:
            print("Hint 2: It is of the Venda tribe.")
    if guess == secret:
        print("It took " + str(tries) + " tries.")
        print("You are correct!!!")
        print("The Munyais soon to be headed by their heir Mukona O. Munyai is the best new age bloodline")
    else:
        print("Incorrect")   
    play = input("Do you want to play again? \n Y or N").upper
    if play == "Y" :
        play_again = True
        tries = 0
        out_of_tries = False
        guess = ""
    else:
        play_again = False
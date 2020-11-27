
# convert to pure binary

def number_guess():
    lower = 1
    upper = int(input("Enter upper range : "))
    guess = lower + upper - 1
    print("Guess number from ", lower, "to", upper, ": ")
    found = False
    while not found:
        guess = upper+ lower - 1
        user_guess = int(guess/2)
        print("Is your number ", user_guess, ": ")
        playerAnswer = int(input("(Yes). 2(Guess Lower). 3(Guess higher) : "))
        if playerAnswer == 3:
            lower += user_guess  # increment bcs guess was too low
        elif playerAnswer == 2:
            upper -= user_guess  # decrement bcs guess was too high
        elif playerAnswer == 1:  # found the number
            found = True
            print("Found it!")
            break
        else:
            print("Invalid input, try again")
            number_guess()

number_guess()

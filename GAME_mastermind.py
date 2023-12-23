import random

# Generate a random 4-digit number for the player to guess
answer = random.randrange(1000, 10000)
answer_digits = [int(d) for d in str(answer)]

# Initialize variables
attempts = 0
current_digits = []

# Main game loop
while True:
    attempts += 1
    correct_digits = 0

    # Get user input for a 4-digit number
    guess = int(input("Enter a 4-digit number: "))
    guess_digits = [int(d) for d in str(guess)]

    # Check each digit of the guess against the answer
    for i in range(4):
        if answer_digits[i] == guess_digits[i]:
            correct_digits += 1
            current_digits.append(answer_digits[i])
        else:
            current_digits.append("x")

    # Display feedback to the user
    if correct_digits == 4:
        print(f"You guessed the number {answer} in {attempts} attempts\nYou've become a Mastermind!")
        break
    else:
        print(f"Not quite the number. You did get {correct_digits} digits correct.")
        print(" ".join(map(str, current_digits)))

        # Clear the list for the next attempt
        current_digits.clear()

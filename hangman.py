import random, drawing_matrix
list_of_words = ['parachute', 'painting', 'butterfly', 'computer', 'sunrise', 'scissors', 'machine', 'origami', 'spray']
secret_word = random.choice(list_of_words)

line = ['-']*len(secret_word)
print("Welcome to hangman!\n\n")
wrong_guesses = []
max_guesses = 13

# Starting picture
start = """
-----   
|           
|               
|            
|              
|               
|               
|              
|              
--------"""

# Ending picture
end = """
-----
|   |
|   O 
| /-+-\ 
|   |  
|   | 
|  | |
|  | | 
|
--------"""

hangmanPic = drawing_matrix.Matrix(start,end)

guess_cnt = 0  # Start counting of guesses, player can guess 20 times
while (guess_cnt < max_guesses and '-' in line):
    
    # Print accumulator with correctly guessed letters along with "-" showing letters which are still unknown
    # then show list of letters which were tried, but didn't match
    print("\n\n\nWord to guess: " + ' '.join(line)  + "  " + str(max_guesses - guess_cnt) + " attempts left.  Wrong guesses: " + " ".join(wrong_guesses))  

    # Ask user to guess one letter
    letter = input("Please guess a letter: ").lower()

     # Increment guess counter
    guess_cnt += 1

    if letter not in secret_word:
        print("\nOops, that's wrong")
        # Add this incorrect guess to reminder
        wrong_guesses.append(letter) 
        # Draw picture here and move to the next prompt
        hangmanPic.update()
        hangmanPic.print()
        continue
    else:
        print("Nice one!")
        for i in range(len(secret_word)):
            if (letter == secret_word[i]):
                line[i] = letter
        
# Iterations finished - either the word was guessed or guess limit exceeded
if ('-' not in line):
    print("\nAwesome, you win!\n" + str(guess_cnt) + " out of " + str(max_guesses) + " guesses used")
else:
    print("\n\nSorry, you lost. The word was: " + secret_word)
    hangmanPic.update()
    hangmanPic.print()

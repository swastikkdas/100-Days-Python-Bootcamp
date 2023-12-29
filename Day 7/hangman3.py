#Step 3

import random2

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random2.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        print(f"Current position: {position} \n Current letter: {letter}\n Guessed letter:{guess}")
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win!!")
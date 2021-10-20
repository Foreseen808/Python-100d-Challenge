import random
import hangman_art as art
import hangman_words as words

print(art.logo)
chosen_word = random.choice(words.word_list)

end = False
lives = 6

display = []
for _ in range(len(chosen_word)):
  display += "_"

while not end:
    guess = input("Guess a letter: ").lower()
    if (guess in display):
      print(f"You've already guessed {guess}")


    #Check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        

    #If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if (guess not in chosen_word ):
        lives -= 1
        print(f"{guess} is not a part of the word.You have {lives} lives left ")
        if (lives == 0):
          end = True
          print("You lose")   
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end = True
        print("You win.")
      
    print(art.stages[lives])
    





"""Purpose: Play hangman"""

## Install rich first ##  pip install rich
# Import random & sys module
from rich.console import Console
console = Console()
import random
import sys
hangman_guy = [""" """, """ 
_____
|/   |
|   
|    
|    
|    
""",
"""
 ____
|/   |
|   😑
|    
|    
|    
""",
"""
 ____
|/   |
|   😕
|    |
|    |    
|    
""",
"""
 ____
|/   |
|   😟
|   \|
|    |
|    
""",
"""
 ____
|/   |
|   😑
|   \|/
|    |
|    
""",
"""
 ____
|/   |
|   😑
|   \|/
|    |
|   / 
""",
"""
 ____
|/   |
|   😑
|   \|/
|    |
|   / \ 
""",
"""
 ____
|/   |
|   💀
|   /|\ 
|    |
|   | |
"""]


def main():
    """Play hangman game"""
    # Constant for amount of turns
    incorrect = 8
    tries = 0

    # Print heading
    console.print("Hello, Let's play hangman! You will have " + str(incorrect) + " turns!\n", style="bold blue")

    # List of words in game, random word chosen
    wordList = [
        "awkward", "bookworm", "crypt", "dwarves", "espionage", "frazzled", "gnarly", "hyphen", "injury", 
        "jumbo", "keyhole", "lucky", "megahertz", "numbskull", "oxidize", "pixel", "queue", "rhythm", 
        "sphinx", "transplant", "unknown", "vaporize", "wimpy", "xylophone", "yippee", "zipper"]
    word = random.choice(wordList)
    guesses = ''

    # Loop game until no turns are left
    while incorrect > 0:         
        wrong = 0
        for char in word:      
            if char in guesses:    
                print(char, end="") 
            else:
                print("_", end="")     
                wrong += 1    

        # Print blank line
        print()

        # If the game is won
        if wrong == 0:        
            win_text()
            play_again()             

        # Guesses for the game
        guess = ''
        if len(guess) < 1:
            guess = input("\nGuess a character or enter the correct word: ")
        guesses += guess                    

        # If the guess is wrong
        if guess not in word:  
            incorrect -= 1  
            tries += 1
            console.print("Wrong!", style="bold underline red") 
            print("You have", + incorrect, 'incorrect guesses left!')
            print(hangman_guy[tries])
    
            # If there are no turns left
            if incorrect == 0:           
                game_over_text()
                play_again()

        # If the game is won with the word guessed       
        if guess is word:
            win_text()
            play_again() 

def play_again():
    """Gives option to play the game again"""
    print("\nDo you want to play again? (y or n)")
    
    # Convert the player's input() to lower_case
    answer = input("> ").lower()

    if "y" in answer:
        # if player typed "yes" or "y" start the game from the beginning
        main()
    else:
        # if user types anything besides "yes" or "y", exit() the program
        sys.exit()

def game_over_text():
    """Prints when game is lost"""
    console.print("""
   ___   _   __  __ ___    _____   _____ ___ 
  / __| /_\ |  \/  | __|  / _ \ \ / / __| _ \ 
 | (_ |/ _ \| |\/| | _|  | (_) \ V /| _||   /
  \___/_/ \_\_|  |_|___|  \___/ \_/ |___|_|_\ 
                                                                                                    
    """, style="red")  

def win_text():
    """Prints when game is won"""
    console.print("""
 __   __                                _ 
 \ \ / /__  _   _  __      _____  _ __ | |
  \ V / _ \| | | | \ \ /\ / / _ \| '_ \| |
   | | (_) | |_| |  \ V  V / (_) | | | |_|
   |_|\___/ \__,_|   \_/\_/ \___/|_| |_(_)
                                                                                                                         
    """, style="green")  


# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()
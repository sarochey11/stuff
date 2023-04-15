import random

# Get the player information
def getPlayerInformation():
    # Try loop to check if the user input is valid
    try:
        numberOfPlayers = 0
        numberOfPlayers = int(input("Enter the number of players (1 or 2): "))
        player1 = ""
        player2 = ""

        # If the user enters a number of players that is not 1 or 2, ask them to enter a valid number of player names
        if numberOfPlayers == 1:
            # if the user enters a number of players that is 1, ask them to enter their name
            player1 = input("Enter your name: ")
            player2 = ""
        elif numberOfPlayers == 2:
            # if the user enters a number of players that is 2, ask for player 1 and player 2 names
            sameName = True # Variable to check if the players have the same name
            while sameName == True: 
                # While loop to check if the players have the same name
                player1 = input("Enter player 1's name: ").capitalize()
                player2 = input("Enter player 2's name: ").capitalize()
                if player1 != player2: 
                    # If the players have different names, set sameName to False
                    sameName = False
                else:
                    # If the players have the same name, ask them to enter different names
                    print("Player 1 and Player 2 cannot have the same name, please enter different names")

        difficulty = ""

        # If the user enters a difficulty that is not easy, medium or hard, ask them to enter a valid difficulty
        while difficulty not in ["EASY", "MEDIUM", "HARD"]: # If the user enters a difficulty that is not easy, medium or hard, ask them to enter a valid difficulty
            difficulty = input("Enter the difficulty (easy, medium or hard): ").upper() # Convert the difficulty entered to uppercase
        
        predefinedOrGuessesAllowed = input("Please type the number of guesses allowed or press enter for a predefined number of guesses: ")
        
        # if predefinedOrGuessesAllowed is not empty, set the numberOfGuesses to the inputted number of guesses
        if predefinedOrGuessesAllowed != "":
            print("You have selected: ", predefinedOrGuessesAllowed, "guesses")
            numberOfGuesses = int(predefinedOrGuessesAllowed)

        # if the user does not enter a number of guesses, set the number of guesses to a predefined number of guesses
        else:
            print("Predefined selected: You have 10 guesses")
            numberOfGuesses = 10
            
        return numberOfPlayers, player1, player2, difficulty, int(numberOfGuesses)

    except ValueError:
        main()

# Shows the players selected settings
def showSettings(numberOfPlayers, numberOfGuesses, difficulty, player1, player2, gameSelected):
    print("\n---------------------------------------")
    print("Your settings are: ")
    print("---------------------------------------")

    # If the user selected a single player game, show the settings for the single player game
    if numberOfPlayers == 1:
        print(f"Player Name: {player1}")
    # If the user selected a two player game, show the settings for the two player game
    else:
        print(f"""Player 1 Name: {player1}\nPlayer 2 Name: {player2}""")
    
    print(f"Game Selected: {gameSelected}")
    print("---------------------------------------")
    print(f"Guesses Allowed: {numberOfGuesses}")
    print(f"Difficulty Level: {difficulty.capitalize()}")
    print("---------------------------------------\n")

# Random Word Game
def randomNumberGame(numberOfPlayers, player1, player2, difficulty, numberOfGuesses):
    gameSelected = "Random Number Game"
    gameStarted = True
    
    # Sets the difficulty level for the game easy, medium or hard
    if difficulty == "EASY":
        # Sets the range of numbers for the easy difficulty level to 1 to 10
        number = random.randint(1, 10)
        computerNumber = "The computer is thinking of a number between 0 and 10"
    elif difficulty == "MEDIUM":
        # Sets the range of numbers for the medium difficulty level to 1 to 25
        number = random.randint(1, 20)
        computerNumber = "The computer is thinking of a number between 0 and 25"
    elif difficulty == "HARD":
        # Sets the range of numbers for the hard difficulty level to 1 to 50
        number = random.randint(1, 30)
        computerNumber = "The computer is thinking of a number between 0 and 50"

    showSettings(numberOfPlayers ,numberOfGuesses, difficulty, player1, player2, gameSelected) # Show the settings the user selected

    # if loop to check if the user wants to play a two player game

    player1CurrGuesses = 0
    player2CurrGuesses = 0
    player1NumberGuess = numberOfGuesses
    player2NumberGuess = numberOfGuesses

    # While loop to check if the game has started
    while gameStarted:

        # If loop to check if the user has entered a valid number of guesses
        try:
            print(f"{computerNumber}\n") # Prints the range of random numbers the computer is thinking of
            player1Guess = int(input(f"{player1 }, please enter your guess: ")) # Asks player 1 to enter their guess
            player2Guess = int(input(f"{player2 }, please enter your guess: ")) # Asks player 2 to enter their guess
            
            # If loop to check if the player 1 guess is correct
            if player1CurrGuesses == player1NumberGuess:
                print(f"{player1} ran out of guesses. The number was: {number}")
                print("You have been returned to the main menu\n")
                gameStarted = False # Ends the game
            # If loop to check if the player 2 guess is correct
            elif player2CurrGuesses == player2NumberGuess:
                print(f"{player2} ran out of guesses. The number was: {number}")
                print("You have been returned to the main menu\n")
                gameStarted = False # Ends the game

            # Player 1 and Player 2 guesses higher than the number
            elif player1Guess > number and player2Guess > number:
                print(f"{player1}'s guess is too high! You have {player1NumberGuess - player1CurrGuesses} left")
                print(f"{player2}'s guess is too high! You have {player2NumberGuess - player2CurrGuesses} left")
                player1CurrGuesses += 1 # Adds 1 to the player 1 current guesses
                player2CurrGuesses += 1 # Adds 1 to the player 2 current guesses

            # Player 1 and Player 2 guesses lower than the number
            elif player1Guess < number and player2Guess < number:
                print(f"{player1}'s guess is too low! You have {player1NumberGuess - player1CurrGuesses} left")
                print(f"{player2}'s guess is too low! You have {player2NumberGuess - player2CurrGuesses} left")
                player1CurrGuesses += 1 
                player2CurrGuesses += 1

            # Player 1 guesses lower than the number and Player 2 guesses higher than the number
            elif player1Guess < number and player2Guess > number:
                print(f"{player1}'s guess is too low! You have {player1NumberGuess - player1CurrGuesses} left")
                print(f"{player2}'s guess is too high! You have {player2NumberGuess - player2CurrGuesses} left")
                player1CurrGuesses += 1
                player2CurrGuesses += 1
            
            # Player 1 guesses higher than the number and Player 2 guesses lower than the number
            elif player1Guess > number and player2Guess < number:
                print(f"{player1}'s guess is too high! You have {player1NumberGuess - player1CurrGuesses} left")
                print(f"{player2}'s guess is too low! You have {player2NumberGuess - player2CurrGuesses} left")
                player1CurrGuesses += 1
                player2CurrGuesses += 1

            elif player1Guess == number and player2Guess == number:
                print("---------------------------------------")
                print(f"The number was: {number}\n")
                print(f"Congratulations!\nBoth players have guessed the number! \n You both guessed the number in {player1CurrGuesses} guesses")
                print("You have been returned to the main menu")
                gameStarted = False # Ends the game
            
            # Player 1 guesses the number
            elif player1Guess == number:
                print("\n---------------------------------------")
                print(f"The number was: {number}\n")
                print(f"Congratulations! {player1} guessed the number in {player1CurrGuesses} guesses")
                print(f"{player2} has lost the game you guessed {player2CurrGuesses} times\n")
                print("You have been returned to the main menu\n")
                gameStarted = False # Ends the game
            # Player 2 guesses the number
            elif player2Guess == number:
                print("\n---------------------------------------")
                print(f"The number was: {number}\n")
                print(f"Congratulations! {player2} guessed the number in {player2CurrGuesses} guesses")
                print(f"{player1} has lost the game you guessed {player1CurrGuesses} times\n")
                print("You have been returned to the main menu\n")
                gameStarted = False # Ends the game
        
        except ValueError:
            print("Invalid input")
    
    main() # Returns the user to the main menu

# Random Word Game
def randomWordGame(numberOfPlayers, player1, player2, difficulty, numberOfGuesses):
    gameSelected = "Random Word Game"
    gameStarted = True
    hardWords = ["BOTTLE", "CHARGE", "DOCTOR", "GLOBAL", "REDUCE"] # List of hard words
    mediumWords = ["AHEAD", "BELOW", "GHOST", "HORSE", "JOKER"] # List of medium words
    easyWords = ["BEAR", "PLAY", "SING", "BIRD", "LEAN"] # List of easy words
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] # List of the alphabet

    # Shows the settings the user selected
    showSettings(numberOfPlayers, numberOfGuesses, difficulty, player1, player2, gameSelected)

    # Setting the word difficulty
    if difficulty == "EASY":
        word = random.choice(easyWords) # Randomly chooses a word from the easy words list
    elif difficulty == "MEDIUM":
        word = random.choice(mediumWords) # Randomly chooses a word from the medium words list
    elif difficulty == "HARD":
        word = random.choice(hardWords) # Randomly chooses a word from the hard words list
        
    def createDictionary(word):
        # Create a dictionary with the letters of the word
        dictionary = {}
        
        for i, letter in enumerate(word):
            # Create a dictionary for each letter, set the value to the letter and set hidden to True
            dictionary[f"{i+1}"] = {"value": letter, "hidden": True}
        return dictionary # Returns the dictionary
    
    def showHiddenValues(dict):
        showUser = []
        # Loop through the dictionary and show the hidden values

        for i in dict:
            value = dict[i]["value"] # Gets the value of the dictionary
            hidden = dict[i]["hidden"] # Gets the hidden value of the dictionary

            # If the letter is hidden, show a dash
            if hidden == True:
                showUser.append("_ ") # Adds a dash to the list when the letter is hidden

            # If the letter is not hidden, show the letter
            elif hidden == False:
                showUser.append(f"{value} ") # Adds the letter to the list when the letter is not hidden
        showUser = "".join(showUser) # Joins the list into a string
        return showUser # Returns the string
    
    
    dict = createDictionary(word) # Runs the createDictionary function and sets the dictionary to the variable dict
        
        
    currGuess = 0
    allowedLetters = [] # Creates a empty list for the allowed letters
    for i in dict:
        # Adds the letters to the allowed letters list
        allowedLetters.append(dict[i]["value"])
        # Randomly chooses a letter from the allowed letters list
        allowedLetters.append(random.choice(alphabet))


    # Starts the game
    while gameStarted is True:
        # While loop for the number of guesses
        while currGuess < numberOfGuesses:
            # If loop to check if the user has entered a valid number of guesses
            try:
                # Show the user the hidden values
                if "_" not in showHiddenValues(dict):
                    print(f"Congratulations! You guessed the word with {currGuess} wrong guesses")
                    print("You have been returned to the main menu")
                    gameStarted = False # Ends the game
                    main() # Returns the user to the main menu
                print(showHiddenValues(dict) + "\n") # Shows the user the hidden values
                prettyAllowedLetters = ", ".join(allowedLetters) # Joins the allowed letters list into a string
                print(f"Allowed letters (includes scrambled word): {prettyAllowedLetters}") # Shows the user the allowed letters
                guess = input("Enter your guess: ").upper() # Asks the user for their guess and sets it to the variable guess and makes it uppercase
                # If the user guesses the word, end the game
                if guess in alphabet:
                    # If the user guesses a letter in the word
                    if guess in word:
                        # Loop through the dictionary
                        for i in dict:
                            # If the letter is in the dictionary, set hidden to False
                            if dict[i]["value"] == guess:
                                dict[i]["hidden"] = False # Sets the hidden value to False
                        print(f"Correct! You have {numberOfGuesses - currGuess} guesses left\n") # Users input was correct and shows how many guesses are left
        
                    else:
                        currGuess += 1  # Adds 1 to the current guess
                        print(f"Wrong! You have {numberOfGuesses - currGuess} guesses left\n") # Shows the user how many guesses they have left when the guess is wrong
                        
                    for i in allowedLetters:
                            if i == guess:
                                # Removes the letter from the allowed letters list when the user guesses the letter
                                allowedLetters.remove(i)
                else:
                    # If the user guesses are invalid (not a letter or more than 1 letter) show an error message
                    print(f"Invalid input, you have {numberOfGuesses - currGuess} guesses left\n")
            except ValueError:
                print("Invalid input")
        print("You ran out of guesses...")
        print(f"The word was: {word}")
        gameStarted = False # Ends the game
        break # Breaks the while loop
        
    main() # Returns the user to the main menu

# Main Menu
def main():
    print("Welcome to the Guessing Game!")
    print("You can either play a Random Word Guessing game which is a single player game or a random Number guessing game which is a two player game\n")
    numberOfPlayers, player1, player2, difficulty, numberOfGuesses = getPlayerInformation() # Runs the getPlayerInformation function and sets the variables to the variables in the function

    # If the user selects the Random Word Game, run the randomWordGame function
    if numberOfPlayers == 1:
        randomWordGame(numberOfPlayers, player1, player2, difficulty, numberOfGuesses)
    elif numberOfPlayers == 2:
        randomNumberGame(numberOfPlayers, player1, player2, difficulty, numberOfGuesses)
        

main() # Runs the main function
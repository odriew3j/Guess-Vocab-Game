import random

def mainProject():
    """Main function to start the project by calling the menu."""
    menuProject()

def menuProject():
    """Displays the main menu options and prompts user input."""
    print("---------------------------------------------------------")
    print("|", "1.Start\t", "2.Help\t\t", "3.About US\t", "4.Exit", "|")
    print("----------------------------------------------------")
    inputProject()

def inputProject():
    """Handles user input for menu selection and calls the corresponding function."""
    choiceClonte = input("Enter your choice : ")
    if choiceClonte == "1":
        startProject()
    elif choiceClonte == "2":
        helpProject()
    elif choiceClonte == "3":
        aboutUsProject()
    elif choiceClonte == "4":
        exitProject()
    else:
        print("Invalid choice")
        menuProject()

def startProject():
    """Starts the 'Guess Vocab Game' by randomly selecting and obscuring words for the user to guess."""
    print("\nWelcome to Guess Vocab Game\n")

    # List of animal names used in the game
    animal_list = ['Dog', 'Cow', 'Cat', 'Horse', 'Donkey', 'Tiger', 'Lion', 'Leopard',
    'Cheetah', 'Bear', 'Elephant', 'Polar', 'Turtle', 'Crocodile', 'Rabbit', 'Hen', 'Pigeon',
    'Crow', 'Fish', 'Dolphin', 'Frog', 'Whale', 'Alligator', 'Eagle', 'Squirrel', 'Ostrich',
    'Fox', 'Goat', 'Wolf', 'Gorilla', 'Chimpanzee', 'Monkey', 'Hamster', 'Orangutan',
    'Giraffe', 'Bat', 'Panda', 'Shark', 'Camel', 'Sheep', 'Rat', 'Snake', 'Raccoon',
    'Jellyfish', 'Chameleon', 'Otter', 'Peacock', 'Boar', 'Zebra', 'Flamingo']
    
    random.shuffle(animal_list) # Shuffle the list for randomness
    selected_animals = random.sample(animal_list, min(20, len(animal_list)))
    score = 0   # Initialize player score
    
    for word in selected_animals:
        hidden_word = list(word)    # Convert word to list for modification
        length = len(word)
        num_spaces = 2 if length <= 5 else 3  # Determine number of missing letters
        indices = random.sample(range(length), num_spaces)  # Select random positions
        
        for i in indices:
            hidden_word[i] = "_"  # Replace selected positions with "_"
        
        print("Guess the word: ", "".join(hidden_word))
        user_guess = []
        
        for i in range(num_spaces):
            guess = input(f"Enter your {i+1} character: ").strip().lower()  # Convert input to lowercase
            
            # Check if input is valid (not empty and a single character)
            while len(guess) != 1 or not guess.isalpha():
                print("Invalid input! Please enter a single letter.")
                guess = input(f"Enter your {i+1} character: ").strip().lower()
            
            user_guess.append(guess)
        
        # Convert actual letters to lowercase for comparison
        correct_letters = [word[i].lower() for i in indices]
        
        # Sort both lists to allow for any order of input
        if sorted(user_guess) == sorted(correct_letters):
            print("Well Done :)")
            print(word)
            score += 1
        else:
            print(f"Wrong! The correct word was {word}")
    
    print("\nGame Over! Your score:", score)
    if score > 18:
        print("You are Strong!")
    elif 10 <= score <= 18:
        print("You are Middle!")
    else:
        print("You are Weak!")
    
    menuProject()

def helpProject():
    print("\nIf you guess the missing letters correctly, you get one score.\n"
          "If you can guess more than 18 words correctly, you are strong.\n"
          "If you guess between 10 and 18 words, you are middle.\n"
          "If you guess less than 10 words, you are weak.\n")
    menuProject()

def aboutUsProject():
    print("\nFull name : 'Example'\n"
          "Email address : Exampl@gmail.com\n"
          "Major : Example\n")
    menuProject()

def exitProject():
    print("Exiting the project...")
    exit()

menuProject()
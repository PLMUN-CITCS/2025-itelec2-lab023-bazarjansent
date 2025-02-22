def display_menu():
    """Displays the menu options to the user."""
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Word Counter")
    print("4. Exit")

def get_integer_input(prompt: str) -> int:
    """Handles user input to obtain an integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def check_even_odd(number: int) -> str:
    """Determines if a given number is even or odd."""
    return f"{number} is an Even number." if number % 2 == 0 else f"{number} is an Odd number."

def greet_user():
    """Prints a greeting message."""
    print("Hello! Welcome!")

def even_odd_checker_action():
    """Handles even/odd checking process."""
    number = get_integer_input("Enter an integer: ")
    print(check_even_odd(number))

def get_sentence_input() -> str:
    """Obtains a sentence input from the user."""
    return input("Enter a sentence: ")

def count_words(sentence: str) -> int:
    """Counts the number of words in a given sentence."""
    return len(sentence.split())

def word_counter_action():
    """Handles the word counting process."""
    sentence = get_sentence_input()
    print(f"The sentence has {count_words(sentence)} words.")

def handle_menu_choice(choice: int) -> bool:
    """Executes the corresponding action based on the user's menu choice."""
    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker_action()
    elif choice == 3:
        word_counter_action()
    elif choice == 4:
        print("Exiting program. Goodbye!")
        return True
    else:
        print("Invalid choice. Please enter a valid option.")
    return False

def main():
    """Main program loop."""
    while True:
        display_menu()
        choice = get_integer_input("Enter your choice (1-4): ")
        if handle_menu_choice(choice):
            break

if __name__ == "__main__":
    main()

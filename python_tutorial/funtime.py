import random

def personalized_greeting():
    """Personalized Greeting App"""
    print("=== Personalized Greeting ===")
    name = input("What's your name? ")
    color = input("What's your favorite color? ")
    print(f"Hello, {name}! Your favorite color, {color}, is awesome!")
    print()

def quiz_game():
    """Simple Quiz Game"""
    print("=== Python Quiz Game ===")
    questions = [
        {
            "question": "What is the correct file extension for Python files?",
            "options": ["A) .pyt", "B) .py", "C) .python", "D) .pt"],
            "answer": "B"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A) function", "B) def", "C) func", "D) define"],
            "answer": "B"
        },
        {
            "question": "What data type is used to store multiple items in Python?",
            "options": ["A) string", "B) integer", "C) list", "D) boolean"],
            "answer": "C"
        }
    ]
    
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)
        
        answer = input("Your answer (A/B/C/D): ").upper()
        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}")
        print()
    
    print(f"Your final score: {score}/{len(questions)}")
    print()

def joke_generator():
    """Random Joke Generator"""
    print("=== Random Programming Joke Generator ===")
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
        "Why do Python programmers wear glasses? Because they can't C!",
        "What's a programmer's favorite hangout place? Foo Bar!",
        "Why did the programmer quit his job? He didn't get arrays!",
        "How do you comfort a JavaScript bug? You console it!",
        "Why do programmers hate nature? It has too many bugs!",
        "What do you call a programmer from Finland? Nerdic!"
    ]
    
    random_joke = random.choice(jokes)
    print(random_joke)
    print()

def main():
    """Main menu for all apps"""
    while True:
        print("=== Fun Time Apps ===")
        print("1. Personalized Greeting")
        print("2. Quiz Game")
        print("3. Random Joke Generator")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            personalized_greeting()
        elif choice == "2":
            quiz_game()
            play_again = input("Want to play again? (y/n): ").lower()
            if play_again == "y":
                quiz_game()
        elif choice == "3":
            joke_generator()
        elif choice == "4":
            print("Thanks for using Fun Time Apps! Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
        
        input("Press Enter to continue...")
        print()

if __name__ == "__main__":
    main()

# fun time.py - A collection of fun apps

# 1. Accept user input to create a list of integers and compute the sum
int_list = input("Enter integers separated by spaces: ").split()
int_list = [int(num) for num in int_list]
print("Sum of integers:", sum(int_list))

print()  # Blank line for readability

# 2. Tuple of favorite books and print each on a new line
favorite_books = ("1984", "To Kill a Mockingbird", "The Hobbit", "Pride and Prejudice", "The Great Gatsby")
print("Favorite books:")
for book in favorite_books:
    print(book)

print()  # Blank line for readability

# 3. Dictionary to store person info from user input
person = {}
person['name'] = input("Enter your name: ")
person['age'] = input("Enter your age: ")
person['favorite_color'] = input("Enter your favorite color: ")
print("Person info:", person)

print()  # Blank line for readability

# 4. Accept user input to create two sets of integers, then find common elements
set1 = set(map(int, input("Enter integers for set 1 (space-separated): ").split()))
set2 = set(map(int, input("Enter integers for set 2 (space-separated): ").split()))
common_elements = set1 & set2
print("Common elements:", common_elements)

print()  # Blank line for readability

# 5. List of words and list comprehension for words with odd number of characters
words = ["apple", "banana", "cherry", "date", "fig", "grape"]
odd_length_words = [word for word in words if len(word) % 2 == 1]


print("Words with odd number of characters:", odd_length_words)
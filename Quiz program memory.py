# Dictionary to store users' data in memory
users_data = {}

# Function to register a new user
def register():
    username = input("Enter a new username: ")
    if username in users_data:
        print("Username already exists. Try again.")
        return
    password = input("Enter a password: ")
    users_data[username] = {'password': password, 'score': 0}
    print(f"User {username} registered successfully!")

# Function to login an existing user
def login():
    username = input("Enter your username: ")
    if username not in users_data:
        print("User not found. Please register first.")
        return None
    password = input("Enter your password: ")
    if users_data[username]['password'] == password:
        print(f"Welcome back, {username}!")
        return username
    else:
        print("Incorrect password.")
        return None

# Function to handle the quiz
def play_quiz(username):
    questions = [
        {"question": "What does AI stand for?", "options": ["Artificial Intelligence", "Automated Interaction", "Automatic Internet", "Analog Integration"], "answer": 1},
        {"question": "Which of the following is a common application of AI?", "options": ["Image recognition", "Texting", "Manual labor", "Watching TV"], "answer": 1},
        {"question": "Who is known as the father of AI?", "options": ["Alan Turing", "Elon Musk", "John McCarthy", "Bill Gates"], "answer": 3},
        {"question": "Which of these is a type of AI?", "options": ["Supervised Learning", "Carpet Learning", "Human Learning", "Text Learning"], "answer": 1},
        {"question": "What is the goal of reinforcement learning?", "options": ["Maximizing the reward", "Minimizing the effort", "Maximizing the risk", "None of the above"], "answer": 1}
    ]
    
    score = 0
    for q in questions:
        print(f"\n{q['question']}")
        for i, option in enumerate(q['options'], 1):
            print(f"{i}. {option}")
        
        try:
            answer = int(input("Enter the number of your answer: ").strip())
            if answer == q["answer"]:
                score += 1
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
    
    users_data[username]['score'] = score
    print(f"\nYour score is: {score}/5")

# Function to show the result of the user
def show_result(username):
    print(f"Your score is: {users_data[username]['score']}/5")

# Main function to drive the program
def main():
    while True:
        print("\nChoose an option:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            username = login()
            if username:
                while True:
                    print("\n1. Play Quiz")
                    print("2. Show Result")
                    print("3. Exit")
                    sub_choice = input("Your choice: ")

                    if sub_choice == "1":
                        play_quiz(username)
                    elif sub_choice == "2":
                        show_result(username)
                    elif sub_choice == "3":
                        print("Exiting...")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Function to register a new user
def register():
    username = input("Enter a new username: ")
    password = input("Enter a password: ")

    # Check if the username already exists
    with open("registration.txt", "r") as file:
        users = file.readlines()

    for user in users:
        existing_username, _ = user.strip().split(":")
        if existing_username == username:
            print("Username already exists. Try again.")
            return

    # Register the new user
    with open("registration.txt", "a") as file:
        file.write(f"{username}:{password}\n")
    print(f"User {username} registered successfully!")

# Function to login an existing user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password match
    with open("registration.txt", "r") as file:
        users = file.readlines()

    for user in users:
        stored_username, stored_password = user.strip().split(":")
        if stored_username == username and stored_password == password:
            print(f"Welcome back, {username}!")
            return username
    print("Incorrect username or password.")
    return None

# Function to get the quiz questions
def load_questions(section):
    questions = []
    with open("questions.txt", "r") as file:
        for line in file:
            parts = line.strip().split("|")
            if parts[0].lower() == section.lower():
                questions.append(parts[1:])
    return questions

# Function to save the result after the quiz
def save_result(username, score):
    with open("results.txt", "a") as file:
        file.write(f"{username}:{score}\n")

# Function to show the user's result
def show_result(username):
    with open("results.txt", "r") as file:
        results = file.readlines()

    for result in results:
        stored_username, stored_score = result.strip().split(":")
        if stored_username == username:
            print(f"{username}, your score: {stored_score}")
            return
    print("No result found.")

# Function to play the quiz
def play_quiz(username):
    questions = get_questions()
    score = 0

    for q in questions:
        print(f"\n{q['question']}")
        for i, option in enumerate(q['options'], 1):
            print(f"{i}. {option}")

        try:
            # Get the user's choice of answer
            answer = int(input("Enter the number of your answer: ").strip())
            if answer == q["answer"]:
                score += 1
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")

    # Save the user's result
    save_result(username, score)
    print(f"\nYour score is: {score}/5")

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

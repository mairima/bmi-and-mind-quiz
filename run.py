# Import necessary modules
import time #To pause output between rules for readability
import pyfiglet #To generate large ASCII art text

# Questions for the mind quiz
mind_questions = {
    "Appreciation": "Extend of daily appreciation of yourself",
    "Confidence": "How confident are you in challenges",
    "Management": "How do you manage time, emotions, responsibilities",
    "Accepting criticism": "How open to receiving feedback for growth",
    "Accept mistakes": "How well do you own and learn from mistakes",
    "Selfgrowth": "How focused are you on your ambitions",
    "Health": "Balanced diet, regular activity, restful sleep",
    "Responsibility": "Standing for rights & respecting others"
}

# Tips shown for each trait when the user scores below 5
mind_tips = {
    "Appreciation": "Practice affirmations and self-care.",
    "Confidence": "Set small goals and celebrate wins.",
    "Management": "Use planners and manage priorities.",
    "Accepting criticism": "Pause, reflect, and grow from it.",
    "Accept mistakes": "Learn and improve from your errors.",
    "Selfgrowth": "Focus on your journey.",
    "Health": "Eat balanced meals, move regularly, and rest.",
    "Responsibility": "Stand up respectfully and stay accountable."
}

# Tips based on BMI category
bmi_tips = {
    "Underweight": "Increase healthy calories and consult a doctor.",
    "Normal": "Keep up your good habits!",
    "Overweight": "Be active and watch portion sizes.",
    "Obese": "Seek a structured plan with professional help."
}
# Store user data during the game
user_data = {
    "name": "",
    "bmi": None,
    "bmi_category": "",
    "mind_score": None
}


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    print("\033c")


# Function to display the rules of the game
def show_rules():
    print("\n=== QUIZ RULES ===\n")
    time.sleep(0.5)
    print("1. Choose options from the main menu using the number provided.")
    time.sleep(0.5)
    print("2. In BMI quiz, provide your height and weight in numbers.")
    time.sleep(0.5)
    print(
        "3. In the Mind Quiz, answer each question from "
        "1 (lowest) to 5 (highest)."
    )
    time.sleep(0.5)
    print(
        "4. You'll get improvement tips if your score is "
        "below 5 on any question."
    )
    time.sleep(0.5)
    print("5. You can quit after completing a quiz. Press enter to restart.")
    time.sleep(0.5)
    input("\nPress Enter to Return back to the Menu\n")
    clear()


# Input function that checks for valid float input
def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Enter a valid number.")


# Function to run the BMI quiz
def run_bmi_quiz():
    print("\n=== BMI QUIZ ===\n")
    weight = get_valid_float("Enter weight in kg: ")
    clear()
    print("\n=== BMI QUIZ ===\n")
    height = get_valid_float("Enter height in meters: ")
    clear()
    bmi = round(weight / (height ** 2), 1)

    # Determine BMI category
    category = ("Underweight" if bmi < 18.5 else
                "Normal" if bmi < 25 else
                "Overweight" if bmi < 30 else "Obese")
    print("\n=== BMI QUIZ RESULTS ===\n")
    print(f"\n{user_data['name']}, your BMI is {bmi} ({category})")

    # Give a tip if not in the normal range
    if category != "Normal":
        print(f"Tip: {bmi_tips[category]}")
        print(f"\n💡 Tip: {bmi_tips[category]}\n")
    # Save BMI results
    user_data['bmi'] = bmi
    user_data['bmi_category'] = category

  


# Function to run the mind personality quiz
def run_mind_quiz():
    print("\n=== MIND PERSONALITY QUIZ ===")
    score = 0
    # Iterate through each question and collect a valid response
    for trait, question in mind_questions.items():
        while True:
            print("\n=== MIND PERSONALITY QUIZ ===\n")
            print("Enter 1 (lowest) to 5 (highest)")
            answer = input(f"{question}?: ")
            clear()
            if answer.isdigit() and 1 <= int(answer) <= 5:
                rating = int(answer)
                score += rating
                # Show a tip for ratings less than 5
                if rating < 5:
                    print(
                        f"Q: {question}\n\n💡 Tip for {trait}: "
                        f"{mind_tips[trait]}"
                    )
                    # time.sleep(4)
                    input("\nPress Enter to Continue\n")
                    clear()
                else:
                    clear()
                break
            clear()
            print(f"❌ {answer} is invalid. Enter a number between 1 and 5.")

    print("\n=== MIND PERSONALITY QUIZ RESULTS ===\n")
    print(f"\n{user_data['name']}, total mind score: {score}/45\n")
    user_data['mind_score'] = score


# Restart the game loop
def ask_restart():
    try:
        input("Quiz Over. Press Enter to start again...\n")
        clear()
        main(restart=True)
    except Exception:
        print("Unexpected input. Restarting game...")
        main(restart=True)


# Main function: shows menu and starts quiz
def main(restart=False):
    print("=== WELCOME TO THE HEALTH & MIND QUIZ GAME ===")

    # Ask for name only once (or if starting fresh)
    if not restart:
        while True:
            name = input("Enter your name: \n").strip()
            clear()
            if not name:
                print(f"❌ {name} is invalid. Name cannot be empty.")
            elif not name.isalpha():
                print(f"❌ {name} is invalid. Names can only use letters.")
            else:
                user_data["name"] = name
                break

    # Reset previous quiz data
    user_data["bmi"] = None
    user_data["bmi_category"] = ""
    user_data["mind_score"] = None

    while True:
        # Show main menu
        print("\n=== MAIN MENU ===")
        print("1. View Rules")
        print("2. Take BMI Quiz")
        print("3. Take Mind Quiz")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        clear()

        # Handle menu selection
        if choice == '1':
            show_rules()
        elif choice == '2':
            run_bmi_quiz()
        elif choice == '3':
            run_mind_quiz()
        elif choice == '4':
            clear()
            print('Thank you for using Health & Mind Quiz Game')
            exit()
        else:
            print(f"❌ {choice} is an invalid choice. Enter 1-4.")


        # If a quiz was taken, save and prompt to restart
        if user_data['bmi'] or user_data['mind_score']:
           
            ask_restart()


# Entry point for the script
if __name__ == "__main__":
    clear()
    main()

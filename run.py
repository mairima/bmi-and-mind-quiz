# Import necessary modules
import csv                  # For writing quiz results to a CSV file
import os                   # For checking file existence
from datetime import datetime  # For timestamping results
import sys                  # For exiting the program if needed

# Set the filename for saving quiz results
FILENAME = "quiz_results.csv"
# Define the CSV file headers
HEADERS = ["Name", "Date", "BMI", "BMI Category", "Mind Quiz Score"]
# Create the file with headers if it doesn't exist yet
if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', newline='') as f:
        csv.writer(f).writerow(HEADERS)
        
        # Questions for the mind quiz
mind_questions = {
    "Loving yourself": "To what extent do you appreciate and value yourself daily? (1-5): ",
    "Confidence": "How willing are you to take on new challenges without fear of failure? (1-5): ",
    "Self-Management": "How effectively do you manage your time, emotions, and responsibilities? (1-5): ",
    "Accepting constructive criticism": "How open are you to receiving feedback and using it to grow? (1-5): ",
    "Accepting your mistakes": "When you make a mistake, how well do you own and learn from it? (1-5): ",
    "Avoid jealousy, envy and competition": "How often do you focus on your own growth instead of comparing yourself to others? (1-5): ",
    "Diet, exercise and sleep": "How consistently do you maintain a balanced diet, regular activity, and restful sleep? (1-5): ",
    "Rights and responsibilities": "How well do you stand up for your rights while respecting others and fulfilling your duties? (1-5): "
}

# Tips shown for each trait when the user scores below 5
mind_tips = {
    "Loving yourself": "Practice affirmations and self-care.",
    "Confidence": "Set small goals and celebrate wins.",
    "Self-Management": "Use planners and manage priorities.",
    "Accepting constructive criticism": "Pause, reflect, and grow from it.",
    "Accepting your mistakes": "Learn and improve from your errors.",
    "Avoid jealousy, envy and competition": "Focus on your journey.",
    "Diet, exercise and sleep": "Eat balanced meals, move regularly, and rest.",
    "Rights and responsibilities": "Stand up respectfully and stay accountable."
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

# Function to display the rules of the game
def show_rules():
    print("""\n=== QUIZ RULES ===
1. Choose options from the main menu using the number provided.
2. In BMI quiz, provide your height and weight in numbers. Decimals with a dot (e.g., 1.60 for height in meters).
3. In the Mind Quiz, answer each question from 1 (lowest) to 5 (highest).
4. You’ll get improvement tips if your score is below 5 on any question.
5. Results are saved only after completing a quiz.
6. You can quit after completing a quiz. After the game ends, press any key to restart.
""")

# Input function that checks for valid float input
def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a valid number.")
  
# Function to run the BMI quiz
def run_bmi_quiz():
    print("\n=== BMI QUIZ ===")
    weight = get_valid_float("Enter weight in kg: ")
    height = get_valid_float("Enter height in meters: ")
    bmi = round(weight / (height ** 2), 1)  
    
    # Determine BMI category
    category = ("Underweight" if bmi < 18.5 else
                "Normal" if bmi < 25 else
                "Overweight" if bmi < 30 else "Obese")    
    print(f"\n{user_data['name']}, your BMI is {bmi} ({category})")
    
    # Give a tip if not in the normal range
    if category != "Normal":
        print(f"💡 Tip: {bmi_tips[category]}")
        
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
            answer = input(question)
            if answer.isdigit() and 1 <= int(answer) <= 5:
                rating = int(answer)
                score += rating
        # Show a tip for ratings less than 5
                if rating < 5:
                    print(f"Tip for {trait}: {mind_tips[trait]}")
                break
            print("Enter a number between 1 and 5.")
    print(f"\n{user_data['name']}, total mind score: {score}/45")
    user_data['mind_score'] = score
    
    # Save the results to the CSV file
    def save_results():
    if user_data['bmi'] is not None or user_data['mind_score'] is not None:
        with open(FILENAME, 'a', newline='') as f:
             csv.writer(f).writerow([
                user_data['name'],
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                user_data['bmi'],
                user_data['bmi_category'],
                user_data['mind_score']
            ])
        print("Progress saved.")
        
    # Restart the game loop
    def ask_restart():
    try:
        input("Game Over. Press any key to start again... ")
        main(restart=True)
    except Exception:
        print("⚠️ Unexpected input. Restarting game...")
        main(restart=True)
    # Main function: shows menu and starts quiz
    def main(restart=False):
    print("=== WELCOME TO THE HEALTH & MIND QUIZ GAME ===")
    
     # Ask for name only once (or if starting fresh)
    if not restart or user_data['name'] == "":
        name = input("Enter your name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        user_data["name"] = name
        
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
        choice = input("Choose an option (1-3): ").strip()
        
       # Handle menu selection
        if choice == '1':
            show_rules()
        elif choice == '2':
            run_bmi_quiz() 
        elif choice == '3':
            run_mind_quiz()
        else:
            print("Invalid choice. Enter 1-3.")
            
     # If a quiz was taken, save and prompt to restart
        if user_data['bmi'] or user_data['mind_score']:
            save_results()
            ask_restart()
            
# Entry point for the script
if __name__ == "__main__":
    main()
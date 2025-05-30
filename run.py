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
    
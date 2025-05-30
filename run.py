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
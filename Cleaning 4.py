import os
import pandas as pd

# Function to split CSV file by 'Question' column
def split_csv_by_question(csv_file_path, output_folder):
    print(f"Processing file: {csv_file_path}")
    try:
        # Read the CSV file
        data = pd.read_csv(csv_file_path)
        
        # Get unique questions
        unique_questions = data['Question'].unique()
        print(f"Unique questions: {unique_questions}")
        
        # Create folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Split data by question and save to separate CSV files
        for question in unique_questions:
            question_data = data[data['Question'] == question]
            question_file_name = f'{os.path.splitext(os.path.basename(csv_file_path))[0]}_{question.replace(" ", "_")}.csv'
            question_file_path = os.path.join(output_folder, question_file_name)
            print(f"Saving question data to: {question_file_path}")
            question_data.to_csv(question_file_path, index=False)
    except Exception as e:
        print(f"Error occurred while processing file {csv_file_path}: {e}")

# Input folder containing CSV files
input_folder = "C:/Users/jacka/OneDrive - University of Keele/Visualisation/output_files10"

# Output folder for split CSV files
output_folder = "C:/Users/jacka/OneDrive - University of Keele/Visualisation/Cleaned_Questions"

# Process each CSV file in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(".csv"):
        file_path = os.path.join(input_folder, file_name)
        split_csv_by_question(file_path, output_folder)

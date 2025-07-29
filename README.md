Project Title: Simple Patient Data Entry System using Python

Objective: The goal of this project is to create a basic command-line application to collect and store patient information in a structured format. It ensures that all necessary fields are entered correctly before saving the data.

Functionality: User Input Collection:

The system prompts the user to enter essential patient details:

Name

Date of Birth (in YYYY-MM-DD format)

Mobile Number

Batch Number (numeric)

Data Storage:

The collected information is stored in a Python dictionary for easy access and structure.

Data Validation Check: A check is performed using the all() function to verify that none of the values are empty.

If all fields are filled, a confirmation message is displayed.

If any required field is missing or empty, an error message is shown.

Technical Details: Python Version: This code works with Python 3.x.

Libraries Used:

datetime (imported but not currently used—can be helpful for validating date format).

Data Structure: Dictionary is used to store and manage patient data efficiently.

Use Cases: This project can be useful in small clinics, camps, or healthcare workshops for maintaining basic patient records in a structured digital format. It can also serve as a learning project for beginners in Python to understand user input, conditionals, and data structures.

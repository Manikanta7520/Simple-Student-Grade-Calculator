# Student Grade Calculator
# Author: Sai Manikanta
# Internship: Developers Arena - Data Science Domain
# Week 2 Project

def calculate_grade(marks):
    """Returns grade and encouragement message based on marks."""
    if marks >= 90:
        return "A", "Outstanding performance! 🌟 Keep shining!"
    elif marks >= 80:
        return "B", "Well done! You’re on the right track 👍"
    elif marks >= 70:
        return "C", "Good effort! Keep pushing for excellence 💪"
    elif marks >= 50:
        return "D", "You passed! Try to strengthen your concepts 📘"
    else:
        return "F", "Don’t worry, learn from mistakes and try again 💫"

# Taking input from the user
student_name = input("Enter student name: ")
marks = float(input("Enter total marks (out of 100): "))

# Getting grade and message
grade, message = calculate_grade(marks)

# Displaying the final report
print("\n===== Student Grade Report =====")
print(f"Name       : {student_name}")
print(f"Marks      : {marks}")
print(f"Grade      : {grade}")
print(f"Message    : {message}")
print("=================================")

# Take input score from the user
total_score = float(input("Enter the total score: "))

# Determine the letter grade based on the grading scheme
if total_score >= 90:
    grade = 'A'
elif total_score >= 80:
    grade = 'B'
elif total_score >= 70:
    grade = 'C'
elif total_score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Print the letter grade
print("Final Grade for the given score is:", grade)
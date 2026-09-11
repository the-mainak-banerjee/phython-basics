# Challenge: Quiz Pass or Fail
# You're building the results screen for an online course quiz. A student
# needs at least 60 points to pass.

# 1. Ask the student for their score and convert it to an int.
# 2. If their score is 60 or higher, print that they passed.
# 3. Otherwise, print that they didn't pass this time

score = int(input("What is your score? "))
if score >= 60:
    print("Congratulations! You have passed the quiz")
else:
    print("Sorry you failed")
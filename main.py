# Author: Dominic Savaglio
# Collaborator: 
# Collaborator:
# Collaborator:
# Section: 10R
# Breakout: 
def getLetterGrade(grade):
  if grade >= 93.0:
    return "A"
  elif grade >= 90.0:
    return "A-"
  elif grade >= 87.0:
    return "B+"
  elif grade >= 83.0:
    return "B"
  elif grade >= 80.0:
    return "B-"
  elif grade >= 77.0:
    return "C+"
  elif grade >= 70.0:
    return "C"
  elif grade >= 60.0:
    return "D"
  else:
    return "F"
def run():
  grade = float(input("Enter your CMPSC 131 grade: "))
  letter_grade = getLetterGrade(grade)
  print("Your letter grade for CMPSC 131 is " + letter_grade + ".")
if __name__ == "__main__":
  run()

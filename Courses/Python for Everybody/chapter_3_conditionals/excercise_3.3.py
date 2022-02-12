
# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
try:
  score = float(input("Enter score: "))

  if score >= 0.0 and score <= 1.0:
    if score >= 0.9:
      print("A")
    elif score >= 0.8:
      print("B")
    elif score >= 0.7:
      print("C")
    elif score >= 0.6:
      print("D")
    elif score < 0.6:
      print("F")
  else:
    print("Bad score")

except:
  print("Bad score")

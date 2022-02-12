# Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

def computegrade(score):
  min_score = 0.0
  max_score = 1.0
  if score >= min_score and score <= max_score:
    if score >= 0.9:
      return "A"
    elif score >= 0.8:
      return "B"
    elif score >= 0.7:
      return "C"
    elif score >= 0.6:
      return "D"
    elif score < 0.6:
      return "F"
  else:
    return "Bad score"

try:
  score = float(input("Enter score: "))
  print(computegrade(score))

except:
  print("Bad score")
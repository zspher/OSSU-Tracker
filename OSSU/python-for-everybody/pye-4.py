# Exercise 4: What is the purpose of the “def” keyword in Python? b

# a) It is slang that means “the following code is really cool”
# b) It indicates the start of a function
# c) It indicates that the following indented section of code is to be stored for later
# d) b and c are both true
# e) None of the above

# Exercise 5: What will the following Python program print out? b

# def fred():
#    print("Zap")

# def jane():
#    print("ABC")

# jane()
# fred()
# jane()

# a) Zap ABC jane fred jane
# b) Zap ABC Zap
# c) ABC Zap jane
# d) ABC Zap ABC
# e) Zap Zap Zap

# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

# def computepay(hours, rate):
#   overtime_limit = 40
#   overtime_pay_rate = 1.5
#   if hours <= overtime_limit:
#     return hours * rate
#   overtime = hours - overtime_limit
#   return (rate * overtime_limit) + (overtime*overtime_pay_rate*rate)


# try:
#   hours = float(input("Enter Hours: "))
#   rate = float(input("Enter Rate: "))
#   pay = computepay(hours, rate)
#   print("Pay: ", pay)
# except:
#   print("Error, please enter numeric input")

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
# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

# hours = float(input("Enter Hours: "))
# rate = float(input("Enter Rate: "))
# if hours > 40:
#   pay = (rate * 40) + (rate * 1.5 * (hours-40))
# else:
#   pay =  hours * rate

# print("Pay: ", pay)

# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# try:
#     hours = float(input("Enter Hours: "))
#     rate = float(input("Enter Rate: "))
#     overtime_limit = 40
#     overtime_pay_rate = 1.5 
#     if hours > overtime_limit:
#         overtime = hours - overtime_limit 
#         pay = (rate * overtime_limit) + (overtime*overtime_pay_rate*rate)
#     else:
#         pay = hours * rate
#     print("Pay: ", pay)
# except:
#     print("Error, please enter numeric input")

# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
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

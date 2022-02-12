# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
if hours > 40:
  pay = (rate * 40) + (rate * 1.5 * (hours-40))
else:
  pay =  hours * rate

print("Pay: ", pay)
# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def computepay(hours, rate):
  overtime_limit = 40
  overtime_pay_rate = 1.5
  if hours <= overtime_limit:
    return hours * rate
  overtime = hours - overtime_limit
  return (rate * overtime_limit) + (overtime*overtime_pay_rate*rate)


try:
  hours = float(input("Enter Hours: "))
  rate = float(input("Enter Rate: "))
  pay = computepay(hours, rate)
  print("Pay: ", pay)
except:
  print("Error, please enter numeric input")

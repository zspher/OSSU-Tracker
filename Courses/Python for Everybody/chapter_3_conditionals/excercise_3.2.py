# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. 
# The following shows two executions of the program:

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    overtime_limit = 40
    overtime_pay_rate = 1.5 
    if hours > overtime_limit:
        overtime = hours - overtime_limit 
        pay = (rate * overtime_limit) + (overtime*overtime_pay_rate*rate)
    else:
        pay = hours * rate
    print("Pay: ", pay)
except:
    print("Error, please enter numeric input")
# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

# sum = 0.0
# count = 0

# while True:

#   line = input('Enter a number: ')
#   if line == 'done':
#     break

#   try:
#     line = float(line)
#   except:
#     print("Invalid input")

#   sum += line
#   count += 1

# print(sum, count, sum/count)

# Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

sum = 0.0
count = 0
min = None
max = 0.0


while True:

  line = input('Enter a number: ')
  if line == 'done':
    break

  try:
    line = float(line)
  except:
    print("Invalid input")
    continue

  sum += line
  count += 1

  if(min is None):
    min = line
  if (min > line):
    min = line

  if (max < line):
    max = line


print(sum, count, min, max)

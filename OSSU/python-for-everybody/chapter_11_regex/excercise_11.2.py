# Exercise 2: Write a program to look for lines of the form:

# New Revision: 39772
# Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.

# Enter file:mbox.txt
# 38549

# Enter file:mbox-short.txt
# 39756

import re
fileName = open(input('Enter File: '))
regex = r'^New Revision: (\d+)'


def getRevisions(fileName, regex):
  revisionList = list()
  for line in fileName:
    line = line.rstrip()
    revisionList += re.findall(regex, line)
  return revisionList


def avgNum(numList):
  count, sum = 0, 0
  for num in numList:
    num = int(num)
    sum += num
    count += 1
  return int(sum/count)


print(avgNum(getRevisions(fileName, regex))) 
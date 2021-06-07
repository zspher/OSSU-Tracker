# Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.

# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195
# fname = input("Enter a file name: ")
# file = open(fname)
# emailHistogram = dict()
# for line in file:
#   if line.startswith("From "):
#     words = line.split()
#     word = words[1]
#     emailHistogram[word] = emailHistogram.get(word,0) + 1

# tupleList = list() 
# for email, count in list(emailHistogram.items()):
#   tupleList.append((count, email))
# tupleList.sort(reverse=True)
# count, email = tupleList[0]
# print(email, count)
# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
# fname = input("Enter a file name: ")
# file = open(fname)
# hourHistogram = dict()
# for line in file:
#   if line.startswith("From "):
#     words = line.split()
#     time = words[5]
#     time = time.split(':')
#     time = time[0]
#     hourHistogram[time] = hourHistogram.get(time,0) + 1

# hourHistogram = list(hourHistogram.items())
# hourHistogram.sort()
# for time, count in hourHistogram:
#   print(time, count)

# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
fname = input("Enter a file name: ")
file = open(fname)
histogram = dict()
for line in file:
  line = line.lower()
  for letter in line:
    if letter.isalpha():
      histogram[letter] = histogram.get(letter,0) + 1

sorted_keys = sorted(histogram, key=histogram.get, reverse=True)
sorted_histogram = dict()
for key in sorted_keys:
  sorted_histogram[key] = histogram[key]
  print(key, histogram[key])
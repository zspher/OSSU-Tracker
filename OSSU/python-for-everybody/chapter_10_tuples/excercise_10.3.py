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
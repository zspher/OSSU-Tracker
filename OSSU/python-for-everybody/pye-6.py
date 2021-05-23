# Exercise 5: Take the following Python code that stores a string:

text = "X-DSPAM-Confidence:    0.8475"
start = text.find(":")
end = text.find("5", start)
str = float(text[start+1:end+1])
print(str)

# Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.




# Exercise 6: Read the documentation of the string methods at https://docs.python.org/library/stdtypes.html#string-methods You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.

# The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is optional.

# x = 'From marquard@uct.ac.za'
# print(x[9])
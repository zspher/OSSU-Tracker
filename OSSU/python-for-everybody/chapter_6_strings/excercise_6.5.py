# Exercise 5: Take the following Python code that stores a string:

text = "X-DSPAM-Confidence:    0.8475"

# Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

start = text.find(":")
end = text.find("5", start)
str = float(text[start+1:end+1])
print(str)
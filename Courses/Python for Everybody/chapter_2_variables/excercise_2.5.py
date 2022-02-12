# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

print("|--Celsius to Fahrenheit Converter--|")
celsius = float(input("Celsius: "))
fahrenheit = (celsius * (9/5)) + 32
print("In Fahrenheit: ", fahrenheit)
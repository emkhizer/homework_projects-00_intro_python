# Write a program which prompts the user for a temperature in Fahrenheit
# (this can be a number with decimal places!) and outputs the temperature
# converted to Celsius.

# The Celsius scale is widely used to measure temperature, but places still
# use Fahrenheit. Fahrenheit is another unit for temperature, but the scale
# is different from Celsius -- for example, 0 degrees Celsius is 32 degrees
# Fahrenheit!

# The equation you should use for converting from Fahrenheit to Celsius is the
# following:

# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0


# User se Fahrenheit temperature input lena
degrees_fahrenheit = float(
    input("Enter temperature in Fahrenheit: "))  # Fahrenheit input lena
# `input()` function user se input leta hai aur `float()` function us input ko
#  decimal number mein convert karta hai.

# Fahrenheit ko Celsius mein convert karna
degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0  # Conversion formula
# Formula: Celsius = (Fahrenheit - 32) * 5 / 9

# Result ko print karna
print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")
# `f-string` ka use karke Fahrenheit aur Celsius values ko message ke sath 
# show kiya jata hai.

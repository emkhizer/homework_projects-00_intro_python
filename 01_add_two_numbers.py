# Write a Python program that takes two integer inputs from the user and
# calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

# The provided solution demonstrates a working implementation
# of this problem, where the main() function guides the user through
# the process of entering two numbers and displays their sum.


# `main` function define karein
def main():
    # User se pehla number input lena
    num1 = int(input("Enter the first number: "))  # Pehla number input lena
    # `input()` function user se input leta hai aur `int()` function us input ko integer mein convert karta hai.

    # User se dosra number input lena
    num2 = int(input("Enter the second number: "))  # Dosra number input lena
    # Yahan bhi `input()` aur `int()` ka use kiya gaya hai.

    # Dono numbers ka sum calculate karna
    total_sum = num1 + num2  # Sum = num1 + num2

    # Sum ko print karna
    print(f"The sum of {num1} and {num2} is: {total_sum}")
    # `f-string` ka use karke num1, num2, aur total_sum ko message ke sath show kiya jata hai.


# Agar ye file directly run ki gayi hai, to `main()` function call karein
if __name__ == "__main__":
    main()
    # `if __name__ == '__main__':` ye check karta hai ke kya file directly run ki gayi hai.
    # Agar haan, to `main()` function call hota hai.

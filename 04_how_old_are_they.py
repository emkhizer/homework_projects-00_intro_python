# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. 
# Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.


# `main` function define karein
def main():
    # Anton ki age
    anton: int = 21  # Anton ki age 21 saal hai
    # `anton` variable mein 21 store kiya gaya hai.

    # Beth ki age
    beth: int = 6 + anton  # Beth Anton se 6 saal badi hai
    # `beth` variable mein Anton ki age mein 6 add kiya gaya hai.

    # Chen ki age
    chen: int = 20 + beth  # Chen Beth se 20 saal bada hai
    # `chen` variable mein Beth ki age mein 20 add kiya gaya hai.

    # Drew ki age
    drew: int = chen + anton  # Drew ki age Chen aur Anton ki age ka sum hai
    # `drew` variable mein Chen aur Anton ki ages ka sum store kiya gaya hai.

    # Ethan ki age
    ethan: int = chen  # Ethan ki age Chen ke barabar hai
    # `ethan` variable mein Chen ki age copy ki gayi hai.

    # Sabhi friends ke names aur ages ko print karna
    print("Anton is " + str(anton))  # Anton ki age print karein
    print("Beth is " + str(beth))    # Beth ki age print karein
    print("Chen is " + str(chen))    # Chen ki age print karein
    print("Drew is " + str(drew))    # Drew ki age print karein
    print("Ethan is " + str(ethan))  # Ethan ki age print karein
    # `str()` function ka use karke numbers ko strings mein convert kiya gaya
    #  hai,takay unhe `print()` ke sath use kiya ja sake.


# Agar ye file directly run ki gayi hai, to `main()` function call karein
if __name__ == '__main__':
    main()
    # `if __name__ == '__main__':` ye check karta hai ke kya file directly run
    #  ki gayi hai.
    # Agar haan, to `main()` function call hota hai.

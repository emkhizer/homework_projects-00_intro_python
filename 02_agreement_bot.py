# Write a program which asks the user what their favorite animal is, and then 
# always responds with "My favorite animal is also ___!" (the blank should be 
# filled in with the user-inputted animal, of course).


# User se unke favorite animal ka input lena
favorite_animal = input("What is your favorite animal? ")  # User se input lena

# Response print karna
print(f"My favorite animal is also {favorite_animal}!")
# `f-string` ka use karke user ka input (`favorite_animal`) message mein
#  include kiya jata hai.
# Prompt the user to enter the lengths of each side of a triangle and 
# then calculate and print the perimeter of the triangle (the sum of 
# all of the side lengths).

# User se triangle ke teen sides ki lengths input lena
side1 = float(input("Enter the length of the first side: "))  # Pehla side
side2 = float(input("Enter the length of the second side: "))  # Dosra side
side3 = float(input("Enter the length of the third side: "))   # Teesra side

# Triangle ka perimeter calculate karna
perimeter = side1 + side2 + side3  # Perimeter teeno sides ka sum hota hai

# Perimeter ko print karna
print(f"The perimeter of the triangle is: {perimeter}")
# `f-string` ka use karke perimeter ko message ke sath show kiya jata hai.
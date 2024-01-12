import math
a = math.cos(30)
print(a)


# Week 1 Basic Activities
# 1. Write a Python program that takes the name of the user as an input and prints "Hello, user-name".
a = input("What is your name?")
print("Hello,", a)

#2. Write a Python program to determine the grade of a student in a course given his/her score using if,
# el-if and else statements. (70-100=A, 60-69=B, 50-59=C, 40-49=D, <40=F).
grade = int(input('Enter a grade: '))

if 70 <= grade <= 100:
    print('A')
elif 60 <= grade <= 69:
    print('B')
elif 50 <= grade <= 59:
    print('C')
elif 40 <= grade <= 49:
    print('D')
else:
    if grade <= 40:
        print('F')


#3. Modify the program in (2) to print the full meaning of each grade point as follows (A=Excellent, B=Very good, C=Good, D=Pass and F= Fail).


grade = int(input('Enter a grade: '))

if 70 <= grade <= 100:
    print('A = Excellent')
elif 60 <= grade <= 69:
    print('B = Very good')
elif 50 <= grade <= 59:
    print('C = Good')
elif 40 <= grade <= 49:
    print('D = Pass')
else:
    if grade <= 40:
        print('F = Fail')

#4. Write a program to print all even numbers between 1 and 100 using: while and for loop

# Using a while loop
num = 1
while num <= 100:
    if num % 2 == 0:
        print(num)
    num += 1

for num in range(1, 101):
    if num % 2 == 0:
        print(num)

# 5. Modify the program in (4) to store the even numbers in a list.

# Using a for loop to store even numbers in a list
even_numbers = []

for num in range(1, 101):
    if num % 2 == 0:
        even_numbers.append(num)

print("Even numbers between 1 and 100:", even_numbers)

# 6. Print the content of the list created in (5) using: while and for statements.

# Using a while loop to print the list
even_numbers = [num for num in range(1, 101) if num % 2 == 0]

index = 0
while index < len(even_numbers):
    print(even_numbers[index])
    index += 1


# Using a for loop to print the list
even_numbers = [num for num in range(1, 101) if num % 2 == 0]

for num in even_numbers:
    print(num)

#7. Extract the logic for printing the content of the list in (6) into a separate function. Call the function from your main method/function.

# In this version, the logic for printing the content of the list has been extracted into a separate function named print_even_numbers.
# The main function is responsible for creating the list of even numbers and then calling
# the print_even_numbers function to print its content.
# The if __name__ == "__main__": block ensures that the main function is executed when the script is run.

def print_even_numbers(even_numbers):
    for num in even_numbers:
        print(num)

def main():
    # Create a list of even numbers
    even_numbers = [num for num in range(1, 101) if num % 2 == 0]

    # Call the function to print the content of the list
    print_even_numbers(even_numbers)

# Call the main function
if __name__ == "__main__":
    main()

print('****************************')

# 8. Write a function that received 3 arguments. Adds up the first two arguments and store the result in the 3rd argument.
# Explore the concept of mutable and immutable types. Print the result of the addition inside the main method.

def add_and_store(arg1, arg2, result_container):
    # Check if the result container is mutable (a list in this case)
    if isinstance(result_container, list):
        # If mutable, update the first element with the sum of arg1 and arg2
        result_container[0] = arg1 + arg2
    else:
        # If not mutable, create a new variable to store the sum
        result_container = arg1 + arg2
    return result_container

def main():
    # Example with an immutable type (int)
    result_int = 0
    result_int = add_and_store(3, 5, result_int)
    print("Result with immutable type:", result_int)

    # Example with a mutable type (list)
    result_list = [0]
    add_and_store(3, 5, result_list)
    print("Result with mutable type:", result_list[0])

if __name__ == "__main__":
    main()

# 9. Write a program to create and print the content of a 2x2 matrix using for and while loop.

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()

def create_matrix():
    matrix = []
    for _ in range(2):
        row = []
        for _ in range(2):
            # You can modify this part to take input or generate values as needed
            element = int(input("Enter a number: "))
            row.append(element)
        matrix.append(row)
    return matrix

def main():
    # Create and print the matrix using a for loop
    print("Using for loop:")
    matrix_for = create_matrix()
    print_matrix(matrix_for)

    # Create and print the matrix using a while loop
    print("\nUsing while loop:")
    matrix_while = create_matrix()
    print_matrix(matrix_while)

if __name__ == "__main__":
    main()



# In this program:
#
# - The `create_matrix` function prompts the user to input values for each element of the matrix.
# - The `print_matrix` function is responsible for printing the matrix.
# - The `main` function demonstrates the creation and printing of the matrix using both `for` and `while` loops.


# 10 Write a program to perform matrix addition of 2 square matrices (use 2x2 matrices for simplicity)

def add_matrices(matrix1, matrix2):
    result_matrix = [[0, 0], [0, 0]]

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    return result_matrix

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()

def main():
    # Input for the first matrix
    matrix1 = []
    print("Enter elements for the first matrix:")
    for _ in range(2):
        row = [int(input("Enter element: ")) for _ in range(2)]
        matrix1.append(row)

    # Input for the second matrix
    matrix2 = []
    print("\nEnter elements for the second matrix:")
    for _ in range(2):
        row = [int(input("Enter element: ")) for _ in range(2)]
        matrix2.append(row)

    # Perform matrix addition
    result_matrix = add_matrices(matrix1, matrix2)

    # Display the result
    print("\nMatrix 1:")
    print_matrix(matrix1)

    print("\nMatrix 2:")
    print_matrix(matrix2)

    print("\nMatrix Addition Result:")
    print_matrix(result_matrix)

if __name__ == "__main__":
    main()

# This program defines a function add_matrices to perform matrix addition and a print_matrix function to display matrices.
# The main function takes user input for two matrices, performs matrix addition, and displays the original matrices along with the result.


"""
OBJECT ORIENTED PROGRAMMING

"""

#1. Create a class of type Vehicle with the following fields: name, make,
# price and function details that prints the properties separated by a comma.

class Vehicle:
    def __init__(self, name, make, price):
        self.name = name
        self.make = make
        self.price = price

    def display_details(self):
        details = f"{self.name}, {self.make}, £{self.price:,.2f}"
        print(details)

# Example usage:
if __name__ == "__main__":
    # Create an instance of the Vehicle class
    my_vehicle = Vehicle(name="Car123", make="BrandXYZ", price=25000.50)

    # Display the details using the class method
    my_vehicle.display_details()

# The Vehicle class has an __init__ method to initialize the object with the provided values for name, make, and price.
# There's a method named display_details that prints the properties of the vehicle separated by a comma.
# In the example usage section, an instance of the Vehicle class is created, and its display_details method is called to print the details.

#2. Alter the above class, make the fields private and create properties for accessing them.

class Vehicle:
    def __init__(self, name, make, price):
        self._name = name
        self._make = make
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def make(self):
        return self._make

    @property
    def price(self):
        return self._price

    def display_details(self):
        details = f"{self.name}, {self.make}, £{self.price:,.2f}"
        print(details)

# Example usage:
if __name__ == "__main__":
    # Create an instance of the Vehicle class
    my_vehicle = Vehicle(name="Car123", make="BrandXYZ", price=25000.50)

    # Access private fields through properties
    print("Name:", my_vehicle.name)
    print("Make:", my_vehicle.make)
    print("Price:", my_vehicle.price)

    # Display the details using the class method
    my_vehicle.display_details()

# The fields (_name, _make, and _price) are marked as private by convention (using a single leading underscore).
# Properties (name, make, and price) are defined with the @property decorator to provide read-only access to the private fields.

# 3.
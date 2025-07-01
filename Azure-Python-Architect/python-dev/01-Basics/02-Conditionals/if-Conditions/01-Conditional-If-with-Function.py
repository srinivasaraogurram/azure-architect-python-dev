import random

def check_age():
    age = input("Enter your age: ")
    if not age.strip():
        age = random.randint(1, 100)
        print(f"No age entered. Using random age: {age}")
    else:
        print(f"Entered Age is, {age}!")

    try:
        age = int(age)  # Convert input to integer
        if age > 18:
            print(f"User with age: {age} is an Adult")
        else:
            print(f"User with age: {age} is a Minor")
    except ValueError:
        print("Invalid input! Please enter a valid number for age.")


# Call the function
check_age()

def sum(a, b):
    """
    Function to calculate the sum of two numbers.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The sum of a and b.
    """
    return a + b    

# callin  sum
result = sum(10, 20)
print(f"The sum of 10 and 20 is: {result}")  # The sum of 10 and 20 is: 30
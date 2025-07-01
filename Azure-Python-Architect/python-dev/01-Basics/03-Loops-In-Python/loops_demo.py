"""
Python Loops Demonstration
This script showcases different types of loops in Python, each encapsulated in its own function.
Each function demonstrates a specific looping technique with practical examples.
"""

def basic_for_loop():
    """
    Demonstrates a basic for loop iterating through a list.
    This is Python's equivalent of a for-each loop in other languages.
    """
    fruits = ["apple", "banana", "cherry"]  # List of fruits to iterate through
    for fruit in fruits:  # Iterate over each item in the list
        print(f"I love {fruit}s!")  # f-string formats the output

def for_range_loop():
    """
    Shows how to use range() in a for loop.
    range() generates a sequence of numbers, commonly used for index-based iteration.
    """
    # range(5) generates numbers from 0 to 4 (5 is exclusive)
    for i in range(5):
        print(i)  # Prints 0 through 4

def enumerate_loop():
    """
    Demonstrates enumerate() which provides both index and value during iteration.
    Useful when you need the position of items in a sequence.
    """
    colors = ["red", "green", "blue"]
    # enumerate() returns (index, value) pairs
    for index, color in enumerate(colors):
        print(f"Color {index + 1}: {color}")  # Adding 1 to make index human-readable

def while_countdown():
    """
    Illustrates a while loop with a decreasing counter.
    The loop continues as long as the condition (count > 0) remains True.
    """
    count = 3  # Initialize counter
    while count > 0:  # Continue while this condition is True
        print(f"Countdown: {count}")
        count -= 1  # Decrement counter (same as count = count - 1)
    print("Blastoff!")  # Executes after loop completes

def while_with_break():
    """
    Shows a while loop with user input and break statement.
    break exits the loop immediately when triggered.
    """
    while True:  # Infinite loop until broken
        user_input = input("Type 'quit' to exit: ").lower()  # Get and lowercase input
        if user_input == "quit":
            print("Goodbye!")
            break  # Exit the loop
        print(f"You typed: {user_input}")

def nested_loops():
    """
    Demonstrates nested for loops.
    The inner loop completes all iterations for each iteration of the outer loop.
    """
    # Outer loop (rows)
    for i in range(1, 4):  # From 1 to 3
        # Inner loop (columns)
        for j in range(1, 4):
            print(f"{i} x {j} = {i * j}")  # Multiplication table entry
        print("---")  # Separator after each row

def dict_loop():
    """
    Shows how to iterate through a dictionary.
    .items() returns key-value pairs for iteration.
    """
    user = {"name": "Alice", "age": 30, "city": "Paris"}
    # .items() returns (key, value) pairs
    for key, value in user.items():
        print(f"{key}: {value}")  # Print each dictionary entry

def for_else_loop():
    """
    Demonstrates the for-else construct.
    The else block executes only if the loop completes without hitting a break.
    """
    numbers = [1, 3, 5]  # List with only odd numbers
    for num in numbers:
        if num % 2 == 0:  # Check if number is even
            print("Even number found!")
            break  # Exit if even found
    else:  # Executes only if no break occurred
        print("No even numbers found.")

def list_comprehension():
    """
    Shows list comprehension - a concise way to create lists.
    This example generates a list of squares.
    """
    # Create list of squares for numbers 0-4
    squares = [x**2 for x in range(5)]  # x**2 means x squared
    print(squares)

def main():
    """
    Main execution function that runs all demonstrations.
    Organized with clear section headers for output readability.
    """
    print("\n=== Python Loop Demonstrations ===\n")
    
    print("--- 1. Basic for loop ---")
    basic_for_loop()

    print("\n--- 2. for loop with range() ---")
    for_range_loop()

    print("\n--- 3. for loop with enumerate() ---")
    enumerate_loop()

    print("\n--- 4. while loop countdown ---")
    while_countdown()

    print("\n--- 5. while loop with break ---")
    print("Note: Interactive example commented out by default")
    # while_with_break()  # Uncomment to test interactive version

    print("\n--- 6. Nested for loops ---")
    nested_loops()

    print("\n--- 7. Dictionary iteration ---")
    dict_loop()

    print("\n--- 8. for-else construct ---")
    for_else_loop()

    print("\n--- 9. List comprehension ---")
    list_comprehension()

    print("\n=== Demonstrations Complete ===")

# Execute the main function when script is run directly
if __name__ == "__main__":
    main()
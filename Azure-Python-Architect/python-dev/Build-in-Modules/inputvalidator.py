def process_input(value):
    """
    Checks if the input is None, empty, only whitespace, or valid.
    Prints the result for each case.
    """
    if value is None:
        print("Input is None (null).")
    elif value == "":
        print("Input is an empty string.")
    elif not value.strip():
        print("Input is only whitespace.")
    else:
        print(f"Valid input: '{value}'")

# Example usage:
process_input(None)        # Input is None (null).
process_input("")          # Input is an empty string.
process_input("   ")       # Input is only whitespace.
process_input("hello")
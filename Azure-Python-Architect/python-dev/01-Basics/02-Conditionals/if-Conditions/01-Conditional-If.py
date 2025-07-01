age = input("Enter your age: ")
print(f"Entered Age is, {age}!")

age = int(age)  # Convert input to integer


if age > 18:
    print(f"user with age:{age} is Adult")
else:
    print(f"user with age:{age} is Minor")


# this is Single line comment
'''
this is a multi-line comment
it can span multiple lines
'''
# Variable declaration and initialization
# Variable names should be descriptive and follow naming conventions
name = "Sri"
print("name:", name);

age = 40
print("int: age:", age);


pi = 3.14159
print("decimal :", pi);

is_active = True
print("boolean isactive:", is_active);

# Type conversion
age_str = str(age)
print("My age is " + age_str)  # My age is 40

# Dynamic typing in Python
dynamic_var = "Hello"
print("Dynamic variable:", dynamic_var)
dynamic_var = 100  # Reassigning to an integer
print("Dynamic variable after reassignment:", dynamic_var)

# Show me how to convert int to string
num = 42
num_str = str(num)
print("Converted integer to string:", num_str)  # Converted integer to string: 42

# Show me how to convert float to string
float_num = 3.14
float_str = str(float_num)
print("Converted float to string:", float_str)  # Converted float to string: 3("Converted boolean to integer:", int_value)  # Converted boolean to integer: 1

# show me how to convert a boolean to a string
bool_value = False
bool_str = str(bool_value)
print("Converted boolean to string:", bool_str)  # Converted boolean to string: False


# Show me how to convert a string to an integer
num_str = "123"
num_int = int(num_str)
print("Converted string to integer:", num_int)  # Converted string to integer: 123


# Show float to integer conversion
# Note: This will truncate the decimal part

pi_str = "3.14159"
pi_int = int(float(pi_str)) 
print("Converted float float to integer:", pi_int)  # Converted float string to integer:

# Show me how to convert a float to an integer
float_num = 45.67
int_num = int(float_num)
print("Converted float to integer:", int_num)  # Converted float to integer: 45

# Show me how to convert an integer to a float
int_num = 10
float_num = float(int_num)
print("Converted integer to float:", float_num)  # Converted integer to float: 10

# Show me how to convert a boolean to an integer
bool_value = True
int_value = int(bool_value)
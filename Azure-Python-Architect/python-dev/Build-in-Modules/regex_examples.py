import re

# Example 1: Simple match
pattern = r"cat"
text = "A black cat sat on the mat."
print(f"Example 1 - Simple match: {re.search(pattern, text) is not None}")  # True if 'cat' is found

# Example 2: Using wildcards ('.' matches any character)
pattern = r"c.t"
print(f"Example 2 - Wildcard match: {re.search(pattern, 'cut') is not None}")  # True

# Example 3: Digit matching (\d matches any digit)
pattern = r"\d+"
text = "Order number: 12345"
print(f"Example 3 - Digit match: {re.search(pattern, text).group()}")  # '12345'

# Example 4: Extract all words starting with 'a' or 'A'
pattern = r"\b[Aa]\w+"
text = "An apple and an apricot are amazing."
print(f"Example 4 - Words starting with 'a' or 'A': {re.findall(pattern, text)}")

# Example 5: Replace all digits with '#'
pattern = r"\d"
text = "My phone number is 9876543210."
print(f"Example 5 - Replace digits: {re.sub(pattern, '#', text)}")

# Example 6: Validate an email address (simple pattern)
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
email = "user@example.com"
print(f"Example 6 - Email valid: {re.match(pattern, email) is not None}")
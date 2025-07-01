import sys

# Dictionary categorizing commonly used Python modules
modules_dict = {
    "Operating System": ['os', 'shutil', 'pathlib', 'glob', 'tempfile', 'fnmatch'],
    "System": ['sys', 'platform', 'getopt', 'argparse'],
    "Math & Numbers": ['math', 'decimal', 'fractions', 'random', 'statistics'],
    "Date & Time": ['datetime', 'time', 'calendar', 'zoneinfo'],
    "Data Types & Collections": ['collections', 'array', 'heapq', 'bisect', 'queue', 'types', 'enum', 'dataclasses'],
    "File & Directory": ['os.path', 'fileinput', 'filecmp', 'zipfile', 'tarfile', 'csv', 'configparser', 'pickle', 'shelve'],
    "Text Processing": ['re', 'string', 'textwrap', 'difflib', 'unicodedata', 'codecs'],
    "Internet & Networking": ['socket', 'http', 'urllib', 'ftplib', 'smtplib', 'imaplib', 'poplib', 'email'],
    "Concurrency": ['threading', 'multiprocessing', 'concurrent', 'asyncio', 'queue'],
    "Utilities": ['logging', 'traceback', 'warnings', 'pprint', 'copy', 'functools', 'itertools', 'operator'],
    "Testing": ['unittest', 'doctest', 'trace', 'timeit'],
    "Third-Party (for comparison)": ['numpy', 'pandas', 'requests', 'flask', 'django']
}

def is_builtin(module_name):
    """
    Check if a module is built-in or part of the standard library.
    Returns True if the module can be imported without pip install.
    """
    if module_name in sys.builtin_module_names:
        return True
    try:
        __import__(module_name)
        return True
    except ImportError:
        return False

# Print out each category and whether each module is built-in or not
for category, modules in modules_dict.items():
    print(f"\nCategory: {category}")
    for mod in modules:
        if is_builtin(mod):
            print(f"  '{mod}' is a built-in or standard library module.")
        else:
            print(f"  '{mod}' is NOT a built-in module. You may need to install it with pip.")

# Example usage of some built-in modules from different categories
import random, os, math, datetime, collections, re, socket, threading, logging, unittest

print("\n--- Example Usage ---")
# Generate a random integer between 1 and 10
print(f"Random int: {random.randint(1, 10)}")
# Print the current working directory
print(f"Current working directory: {os.getcwd()}")
# Calculate the square root of 16
print(f"Square root of 16: {math.sqrt(16)}")
# Print today's date
print(f"Current date: {datetime.date.today()}")
# Count the frequency of each character in 'hello world'
print(f"Counter example: {collections.Counter('hello world')}")
# Check if the string 'hello' matches the regex pattern 'h.llo'
print(f"Regex match: {re.match('h.llo', 'hello') is not None}")
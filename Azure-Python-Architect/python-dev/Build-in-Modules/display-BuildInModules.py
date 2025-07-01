import sys

def is_builtin(module_name):
    """Check if a module is built-in or part of the standard library."""
    if module_name in sys.builtin_module_names:
        return True
    try:
        __import__(module_name)
        return True
    except ImportError:
        return False

modules_to_check = ['random', 'os', 'math', 'json', 'numpy', 'requests']

for mod in modules_to_check:
    if is_builtin(mod):
        print(f"'{mod}' is a built-in or standard library module.")
    else:
        print(f"'{mod}' is NOT a built-in module. You may need to install it with pip.")

# Example usage of a built-in module
import random
print(f"Random number between 1 and 100: {random.randint(1, 100)}")
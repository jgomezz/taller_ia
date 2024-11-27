
"In Python, how can I handle exceptions to prevent my program from crashing when an error occurs?"

def safe_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    except TypeError:
        print("Error: Invalid input types!")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
print(safe_division(10, 2))  # Valid division
print(safe_division(10, 0))  # Division by zero
print(safe_division('10', 2))  # Type error
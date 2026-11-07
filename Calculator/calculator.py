"""
Simple Python Calculator
A command-line calculator supporting basic arithmetic operations.
"""

def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b

def divide(a: float, b: float) -> float:
    """Return the quotient of a and b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def modulus(a: float, b: float) -> float:
    """Return remainder of a divided by b."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero for modulus.")
    return a % b

def power(a: float, b: float) -> float:
    """Return a raised to the power of b."""
    return a ** b

def get_number(prompt: str) -> float:
    """Prompt user for a valid number with error handling."""
    while True:
        try:
            val = input(prompt).strip()
            return float(val)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def format_result(val: float) -> str:
    """Display integer values cleanly without trailing .0."""
    return f"{int(val)}" if val.is_integer() else f"{val:.4f}".rstrip('0').rstrip('.')

def main():
    print("=" * 40)
    print("        Simple Python Calculator        ")
    print("=" * 40)
    
    operations = {
        "1": ("Addition (+)", add, "+"),
        "2": ("Subtraction (-)", subtract, "-"),
        "3": ("Multiplication (*)", multiply, "*"),
        "4": ("Division (/)", divide, "/"),
        "5": ("Modulus (%)", modulus, "%"),
        "6": ("Power (**)", power, "^")
    }
    
    while True:
        print("\nSelect an operation:")
        for key, (label, _, _) in operations.items():
            print(f"  {key}. {label}")
        print("  7. Exit")
        
        choice = input("\nEnter choice (1-7): ").strip()
        
        if choice == "7":
            print("\nThank you for using Simple Calculator. Goodbye!")
            break
            
        if choice not in operations:
            print("Invalid selection. Please choose a number between 1 and 7.")
            continue
            
        label, func, symbol = operations[choice]
        print(f"\n-- {label} --")
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        try:
            result = func(num1, num2)
            print(f"\nResult: {format_result(num1)} {symbol} {format_result(num2)} = {format_result(result)}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

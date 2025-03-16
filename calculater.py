def calculator():
    try:
        num1, num2 = float(input("First number: ")), float(input("Second number: "))
        op = input("Operation (+, -, *, /): ")
        ops = {'+': num1 + num2, '-': num1 - num2, '*': num1 * num2, '/': num1 / num2 if num2 else 'Error: Division by zero'}
        print(f"Result: {ops.get(op, 'Invalid operation')}")
    except ValueError:
        print("Invalid input. Enter numbers only.")

if __name__ == "__main__":
    calculator()

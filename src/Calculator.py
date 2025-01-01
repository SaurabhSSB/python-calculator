
def calculate() -> None:
    """
    Performs basic arithmetic operations on two numbers.

    This function continuously prompts the user for two numbers and an operator, 
    performs the specified operation, and displays the result. 
    The user can choose to continue or exit the calculator.
    """
    while True:
        try:
            # Get user input with clear prompts
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            operator = input("Enter the operation (+, -, *, /, //, **, %): ")

            # Perform the calculation based on the operator
            match operator:
                case "+":
                    result = num1 + num2
                case "-":
                    result = num1 - num2
                case "*":
                    result = num1 * num2
                case "/":
                    if num2 == 0:
                        raise ZeroDivisionError("Cannot divide by zero")
                    result = num1 / num2
                case "//":
                    if num2 == 0:
                        raise ZeroDivisionError("Cannot divide by zero")
                    result = num1 // num2
                case "**":
                    result = num1 ** num2
                case "%":
                    if num2 == 0:
                        raise ZeroDivisionError("Cannot divide by zero")
                    result = num1 % num2
                case _:
                    raise ValueError("Please enter a valid operator")

            # Display the result
            print(f"The result of {operator} is: {result}")

            # Check if the user wants to continue
            repeat = input("Do you want to perform another calculation? (Y/N) ")
            if repeat.lower() != 'y':
                print("Exiting calculator.")
                break 

        except ValueError as e:
            print(f"Invalid input: {e}. Please enter valid numbers.")
        except ZeroDivisionError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculate()
    
mod = 50

def modulus_calculator():
    while True:
        print("\nModulus Calculator")
        print("Enter 'x' at any prompt to exit.")

        # Get inputs
        num1_input = input("Enter the first number: ")
        if num1_input.lower() == 'x':
            break

        num2_input = input("Enter the second number: ")
        if num2_input.lower() == 'x':
            break

        num3_input = mod

        try:
            # Convert inputs to floats
            num1 = float(num1_input)
            num2 = float(num2_input)
            num3 = float(num3_input)

            # Calculate product and modulus
            product = num1 * num2
            result = product % num3

            print(f"The result of ({num1} * {num2}) % {num3} is: {result}")

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except ValueError:
            print("Error: Please enter valid numbers.")


modulus_calculator()
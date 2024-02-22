def add_two_numbers(first_number, second_number):
    """
    Add two numbers together.
    """
    result = first_number + second_number
    return result

def subtract_two_numbers(first_number, second_number):
    """
    Subtract second number from the first number.
    """
    result = first_number - second_number
    return result

def multiply_two_numbers(first_number, second_number):
    """
    Multiply two numbers.
    """
    result = first_number * second_number
    return result

def divide_two_numbers(first_number, second_number):
    """
    Divide first number by the second number.
    """
    if second_number == 0:
        print("Error: Division by zero!")
        return None
    else:
        result = first_number / second_number
        return result


num1 = 10
num2 = 5

sum_result = add_two_numbers(num1, num2)
print(f"Sum of {num1} and {num2} is: {sum_result}")

difference_result = subtract_two_numbers(num1, num2)
print(f"Difference between {num1} and {num2} is: {difference_result}")

product_result = multiply_two_numbers(num1, num2)
print(f"Product of {num1} and {num2} is: {product_result}")

quotient_result = divide_two_numbers(num1, num2)
if quotient_result is not None:
    print(f"Quotient of {num1} divided by {num2} is: {quotient_result}")

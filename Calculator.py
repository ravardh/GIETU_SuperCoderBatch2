def calculator(p, q, oper):
    match oper:
        case "+":
            return p + q
        case "-":
            return p - q
        case "*":
            return p * q
        case "/":
            if q != 0:
                return p / q
            else:
                print("Error: Division by zero!")
                return None
        case "%":
            return p % q
        case _:
            print("Invalid Operator!")
            return None

p = int(input("Enter the first digit: "))
q = int(input("Enter the second digit: "))
oper = input("Enter the type of operation : ")

result = calculator(p, q, oper)
if result is not None:
    print("Your answer is:", result)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    try:
        num = int(input("Enter a non-negative integer to calculate its factorial: "))
        if num < 0:
            print("Please enter a non-negative integer.")
        else:
            print("Factorial of", num, "is", factorial(num))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

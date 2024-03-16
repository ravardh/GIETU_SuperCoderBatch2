def print_hollow_square(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
size = int(input("Enter the size of the square: "))
print_hollow_square(size)
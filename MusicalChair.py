def find_winner(N, K):
    chairs = list(range(1, N + 1))
    current_position = 0
    while len(chairs) > 1:
        current_position = (current_position + K - 1) % len(chairs)
        chairs.pop(current_position)
    return chairs[0]
def main():
    N = int(input("Enter the number of children: "))
    K = int(input("Enter the counting interval: "))
    winner = find_winner(N, K)
    print("The winner is child", winner)
if __name__ == "__main__":
    main()
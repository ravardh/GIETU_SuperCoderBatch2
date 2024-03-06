if __name__ == '__main__':  # Greedy approach
    items: list = [0, 1, 2, 3, 4, 5, 6]
    price: list = [10, 5, 15, 7, 6, 18, 3]
    weight: list = [2, 3, 5, 7, 1, 4, 1]
    capacity: int = 15
    values: list = []
    for i in range(len(items)):
        values.append(price[i] / weight[i])

    # print(items)
    # print(values)

    # bubble sort
    for i in range(len(values)):
        for j in range(len(values) - i - 1):
            if values[j] < values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                items[j], items[j + 1] = items[j + 1], items[j]

    # print(items)
    # print(values)

    selectedItems: list = []
    profit: int = 0
    totalWeight: int = 0

    i: int = 0
    while totalWeight + weight[items[i]] <= capacity:
        selectedItems.append(items[i])
        profit += price[items[i]]
        totalWeight += weight[items[i]]
        i += 1

    print(selectedItems)
    print(profit)
    print(totalWeight)

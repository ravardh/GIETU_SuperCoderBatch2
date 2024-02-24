if __name__ == '__main__':
    arr: list = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
    k: int = int(input('enter k '))

    max_element: int = 0
    second_max_element: int = 0
    for i in range(k):
        if arr[i] > second_max_element:
            if arr[i] > max_element:
                max_element = arr[i]
            else:
                second_max_element = arr[i]

    for i in range(len(arr) - k):
        if arr[i] == max_element:
            max_element = second_max_element
        elif arr[i]==second_max_element:
            pass
            

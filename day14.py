# Longest Subarray

def divide(st: int, end: int, length: list, arr: list,count:list):
    if end == len(arr) or st == len(arr) or st >= end:
        return


    divide(st, end + 1, length, arr,count)
    divide(st + 1, end, length, arr,count)


if __name__ == '__main__':
    arr: list = [9, -3, 3, -1, 6, -5]
    length: list = [0]
    count:list=[0]
    divide(0, 1, length, arr,count)
    print(count)
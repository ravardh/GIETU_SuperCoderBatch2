if __name__ == '__main__':
    string: str = 'ABCBBACBAABACBABC'
    pattern: str = 'CBA'

    for i in range(len(string) - len(pattern)):
        if string[i] == 'C':
            if string[i + 1] == 'B':
                if string[i + 2] == 'A':
                    print(i)

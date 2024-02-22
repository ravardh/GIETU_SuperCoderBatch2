if __name__ == '__main__':
    option: str = ''

    while option != 'e':
        option: str = input('enter option ')
        if option != 'e':
            x: int = int(input('enter a '))
            y: int = int(input('enter b '))
        match option:
            case '+':
                print(x, ' + ', y, ' = ', x + y)
            case '-':
                print(x, ' - ', y, ' = ', x - y)
            case '*':
                print(x, ' * ', y, ' = ', x * y)
            case '/':
                print(x, ' / ', y, ' = ', x // y)

            case 'e':
                print('Exited')
            case '_':
                print('Invalid input')

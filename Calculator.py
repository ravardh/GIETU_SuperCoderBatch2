def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a *b 
def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Tera jivan me koi deekha hai zero se devide karte hue , hatt"

def calculator():
    while True:
        print("Wass Calculator to hai , itna Vaoo Kyun Kha raha hai")
        print("1. Aree Addition karna :!!")
        print("2. hann abhi  tu Subtract kar:")
        print("3.  tere se nahi hopayega ye Multiply")
        print("4. Tu jake KOne me kar Divide")
        print("5. Nikal ja yanhha see ,  I said Get Out")

        choice = input("Hann Chall Uthha yanhe kuchh (1|2|3|4|5): ")

        if choice == '5':
            print("Kya Dala Hai re Tu , Hatto Wanha se Hato ! Tera.....!! (-^_^-)!")
            break

        num1 = float(input("Arre Dal Na Pehla Number: "))
        num2 = float(input("Abee Dal na number , kitna Bar bataun Number Dalne ke liye : "))

        match choice:
            case '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            case '2':
                print(f"{num1} - {num2} = {sub(num1, num2)}")
            case '3':
                print(f"{num1} * {num2} = {mult(num1, num2)}")
            case '4':
                result = div(num1, num2)
                print(f"{num1} / {num2} = {result}")
            case '5':
                print("Jaldi Wahan se hattoo , tera ......!! (-^_^-)")
                break
            case _:
                print("Kya Dala Hai re Tu !! (-^_^-)")

if __name__ == "__main__":
    calculator()

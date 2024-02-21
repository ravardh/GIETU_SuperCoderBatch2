
Calculate=True
while(Calculate):
    a = int(input("Enter the First Number: "))
    op = input("Enter the operator: ")
    b = int(input("Enter the  Second Number: "))
    match op:
        case '+':
            ans=a+b
            print(f"{a} + {b} = {ans}")
            c=int(input("Press 1 To continue operation otherwise Press 0 :"))
            if(c==0):
                Calculate=False
                
        case '-':
            ans = a - b
            print(f"{a} - {b} = {ans}")
            c=int(input("Press 1 To continue operation otherwise Press 0 :"))
            if(c==0):
                Calculate=False
        case '*':
            ans = a * b
            print(f"{a} * {b} = {ans}")
            c=int(input("Press 1 To continue operation otherwise Press 0 :"))
            if(c==0):
                Calculate=False            
        case '/':
            if b != 0:
                ans = a / b
                print(f"{a} / {b} = {ans}")
            else:
                print("Error! Can not divisible by 0")
            c=int(input("Press 1 To continue operation otherwise Press 0 :"))
            if(c==0):
                Calculate=False
        case '%':
            if b != 0:
                ans = a % b
                print(f"{a} % {b} = {ans}")
            else:
                print("Error! Can not divisible by 0")
            c=int(input("Press 1 To Continue operation Otherwise Press 0 :"))
            if(c==0):
                Calculate=False
        case '**':
                ans = a ** b
                print(f"{a} to the Power {b} = {ans}")
                c=int(input("Press 1 To continue operation otherwise Press 0 :"))
                if(c==0):
                    Calculate=False
        case _:
            print("! Enter Valid Input")
           

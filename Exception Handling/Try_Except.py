dict={1:"Aditya",2:"Santoshi",3:"Adi"}
try:
    print(dict[5])
except:
    print("Exception Generated ! invalid Key")
else:
    print("Valid Key")
finally:
    print("Code executed Successfully")
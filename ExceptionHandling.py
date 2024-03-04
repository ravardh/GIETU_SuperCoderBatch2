d={1:"abc",2:"def",3:"xyz"}
print(d)
try:
    print(d[2])
except:
    print("Invalid key")
else:
    print("Valid key")
finally:
    print("code executed sucessfully")
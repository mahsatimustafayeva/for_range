a=int(input("Eded daxil edin: "))
if a<0:
    print("Menfi ededin faktoriali yoxdur!")
else:
    x=1
    for i in range(1,a+1):
        x=x*i
    print(x)
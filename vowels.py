saitler="a,e,ə,ı,i,o,ö,u,ü,A,E,Ə,İ,I,O,Ö,U,Ü"
metn=input("Metni daxil edin: ")
a=0
for i in metn:
    if i in saitler:
        a+=1
print("Metndeki saitlerin sayi:", a)
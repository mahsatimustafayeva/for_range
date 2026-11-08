a=input("Sifreni daxil edin: ")
boyuk=0
kicik=0
reqem=0
diger=0
for simvol in a:
    if simvol.isupper():
        boyuk+=1
    elif simvol.islower():
        kicik+=1
    elif simvol.isdigit():
        reqem+=1
    else:
        diger+=1

print("Boyuk herf:",boyuk)
print("Kicik herf:",kicik)
print("Reqem:", reqem)
print("Diger simvol:", diger)
if len(a)>8 and boyuk>0 and kicik>0 and reqem>0 and diger>0:
    print("Sifre gucludur")
else:
    print("Sifre guclu deyil")


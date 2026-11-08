temperatures = [-3, 2, 8, 15, 22, 27, 31]
gun=1
for i in temperatures:
    if i<0:
        hava="Saxta" 
    elif i<=10:
        hava="Soyuq"
    elif i<20:
        hava="Mulayim"
    elif i<30:
        hava="Isti"
    else:
        hava="Cox isti"
    print(f"{gun}-ci gun: {i}° → {hava}")
    gun+=1
students = [("Aysel", 95), ("Murad", 72), ("Leyla", 84), ("Elvin", 48), ("Nigar", 63)]
for ad,bal in students:
    if bal >=91:
        qiymet="A"
    elif bal >=81:
        qiymet="B"
    elif bal >=71:
        qiymet="C"
    elif bal>=61:
        qiymet="D"
    elif bal>=51:
        qiymet="E"
    else:
        qiymet="F"
    print(f"{ad}: {bal} → {qiymet}")
    
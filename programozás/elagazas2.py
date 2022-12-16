osztalyzat = int(input("Kérem az osztályzatot"))
print(osztalyzat)

if osztalyzat == 1:
    print("elégtelen")
elif osztalyzat == 2:
    print("elégséges")
elif osztalyzat == 3:
    print("közepes")
elif osztalyzat == 4:
    print("jó")
elif osztalyzat == 5:
    print("jeles")
else: 
    print("Nem jó számot adtál meg!")

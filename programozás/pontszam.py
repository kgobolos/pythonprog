pont = int(input("Kérem a pontszámot!"))

if pont < 50:
    print("1")
elif pont >= 50 and pont < 60:
    print("2")
elif pont >= 60 and pont < 70:
    print("3")
elif pont >= 70 and pont < 85:
    print("4")
elif pont >= 85:
    print("5")
else:
    print("Nem jó számot adtál meg")
# szoveg = "ezegyszöveg"
# if "v" in szoveg:
#     print("benne van")
# else: print("nincs benne")

# szoveg = "ezegyszöveg"
# beker = input("Kérem a betűt! ")
# if beker in szoveg:
#     print(f"{beker} betű benne van a szövegben")
# else: print(f"{beker} betű nincs a szövegben")

# szoveg = "KEDD"
# print(szoveg.lower())


hetnapjai = ["Hétfő","Kedd","Szerda","Csütörtök","Péntek","Szombat","Vasárnap"]
# hetnapjai.lower()
# print(hetnapjai)
# for i in range(len(hetnapjai)):
#     hetnapjai[i] = hetnapjai[i].lower()
hetnapjai_kisbetu = [item.lower() for item in hetnapjai]
hetnapjai_nagybetu = [item.upper() for item in hetnapjai]

beker = input("Kérem a napot! ").upper()

if beker in hetnapjai_nagybetu:
    print(f"{beker} nap benne van a listában")
else:
    print(f"{beker} nap nincs a listában")



lista = [] #üres lista

# lista.append()
lista.append("Fifa")
lista.append("Fortnite")
lista.append("COD")
lista.append("GTA")
lista.append("PUBG")

#kiiratas 3 féle képpen
#1.
print(lista)
print("***************************")
#2.
for item in lista:
    print(item)

print("***************************")
#3.
#len függvény a lista hossza (hány elemet tartalmaz)
for i in range(len(lista)):
    print(lista[i])
print("**********************")
#szűrés (lecserélés) 
for item in lista:
    if item == "COD":
        print("IGEN")
    else:
        print("NO")









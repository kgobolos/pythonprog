lista =[20,12,101,23,76,44,89,102]
print(lista)
print("**************************")
# lista.sort()sorbarendezés növekvő sorrend
lista.sort(reverse=True) #sorbarendezés csökkenő sorrend
print(lista)
print("**************************")
print(max(lista))
print("**************************")
print(min(lista))
print("**************************")
print(sum(lista))

print("**************************")
#Feladat összeszorozni a számokat!
szorzat = 1
for i in range(len(lista)):
    szorzat = szorzat * lista[i]
print(szorzat)






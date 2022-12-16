# Kör területe: r^2*PI
# print(math.pi)
import math
d = int(input("Kérem a kör átmérőjét: "))
r = d/2 
#T = r**2*math.pi
pi = math.pi
T = math.pow(r,2)*pi
x = round(T,3)
print(f"A kör területe: {x}")

K = 2 * r * pi
y = round(K, 2)

print(f"A kör kerülete: {y}")

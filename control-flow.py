# EJEMPLO 1: Determinar si una persona puede ver una
# película considerando su edad y el rating
print("#1: RATING PELÍCULAS")
age = int(input("Edad del cliente => "))
rating = input("Rating de la película => ")
if age > 17:
    print("Cliente apto para ver la película")
elif rating == 'R':
    print("Cliente NO apto para ver la película")

# EJEMPLO 2: Determinar si un número es par o impar
print("\n#2: NÚMERO PAR O IMPAR")
num = int(input("Ingrese un número => "))
if num%2 == 0:
    print(f"El {num} es un número par")
else:
    print(f"El {num} es un número impar")   

# EJEMPLO 3: Determinar si una división de enteros
# da un decimal como resultado
print("\n#3: DIVISÓN DA ENTERO O DECIMAL")
num = int(input("Ingrese el primer entero => "))
num2 = int(input("Ingrese el segundo entero => "))
res = num/num2
print(f"{num}/{num2} = {res}")
if res == int(res):
    print("La divisón resulta en un entero")
else:
    print("La división resulta en un decimal")


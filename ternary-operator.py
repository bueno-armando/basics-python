# EJEMPLO 1: obtener el mayor entre dos
# enteros
print("#1: Mayor entre dos enteros")
a = int(input("Entero 1 => "))
b = int(input("Entero 2 => "))
if a == b:
    print("Los dos son iguales")
else:
    print(f"{a} es mayor") if a > b else print(f"{b} es mayor")

# EJEMPLO 2: determinar si un entero es divisible
# entre 3
print("\n#2: Divisible entre 3")
a = int(input("Ingrese un entero => "))
print("Divisible entre 3") if a%3 == 0 else print("No Divisible entre 3")

# EJEMPLO 3: determinar si un entero es
# positivo o negativo
print("\n#3: Positivo o negativo")
a = int(input("Ingrese un entero => "))
print("Positivo") if a > -1 else print("Negativo")

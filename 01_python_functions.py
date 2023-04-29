# EJEMPLO 1: Mensaje de bienvenida al usuario
print("#1: BIENVENIDA AL USUARIO")
def welcome_user(usr_name):
    print(f"Bienvenido, {usr_name}!")
name = input("Nombre de usuario => ")
welcome_user(name)

# EJEMPLO 2: Definir si el usuario es mayor de edad
print("\n#2: ES MAYOR DE EDAD")
def isAdult(age):
    if age >= 18:
        return True
    else:
        return False
age = int(input("Ingrese edad del usuario => "))
print("Es mayor de edad") if isAdult(age) else print("Es menor de edad")

# EJEMPLO 3: Número elevado a una potencia
def potencia(a,b):
    res = a
    for i in range(b):
        res *= a
    return res
print("\n#3: NÚMERO ELEVADO A UNA POTENCIA")
a = int(input("Ingrese el número => "))
b = int(input("Ingrese la potencia => "))
print(f"{a}^{b} = {potencia(a,b)}")
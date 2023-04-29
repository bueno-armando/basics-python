# EJEMPLO 1: Mostrar números del 1 al 10
print("#1 NÚMEROS DEL 1 AL 10")
n = 1
while n <= 10:
    print(n, end=" ")
    n += 1
print("\n")

# EJEMPLO 2: Ingresar enteros hasta que la suma
# alcanze 50
print("#2: ENTEROS HASTA QUE LA SUMA ALCANZE 10")
sum = 0
while sum < 10:
    n = int(input("Ingrese un entero  => "))
    sum += n
    print("Suma:",sum)

# EJEMPLO 3: Mostrar serie fibonacci hasta número dado
print("\n#3: SERIE FIBONACCI HASTA QUE ALCANZE N")
n = int(input("Ingrese el alcance de la serie (n) => "))
fibo = 0
a = 1
b = 0
while fibo < n:
    fibo = a+b
    a = b
    b = fibo
    print(fibo, end=" ")
print()
# 1: Imprimr nombre completo
print("------#1: Nombre completo------")
def print_name(name1='', name2='', last_name1='', last_name2=''):
    print("Tu nombre completo es:")
    print(name1, name2, last_name1, last_name2)
print_name(name1="Armando", last_name1="Casas")
print_name(name1="Julio", name2="Juan", last_name1="Casas", last_name2="Terrazas")

# 2: Precio con IVA
print("\n------#2: Precio con IVA------")
def price(base, desc=-1):
    if desc == -1:
        print("Descuento no provisto, abortando")
    else:
        print(f"Precio con descuento: {base - base*(desc/100)}")
price(desc=20, base=100)
price(base=200, desc=30)

# 3: Número elevado a una potencia
print("\n------#3: Número elevado a una potencia------")
def potencia(num, pot):
    res = num
    for i in range(pot):
        res *= num
    print(f"{num}^{pot} = {res}")
potencia(pot=5, num=2)
potencia(num=3, pot=4)


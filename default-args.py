#EJEMPLO 1: Crear cuenta de usuario
print("------#1: Crear cuenta de usuario------")
def crear_cuenta(username, password="123abc"):
    print("Datos de la cuenta:")
    print(f"Nombre de usuario: {username}")
    print(f"Contraseña: {password}")
    if password == '123abc':
        print("Contraseña default, recomendado cambiarla!")
    print()
crear_cuenta("Julio Jacinto")
crear_cuenta("Rey Reyes", "03msktr!")


#EJEMPLO 2: Bienvenida a usuario
print("\n------#2: Bienvenida a usuario------")
def bienvenida(usr_name="nuevo usuario"):
    print(f"Bienvenido, {usr_name}!")
bienvenida()
bienvenida("Armando Casas")

#EJEMPLO 3: Realizar una transaccion
print("\n------#3: Transacción------")
def transaction(amount=0, reason="general"):
    if amount == 0:
        print("Cantidad no provista, abortando")
    else:
        print(f"Transacción exitosa de {amount}, motivo: {reason}")
transaction()
transaction(101)
transaction(222, "Aporte fiesta gerencial")
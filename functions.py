def hello_world():
    print("Hello World!")

def hello_world_name(first_name = "NoName"):
    print(f"Hello, {first_name}!")

# *args: se puede mandar cualquier cantidad de variables
def hello_world_args(*args):
    name_0 = args[0]
    name_1 = args[1]
    name_2 = args[2]

    print(args)
    print(type(args))
    print(f"Hello all: {name_0}, {name_1}, {name_2}!")

# se le está dando una llave (key) a los argumentos
def hello_world_keyword_args(person_1, person_2):
    print(f"Hello all: {person_1}, {person_2}")

# keywords sin darle nombre a las keys
def hello_world_arbitrary_keyword_args(**kwargs):
    print(kwargs)
    if not 'person_2' in kwargs.values():
        print("No hay segunda persona")
    else:
        print(f"Hello {kwargs['person_1']} / {kwargs['person_2']}")

    print(kwargs)
    print(type(kwargs))

#hello_world()
#hello_world_name("Armando")
#hello_world_name("Esme")
#hello_world_args("Armando", "César", "Rodrigo")
#hello_world_keyword_args("Armando", "Rodrigo")
#hello_world_arbitrary_keyword_args(person_1="Armando", person_2="Rodrigo")
hello_world_arbitrary_keyword_args(person_1="Armando")
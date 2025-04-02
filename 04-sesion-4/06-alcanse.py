saludo = "Hola Mundo"

def saludar():
    global saludo
    saludo = "Adios Mundo"
    # print(saludo)

print(saludo)
saludar()
print(saludo)


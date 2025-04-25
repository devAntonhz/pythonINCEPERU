#
# ? BUCLE: FOR
# * SYNTAX

# for var in iterable:
#     sentencia

# ? RANGE CON FOR

for numero in range(5):
    print(numero + 1)

# TODO: Imprime los NUMERO DEL 50 al 70 pero solo los POSITIVO O NUMEROS PARES en el BUCLE FOR en PYTHON

# for numero in range(50, 71):
#     if numero % 2 == 0:
#         print(numero)

# ? FOR CON STRING

# nombre = "Maria"

# for nombre_usuario in nombre:
#     print(nombre_usuario)

# ? ::::: EJERCICIO ::::::: Contador de VOCALES

texto = input("Digita un texto: ")
vocales = "aeiouAEIOU"
contador = 0

for letra in texto:
    if letra.lower() in vocales:
        contador += 1

print("Numero de vocales contadas:", contador)

# TODO: CREA UN PROGRAMA QUE CONTABILIZE CUANTAS "A" EXISTE EN ESA PALABRA

texto = input("Digite una palabra: ")
contador = 0

for letra in texto:
    if letra == "a":
        contador += 1

sumatoria = 0

for x in range(1, 6):
    sumatoria += x

print("La suma entre el 1 y el 100 es:", sumatoria)

for i in range(5, 0, -1):
    print(i)

print("GO..!!!")

# ? FOR CON LISTAS

frutas = ["Pera", "Uva", "Platano", "Manzana"]

for fruta in frutas:
    print(fruta)
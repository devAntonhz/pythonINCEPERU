# #
# # ? LISTAS

# frutas = ["pera", "Manzana", "Uva"]
# print(frutas)

# datos_usuario = ["Juan", "Sanzhes", 30, True, 2053.54]
# print(datos_usuario)

# def dato():
#     return dato

# usarios_jorge = ["Jorge", 15145, dato()]
# print(usarios_jorge)

# numeros = list(range(1, 6))
# print(numeros)

# saludar = list("Hola Mundo")
# print(saludar)

# print(type(saludar))

# # ? LIstas respetan el orden

# cadenas_1 = ["t1", "t2", "t3"]
# cadenas_2 = ["t1", "t2", "t3"]
# cadenas_3 = cadenas_2

# print(cadenas_1 == cadenas_2) # COMPRACION
# print(cadenas_1 is cadenas_2)
# print(cadenas_2 is cadenas_3)
# print("t1" in cadenas_1)
# # print(["t1"] in cadenas_1) # SOlo si existe una sublista

# # ? ACCEDER A SUS VALORES ( Indexacion, Slacing, Stride )
# lista = [1, 2, 3, 5, 6, "Maria"]
# print(lista[2])
# print(lista[-1])

# print(lista[3:5])
# print(lista[-2:])

# print(lista[1::2])

# TODO: CREA UN FUNCION LLAMADA cuentaregresiva(), que reciba un numero entero positivo y muestra una cuenta regresiva desde el valor 20 hasta 1, y que al funal cree un mensaje que imprima el nombre del usuario y le diga, Aprendiendo PYTHON

# TODO: Crea una funcion que calisifique el numero que recibe, un entero y devuelva una cadena indicando si el numero es positivo, o si es negativo, o tambien sea 0

# lista = [1, 2, 3, 5, 6, "Maria"]
# reversa = lista[::-1]
# print(reversa)

# # ? REFERENCIA A UN STRING
# saludo = "Hola INCEPERU"
# text = "Hola INCEPERU"

# print(text[:] is saludo[:])

# lista = [1, 2, 3, 4, 5]
# print(lista[:] is lista)

# # ? OPERADORES CON LISTAS

# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]

# print(lista1 + lista2)
# print(lista1 * 3)
# print(len(lista1))
# print(min(lista1))
# print(max(lista1))

# # AGREGANDO DE FORMA DIRECTA
# print([10, 11, 12] + [400])

# # ? LISTAS ANINDADAS
# # lista = [[1, 2], [3, 4], [5, 6]]
# lista = [1, [2, [3, 4], 5], 6]
# print(lista)
# print(lista[1][1][1])

# # ? LISTAS MUTABLES (CAMBIA EL VALOR)
# series = ["Naruto", "DBZ", "Pokemon", "Digimon", "Los Simpson"]

# # CAMIADO EL VALOR DEL ELEMETO
# series[1] = "DBGT"
# print(series)

# # ELIMINADO
# del series[2]
# print(series)

# del series[1:3]
# print(series)

# # AGREGAR VALORES
# series += ["Wolfe", "Vampiros"]
# print(series)

# # SUSTITUCION
# series[2:4] = [1, 2, 3]
# print(series)

# # ? METODOS DE UNA LISTA
# lista_numeros = [1, 2, 3, 4, 5]

# lista_numeros.append(6)  # AGREGA UN VALOR AL FINAL DE LA LISTA
# lista_numeros.extend([7, 8])
# lista_numeros.insert(2, "Juan")  # Desde un elemento en posicion x
# lista_numeros.insert(0, "Maria")
# lista_numeros.remove(5)  # ELIMINA ELEMENTOS DE UNA LISTA DESDE SU NOMBRE DE ELEMENTO
# lista_numeros.pop(3)  # ELIMINA ELEMENTOS DE UNA LISTA DESDE SU INDEXACION
# # lista_numeros.clear() # ELEIMINA LOS ELEMENTOS DE MI LISTA
# print(lista_numeros)
# index = lista_numeros.index("Maria")
# lista_numeros.extend([8, 2])
# print(lista_numeros)
# cuenta = lista_numeros.count(4)
# print(cuenta)
# copia = lista_numeros.copy()
# print(copia)
# lista_numeros.reverse()
# print(lista_numeros)
# numeros = [1, 4, 2, 100, 500, 20, 1000]
# # numeros = sorted(numeros)
# numeros = sorted(numeros, reverse=True)
# print(numeros)
usuarios = [[3, "Jose"], [1, "Maria"], [2, "Juana"]]


usuarios = [["Jose", 3], ["Maria", 1], ["Ana", 2]]
usuarios.sort()

usuarios.sort(key=lambda var: var[1])
print(usuarios)

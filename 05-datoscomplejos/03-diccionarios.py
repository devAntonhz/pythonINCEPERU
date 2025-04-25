# # 
# # ? SYNTAXIS
# # var = {key1: valor1, key2: valor2,....., keyn: valorn}

# usuario = {"Nombre": "Pepito", "Apellido": "Sanchez"}
# print(type(usuario))
# print(usuario)

# print(usuario["Apellido"])

# dic = {
#     1: "uno", 
#     2: "dos", 
#     3: "tres",
#     "uno": 1,


# }

# print(dic["uno"])

# dic = {
#     ("uno", 1): "UNO",
#     ("dos", 2): "DOS"
# }

# print(dic[("dos", 2)])

# usuario = {
#     "Nombre": "Jorge",
#     "Apellido": "Macanao",
#     "Pais": "Perú",
#     "Ciudad": "Iquitos"
# }
# usuario["Nombre"] = "Pedro"

# # MODIFACAR VALORES
# print(usuario)

# # AGREGAR VALORES A MI DICTIONARY
# usuario["Telefono"] = 999999999
# print(usuario)

# dic = {
#     "num": 20,
#     "str": "Hola Mundo",
#     "lista": [1, 2, 3],
#     "tupla": (1, 2, 3, 4),
#     "dict": {"key1": "valor1", "key2": "valor2", 3: True}
# }

# print(dic["lista"][0])
# print(dic["dict"][3])

# dic = {
#     "key": 2,
#     "key": 3,
#     "key": 1
# }

# print(dic["key"])

# ? OPERADORES QUE VIMOS

dic1 = {
    "key1": 1,
    "key2": 2,
}

dic2 = {
    "key3": 3,
    "key4": 4,
}

print(dic1 is dic2)
print(dic1 == dic2)
print(dic1 + dic2)
print(dic1 * 2)

# 
# # ? SENTENCIAS IF - ELSE DE UNA SOLA LINEA:
# if 40 > 10: print("Sentencia Valida"); print("Fin de la sentencia....")

# if 40 < 10: print("Si es mayor")
# elif 40 > 30: print("Si es mayor de 30")
# else: print("no es mayor")

# ? OPERADOR TERNARIO

# nombre = input("Digite un nombre: ")

# if nombre == "ana":
#     # print("Adivinaste")
#     mensaje = "Adivinaste"
# else:
#     # print("No Adivinaste")    
#     mensaje = "No Adivinaste"

# nombre = input("Digite un nombre: ")

# mensaje = "Adivinaste" if nombre == "ana" else "No Adivinaste"

# print(mensaje)

# nombre = input("Digite su nombre: ")

# edad = 30 if nombre.lower() == "ana" else 15
# print("Su edad es:", edad)

# ? ENCADEAMIENTO DE OPERADORES

edad  = 25

# if edad >= 15 and edad <= 65:
#     print("Pueden bañarse en la piscina")

if 15 <= edad <= 65:
    print("Pueden bañarse en la piscina")
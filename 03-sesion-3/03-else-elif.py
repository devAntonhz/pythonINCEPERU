edad = -50

# ? CLAUSULA ELSE
# if edad >= 18:
#     print("Puedes ver la pelicula")
# else:
#     print("Es menor de edad edad")


# # ? CLAUSUAL ELIF
# if edad >= 18:
#     print("Puedes ver la pelicula")
# elif edad >= 14:
#     print("Necesita el permiso de los padres")
# elif edad < 0:
#     print("Edad erronea")
# else:
#     print("No puede ver la pelicula")

nombre = input("Digite un nombre de mujer que empiece con \"A\": ")

# ? ANIDACION DE IF
if nombre.upper() == "ANA":
    print("Adivinaste el nombre, ahora....")

    fiesta = input("Adivina en que distrito queda la fiesta: ")
    if fiesta.lower() == "callao":
        print("Advinistas, eres bienvenida(0) a la fiesta")
    else:
        print("Fallaste, no eres benvenido(a) a la fiesta")
else:
    print("Error fallaste en el nombre...")

# ! TODO: TAREA: CREA EL FAMOSO JUEGO DE PIEDRA PAPEL O TIJERA, ENTRE 2 JUGADORES, con opeardor comparacion (==) | PRO si usas > y <.




# var = ("Hola", "Juana", 20)
# print(type(var))

# var = ("Hola", "Juana", 20) + ("Maria", 200, True, "jorge")
# print(var)

# var = ("Hola", "Juana", 20) * 2
# print(var)

# tupla = ("Jose", "Maria", "Sandra")
# tupla[2] = "Domitila" # ERROR ES INMUTABLES
# print(tupla)

var = (1, 2, "Maria", 4, 5)

num1, num2, nombre, num4, num5 = var
print(nombre)
print(num2)


def mi_funcion():
    return (5, 6)

num1, num2 = mi_funcion()
print(num2)


var = (1, 2, "Maria", 4, 5)
print(var[::-1])


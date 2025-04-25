
# ? Tipo de Datos String.

# ? Secuencias de escape
# saludo = "Bienvenidos Estudiantes "INCEPERU""

saludo = "\tBienvenidos: \nEstudiantes \"INCEPERU\""
print(saludo)

# ? METODOS Strings
saludo = "Bienvenidos Estudiantes \"INCEPERU\""
saludo_2 = "aprendiendo a programar en python"
saludo_3 = "     Hola Python       "

print(saludo.upper()) # Convetir todo a Mayuscula
print(saludo.lower()) # Convetir todo a Minuscula
print(saludo_2.capitalize()) # Solo la primera letra en Mayuscula
print(saludo_2.title()) # Las primeras palabras en Mayuscula

print(saludo_3.strip()) # Eliminar espacios a la derecha e izquierda
# lstrip(): Elimina a la izquierda
# rstrip(): Elimina a la derecha

print(saludo.find("E")) # Busca la indexacion de una cadena
print(saludo_2.replace("python", "INCEPERU"))

# ! EJERCICIO: A ESTOS DAOS CAMBIA:
# ! A LA PRIMERA VARIABLE que conviertela a MAYUSCULA, a la segunda en MINUSCULA, y a la TERCERA, Solo las primeras letras en Mayusculas, Cambia el apellido a estos datos.

# ? CONCEPTO DE INDEXACION, SLACING y STRIDE
# ? INDEXACION 
nombre = "Ana Perez"
print(nombre[7]) # Extrae un caracter del string
print(nombre[-2])

# ? SLACING
nombre = "Joe Perez"
print(nombre[:9]) # Extrae pedasos de un string
print(nombre[-3:])

# ? STRIDE
nombre = "Ana Curk Cobain"
print(nombre[::2]) # Recorre espacios

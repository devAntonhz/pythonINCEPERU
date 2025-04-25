def suma(*numeros):
    # print(numeros)
    resultado = 0

    for numero in numeros:
        resultado += numero
    print(resultado)

suma(10, 50)
suma(10, 50, 20)
suma(10, 50, 20, 50, 100, 1, 20 ,30)

# def nombres(*noms):
#     print(noms)

# nombres("Juana")
# nombres("Ivana", "Sandra")
# nombres("Julia", "Sandra", "Pedrita")
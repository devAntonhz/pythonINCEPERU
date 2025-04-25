def productos(**datos):
    print(datos["id"], datos["nombre"])


productos(id=1, nombre="TV Sony", anio="2020", desc="Televisor 4K")
productos(id=2, nombre="LG", anio="2019", desc="Televisor 4K", precio=2020)
productos(id=3, nombre="LG WebOS", anio="2019", desc="Televisor 4K")
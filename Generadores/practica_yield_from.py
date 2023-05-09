def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield elemento


ciudades_devueltas=devuelve_ciudades("Lima", "Trujillo", "Arequipa", "Piura")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))
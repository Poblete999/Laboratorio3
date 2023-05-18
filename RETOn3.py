#Resolver antes del miercoles (16:00):


Ciudades = ["Santiago", "Temuco", "Osorno", "Punta Arenas"]
Indice = [134, 99, 245, 50]

Ciudades_aux = (zip(Ciudades, Indice))
maxValor = max(Ciudades_aux, key=lambda x : x[1])
print("La ciudad con el indice de calidad más bajo es",maxValor[0], "con un valor en el indice de",maxValor[1])

Ciudades_aux2 = (zip(Ciudades, Indice))
minValor = min(Ciudades_aux2, key=lambda x : x[1])
print("La ciudad con el indice de calidad más alto es",minValor[0], "con un valor en el indice de",minValor[1])

if maxValor[1]<=50:
    print(maxValor[0], "tiene un indice de calidad del aire bueno")
elif maxValor[1]<=100:
    print(maxValor[0], "tiene un indice de calidad del aire moderado")
elif maxValor[1]<=150:
    print(maxValor[0], "tiene un indice de calidad del aire dañino a la salud para grupos sensibles")
elif maxValor[1]<=200:
    print(maxValor[0], "tiene un indice de calidad del aire dañino a la salud")
elif maxValor[1]<=300:
    print(maxValor[0], "tiene un indice de calidad del aire muy dañino a la salud")
else:
    print(maxValor[0], "tiene un indice de calidad del aire peligroso para la salud")

if minValor[1]<=50:
    print(minValor[0], "tiene un indice de calidad del aire bueno")
elif minValor[1]<=100:
    print(minValor[0], "tiene un indice de calidad del aire moderado")
elif minValor[1]<=150:
    print(minValor[0], "tiene un indice de calidad del aire dañino a la salud para grupos sensibles")
elif minValor[1]<=200:
    print(minValor[0], "tiene un indice de calidad del aire dañino a la salud")
elif minValor[1]<=300:
    print(minValor[0], "tiene un indice de calidad del aire muy dañino a la salud")
else:
    print(minValor[0], "tiene un indice de calidad del aire peligroso para la salud")


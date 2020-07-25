frutas = ['manzana', 'pera', 'mango']
for fruta in frutas:
    print(fruta)

estudiantes = {
    'mexico': 10,
    'chile': 45,
    'brasil': 4,
}

for pais in estudiantes:
    print(pais)

for pais in estudiantes.keys():
    print(pais)

for numero_de_estudiantes in estudiantes.values():
    print(numero_de_estudiantes)

for pais, numero_de_estudiantes in estudiantes.items():
    print(pais, numero_de_estudiantes)
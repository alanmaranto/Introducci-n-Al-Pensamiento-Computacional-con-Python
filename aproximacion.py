# Encontrar raíz de cualquier número
objetivo = int(input("Escoge un numero: "))
epsilon = 0.01
delta = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += delta

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontró la raíz cuadrada del objetivo {objetivo}')
else:
    print(f'La raiz cuadrdada de {objetivo} es {respuesta}')

objetivo = int(input(f'Escoge un numero: '))
epsilon = 0.01
lowerBound = 0.0
upperBound = max(1.0, objetivo)
respuesta = (upperBound + lowerBound) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo={lowerBound}, alto={upperBound}, respuesta={respuesta}')
    if respuesta**2 < objetivo:
        lowerBound = respuesta
    else:
        upperBound = respuesta

    respuesta = (upperBound + lowerBound) / 2

print(f'La raiz cuadrada de {objetivo} es {respuesta}')

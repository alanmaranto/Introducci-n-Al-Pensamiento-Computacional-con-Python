my_tuple = ()
print(type(my_tuple))

# Reasignando tupla vacia
my_tuple = (1, "dos", True)
my_tuple[0]
# Resultado 1

my_tuple[0] = 2
# Error porque tuplas con valores no se pueden reasignar

my_tuple = (1)
""" Esto seria un int """

my_tuple = (1,)
""" Esto si es una tupla """

my_other_tuple = (2, 3, 4)
my_tuple += my_other_tuple
print(my_tuple)


x, y, z = my_other_tuple

def coordinates():
    return (5,4)

coordinate = coordinates()
coordinate
print(coordinate)
x, y = coordinates()
print(x, y)
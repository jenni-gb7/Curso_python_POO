"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:
Bob necesita una forma rápida de calcular el volumen de un cuboide rectangular con tres valores: el , y del cuboide.lengthwidthheight

Escribe una función para ayudar a Bob con este cálculo."""

def get_volume_of_cuboid(length, width, height):
    """
    Calcula el volumen de un cuboide rectangular.

    Parámetros:
        length (int): La longitud del cuboide.
        width (int): El ancho del cuboide.
        height (int): La altura del cuboide.

    Retorna: int: El volumen del cuboide, que es el producto de la longitud, el ancho y la altura.
        """
    vol = length * width * height
    return vol

if __name__ == '__main__':
    length = int(input("Ingresa el primer número:"))
    width = int(input("Ingresa el segundo número:"))
    height = int(input("Ingresa el segundo número:"))
    print(get_volume_of_cuboid(length, width, height))
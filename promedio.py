def calcular_promedio(lista_numeros):
    """
    Calcula el promedio de una lista de números.

    Parámetros:
    lista_numeros (list): Lista que contiene valores numéricos.

    Retorna:
    float: El promedio de los números de la lista.
    """

    promedio = sum(lista_numeros) / len(lista_numeros)
    return promedio


notas = [8, 9, 10, 7, 6]
resultado = calcular_promedio(notas)

print("Las notas son:", notas)
print("El promedio es:", resultado)

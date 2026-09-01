# Número decimal que se convertirá a octal
numero = 255

# Si el número es 0, se imprime directamente
if numero == 0:
    print(0)

# Si el número es diferente de 0, comienza la conversión
else:
    # Variable donde se guardará el número octal
    octal = ""

    # Repite el proceso mientras el número sea mayor que 0
    while numero > 0:
        # Obtiene el residuo de dividir entre 8
        residuo = numero % 8

        # Agrega el residuo al inicio de la cadena octal
        octal = str(residuo) + octal

        # Divide el número entre 8 usando división entera
        numero = numero // 8

# Imprime el resultado final en octal
print(octal)
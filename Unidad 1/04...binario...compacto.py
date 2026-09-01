# Número decimal que se convertirá a binario
numero = 9

# Variable donde se guardará el número binario
binario = ""

# Repite el proceso mientras el número sea mayor que 0
while numero > 0:
    # Obtiene el residuo de dividir entre 2 y lo agrega al inicio del binario.
    # También divide el número entre 2 usando división entera para continuar.
    binario, numero = str(numero % 2) + binario, numero // 2

# Imprime el resultado final en binario
print(binario)
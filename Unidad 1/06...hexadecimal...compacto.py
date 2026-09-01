# Número decimal que se convertirá a hexadecimal
numero = 456

# Variable donde se irá guardando el resultado
hexadecimal = ""

# Cadena con los dígitos del sistema hexadecimal
digitos = "0123456789ABCDEF"       

# Repite el proceso mientras el número sea mayor que 0
while numero > 0:
    # Obtiene el residuo de dividir entre 16 y lo agrega al inicio del resultado
    hexadecimal = digitos[numero % 16] + hexadecimal

    # Divide el número entre 16 (división entera) para continuar la conversión
    numero = numero // 16

# Imprime el resultado; si el número era 0, imprime "0"
print(hexadecimal or "0")
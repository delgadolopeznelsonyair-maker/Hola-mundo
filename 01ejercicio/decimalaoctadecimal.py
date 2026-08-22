numero = 25

octal = ""

while numero > 0:
    residuo = numero % 8
    octal = str(residuo) + octal
    numero = numero // 8

print(octal)
operador = input("Ingrese un operador: (+, -, *, /): ")
o1 = input("Ingrese el primer número: ")
o2 = input("Ingrese el segundo número: ")
resultado = o1 + operador + o2
resultado = eval(resultado)
print("El resultado de la operacion es:", resultado)

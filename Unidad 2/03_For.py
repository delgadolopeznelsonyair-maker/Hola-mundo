#trabajando con for con rangos
for numero in range (0, 7,3) :
    cuadrado = numero ** 2
    print (numero,cuadrado)

#trabajando for con listas 
materias = ["phyton", "linux" , "interfaces"]
for posicion , materias in enumerate (materias, start=1):   
    print(f"{posicion},{materias}")

for materia in materias :
    print(materia)
cadena ="0123456788ABCDEF"
for letra in cadena : 
    print(letra)   

for i in range (len(cadena)):
    print (cadena[i])    
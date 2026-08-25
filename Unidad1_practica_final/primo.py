n = int(input("ingresa un número: "))
if n<=1:
    print("no es primo")
i=2
while i<n:
    if n%i==0:
        print("no es primo")
        break
    elif n%i==0 and i==n:
        print("Es primo ")
        break
    elif n%i!=0 and i<n:
        print("Es primo")
        break
    i=i+1
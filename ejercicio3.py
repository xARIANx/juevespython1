def entrada(x = input("Digite el primer numero: "), y = input("Digite el segundo numero: ")):
    valor1 = int(x)
    valor2 = int(y)
    
    print(f"El primer numero es: {valor1} y el segundo numero es: {valor2}")
    if valor1 > valor2 : print("El primer numero es mayor que el segundo")
    if valor2 > valor1 : print("El segundo numero es mayor que  el primero")

entrada()
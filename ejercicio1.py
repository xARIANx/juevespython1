def multiplo(x = input("Digite el numero que desea calcular: ")):
    numero = int(x)
    if numero % 5 == 0 : print("El numero es multiplo de 5")
    elif numero % 3 == 0 : print("El numero es multiplo de 3")
    else : print("El numero digitado no es multiplo 3 ni de 5")

multiplo()


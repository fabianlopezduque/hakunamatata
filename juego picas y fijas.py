print("............................................")
print("....BIENVENIDO AL JUEGO DE PICAS Y FIJAS....")
print("............................................")

numero = "9410"
numeroEncontrado = False
while not numeroEncontrado:
    #ingresar un numero de cuatro digitos de cero a nueve
   
    numeContrincante= input("ingrese el numero a evaluar: ")
       
    picas=0
    fijas=0
    if numero == numeContrincante:
        numeroEncontrado = True
    else:
        #buscar fijas en el numero dado
        for  i in range(0,4):
            x=numero.find(numeContrincante[i])
            if x == i:
                fijas +=1
            elif x != -1 and x !=1:
                picas +=1
        #indica cuantas picas y fijas hay en el juego del numContrincante
        print(f"tiene {picas} picas y {fijas} fijas")
    if numeroEncontrado:
        print("has encontrado el numero")

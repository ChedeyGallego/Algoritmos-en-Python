#Diseña un algoritmo y un diagrama de flujo para:
    #Con la base y la altura de un rectángulo, 
    #se nos pide calcular su perímetro y su área

#Datos de entrada
    #Base rectángulo
    #Altura rectángulo

#Datos de salida
    #Perímetro rectángulo
    #Área rectángulo

#Proceso
#perimetro=(2b+2h)
#área=(b*h)
def rectángulo():
    base=int(input('Dime la base del rectángulo: '))
    altura=int(input('Dime la altura del rectángulo: '))

    perímetro=(2*base+2*altura)
    área=(base*altura)

    print(f'El perímetro del rectángulo es {perímetro}m y el área es {área}m2')
rectángulo()
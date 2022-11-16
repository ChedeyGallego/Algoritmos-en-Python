#Ejercicio 3
    #Se pide calcular la nota de tu examen tipo test.
    #Serán 20 preguntas
    #Las preguntas correctas sumarán 0,5
    #Las preguntas incorrectas restarán 0,25
    #Las preguntas sin contestar tendrán 0

#Datos de entrada
    #Número de preguntas
    #Preguntas correctas
    #Preguntas incorrectas
    #Preguntas sin contestar

#Datos de salida
    #Nota de tu examen tipo test

#Proceso
#Nota Test= (Correctas*0.5 + Incorrectas*0.25)/20
notaTest=0
def nota():
    for pregunta in range(20):
        respuesta=input("Ingrese si su respuesta es correcta: ")
        if respuesta.lower()=="si":
            notaTest=notaTest+0.5
        if respuesta.lower()=="no":
            notaTest=notaTest-0.25
        if respuesta.lower()=="":
            notaTest=notaTest
        print(notaTest)
notaTest()
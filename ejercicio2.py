#La nota del trimestre está basada en
    #Nota hito individual = 30%
    #Nota hito grupal = 20%
    #Nota examen = 50%

#Datos entrada
    #Nota hito individual
    #Nota hito grupal
    #Nota examen

#Datos salida
    #Nota del trimestre

#Proceso
#notaTrimestre=(notaIndividual+notaGrupal+examen)/3
def nota():
    n1=int(input('Dime tu nota del hito individual: ')) #pedimos la nota individual del hito
    n2=int(input('Dime tu nota del hito grupal: ')) #pedimos la nota grupal del hito
    n3=int(input('Dime tu nota del examen: ')) #pedimos la nota del examen
    notaTrimestre=(n1*0.3+n2*0.2+n3*0.5)
    print (f'La nota del trimestre es {round(notaTrimestre)}')
nota()

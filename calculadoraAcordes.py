
# Nombre: Alejandro Tejada
# Curso: música computacional
# Fecha: Julio 2021
# Programa: calculadoraAcordes.py
# Propósito: Este programa tiene como fin generar una escala y sus acordes
# V 1.0

arrayNotas = ["DO", "DO#", "RE", "RE#", "MI",
              "FA", "FA#", "SOL", "SOL#", "LA", "LA#", "SI"]

arrayNotasv2 = ["DO", "RE", "MI",
                "FA", "SOL", "LA", "SI"]
notaBase = input("Ingrese la nota base de la nueva escala en MAYUSCULAS: ")

indice = arrayNotas.index(notaBase)

arrayNuevaEscala = []
print("La escala es: ....")
# we print the formula
print("Nota:  ", arrayNotas[indice])
arrayNuevaEscala.append(arrayNotas[indice])
indice = (indice+2) % len(arrayNotas)
arrayNuevaEscala.append(arrayNotas[indice])
print("Nota:  ", arrayNotas[indice])
indice = (indice+2) % len(arrayNotas)
arrayNuevaEscala.append(arrayNotas[indice])
print("Nota:  ", arrayNotas[indice])
indice = (indice+1) % len(arrayNotas)
arrayNuevaEscala.append(arrayNotas[indice])
print("Nota:  ", arrayNotas[indice])
indice = (indice+2) % len(arrayNotas)
arrayNuevaEscala.append(arrayNotas[indice])
print("Nota:  ", arrayNotas[indice])
indice = (indice+2) % len(arrayNotas)
arrayNuevaEscala.append(arrayNotas[indice])
print("Nota:  ", arrayNotas[indice])
indice = (indice+2) % len(arrayNotas)
arrayNuevaEscala.append(arrayNotas[indice])
print("Nota:  ", arrayNotas[indice])


def recursiveCalculator(contador, nota):
    if(contador <= 7):
        indice = arrayNuevaEscala.index(nota)
        print("----------------------------------------------")
        print("EL ACORDE DE ", arrayNuevaEscala[indice])
        print("Acorde # :  ", contador, "  ",  arrayNuevaEscala[indice])
        if(indice < len(arrayNuevaEscala)-1):
            notasegunda = arrayNuevaEscala[indice+1]
        else:
            notasegunda = arrayNuevaEscala[indice]
        indice = (indice+2) % len(arrayNuevaEscala)
        print("Acorde # :  ", contador, "  ",  arrayNuevaEscala[indice])
        indice = (indice+2) % len(arrayNuevaEscala)
        print("Acorde # :  ", contador, "  ",  arrayNuevaEscala[indice])
        contador = contador+1
        print("-------------------------------")
        recursiveCalculator(contador, notasegunda)
    else:
        print("Fin de los acordes")


recursiveCalculator(1, arrayNuevaEscala[0])

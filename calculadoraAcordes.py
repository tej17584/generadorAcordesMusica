
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
gradoNumero = int(input("Ingrese el grado como un número [1,2,3,4,5,6,7]: "))
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
        nota1 = arrayNuevaEscala[indice]
        print("Acorde # :  ", contador, "  ",  arrayNuevaEscala[indice])
        if(indice < len(arrayNuevaEscala)-1):
            notasegunda = arrayNuevaEscala[indice+1]
        else:
            notasegunda = arrayNuevaEscala[indice]
        indice = (indice+2) % len(arrayNuevaEscala)
        nota2 = arrayNuevaEscala[indice]
        print("Acorde # :  ", contador, "  ",  arrayNuevaEscala[indice])
        indice = (indice+2) % len(arrayNuevaEscala)
        nota3 = arrayNuevaEscala[indice]
        print("Acorde # :  ", contador, "  ",  arrayNuevaEscala[indice])
        print("El acorde es del tipo: ", getAcorde(nota1, nota2, nota3))
        contador = contador+1
        print("-------------------------------")
        recursiveCalculator(contador, notasegunda)
    else:
        print("Fin de los acordes")


def recursiveCalculatorV2(contador, nota):
    if(contador <= 7 and contador != gradoNumero):
        indice = arrayNuevaEscala.index(nota)
        nota1 = arrayNuevaEscala[indice]
        if(indice < len(arrayNuevaEscala)-1):
            notasegunda = arrayNuevaEscala[indice+1]
        else:
            notasegunda = arrayNuevaEscala[indice]
        indice = (indice+2) % len(arrayNuevaEscala)
        nota2 = arrayNuevaEscala[indice]
        indice = (indice+2) % len(arrayNuevaEscala)
        nota3 = arrayNuevaEscala[indice]
        contador = contador+1
        recursiveCalculatorV2(contador, notasegunda)
    elif(contador <= 7 and contador == gradoNumero):
        print("ENTRADO ACA")
        indice = arrayNuevaEscala.index(nota)
        print("----------------------------------------------")
        print("EL ACORDE DE ", arrayNuevaEscala[indice])
        nota1 = arrayNuevaEscala[indice]
        print("Acorde # :  ", contador, "  ",  arrayNuevaEscala[indice])
        if(indice < len(arrayNuevaEscala)-1):
            notasegunda = arrayNuevaEscala[indice+1]
        else:
            notasegunda = arrayNuevaEscala[indice]
        indice = (indice+2) % len(arrayNuevaEscala)
        nota2 = arrayNuevaEscala[indice]
        print("Acorde # :  ", contador, "  ",  arrayNuevaEscala[indice])
        indice = (indice+2) % len(arrayNuevaEscala)
        nota3 = arrayNuevaEscala[indice]
        print("Acorde # :  ", contador, "  ",  arrayNuevaEscala[indice])
        print("El acorde es del tipo: ", getAcorde(nota1, nota2, nota3))
        print("El acorde del grado: ", gradoNumero,
              " es del tipo: ", getTipoGrado(gradoNumero))
        contador = contador+1
        print("-------------------------------")
        recursiveCalculatorV2(contador, notasegunda)
    else:
        print("Fin de los acordes")


""" 
def getDiferencia(nota1, nota2):
    indice1 = arrayNotas.index(nota1)
    print(indice1)
    indice2 = arrayNotas.index(nota2)
    print(indice2)
    return indice2-indice1
 """


def getTipoGrado(numero):
    if(numero == 1 or numero == 3 or numero == 6):
        return "TONICA"
    elif (numero == 2 or numero == 4):
        return "SUB-DOMINANTE"
    elif(numero == 5 or numero == 7):
        return "DOMINANTE"


def getAcorde(nota1, nota2, nota3):
    indice1 = arrayNotas.index(nota1)
    tipoAcorde1 = ""
    tipoAcorde2 = ""
    if(arrayNotas[(indice1+3) % len(arrayNotas)] == nota2):
        tipoAcorde1 = "MENOR"
    elif(arrayNotas[(indice1+4) % len(arrayNotas)] == nota2):
        tipoAcorde1 = "MAYOR"
    indice2 = arrayNotas.index(nota2)
    if(arrayNotas[(indice2+3) % len(arrayNotas)] == nota3):
        tipoAcorde2 = "MENOR"
    elif(arrayNotas[(indice2+4) % len(arrayNotas)] == nota3):
        tipoAcorde2 = "MAYOR"

    if(tipoAcorde1 == "MAYOR" and tipoAcorde2 == "MAYOR"):
        return "Acorde --> AUMENTADO <--"
    elif(tipoAcorde1 == "MENOR" and tipoAcorde2 == "MENOR"):
        return "Acorde --> DISMINUIDO <--"
    elif(tipoAcorde1 == "MAYOR" and tipoAcorde2 == "MENOR"):
        return "Acorde --> MAYOR <--"
    elif(tipoAcorde1 == "MENOR" and tipoAcorde2 == "MAYOR"):
        return "Acorde --> MENOR <--"
    return ""


recursiveCalculatorV2(1, arrayNuevaEscala[0])

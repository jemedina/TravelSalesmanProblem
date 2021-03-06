from random import *
import math
import itertools
import random
import time

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Utils():

    #Metodo para calcular el recorrido total de un posible orden a visitar de ciudades
    @staticmethod
    def calcularRecorrido(copiaCiudades):
        recorrido=0
        for i in range(len(copiaCiudades)-1):
            ruta = Ruta(copiaCiudades[i], copiaCiudades[i+1])
            recorrido += ruta.distancia

        return recorrido

class Ciudad():
    def __str__(self):
        #return "Ciudad{no: "+color.RED+str(self.no_ciudad)+color.END+", x: "+color.BLUE+str(self.x)+color.END+", y: "+color.BLUE+str(self.y)+color.END+"}"
        return str(self.no_ciudad)

    def __repr__(self):
        return self.__str__()

    def __init__(self,no_ciudad, x, y):
        self.no_ciudad = no_ciudad
        self.x = x
        self.y = y


class Ruta():
    c_origen = None#Ciudad origen
    c_destino = None#Ciudad destino
    distancia = 0#Distancia entre ciodades

    def __init__(self, c_origen, c_destino):
        self.c_origen = c_origen
        self.c_destino = c_destino
        self.distancia = 0
        self.calcularDistancia(c_origen, c_destino)

    #Metodo para calcular la distancia entre 2 ciudades
    def calcularDistancia(self, c_origen, c_destino):
        self.distancia = math.sqrt(
            ((c_origen.x - c_destino.x)**2) + ((c_origen.y - c_destino.y)**2))
        #print("Calculando distancia entre ciudad ",c_origen.no_ciudad, "y ", c_destino.no_ciudad)

class Ciudades():
    ciudades = []#Arreglo para las 25 ciudades
    recorrido = 0#Valor de la suma de las distancias entre c/u de las ciudades
    def __init__(self):
        pass
    
    def __str__(self):
        return self.ciudades


    def genCiudades(self):
        self.ciudades.append(Ciudad(1,5,4))
        self.ciudades.append(Ciudad(2,7,4))
        self.ciudades.append(Ciudad(3,5,6))
        self.ciudades.append(Ciudad(4,4,3))
        self.ciudades.append(Ciudad(5,3,6))
        self.ciudades.append(Ciudad(6,4,5))
        self.ciudades.append(Ciudad(7,2,4))
        self.ciudades.append(Ciudad(8,1,3))
        self.ciudades.append(Ciudad(9,1,5))
        self.ciudades.append(Ciudad(10,3,2))
        self.ciudades.append(Ciudad(11,6,3))
        self.ciudades.append(Ciudad(12,7,7))
        self.ciudades.append(Ciudad(13,6,1))
        self.ciudades.append(Ciudad(14,4,1))
        self.ciudades.append(Ciudad(15,1,1))
        self.ciudades.append(Ciudad(16,1,7))
        self.ciudades.append(Ciudad(17,4,7))
        self.ciudades.append(Ciudad(18,7,2))
        self.ciudades.append(Ciudad(19,9,2))
        self.ciudades.append(Ciudad(20,8,5))
        self.ciudades.append(Ciudad(21,10,4))
        self.ciudades.append(Ciudad(22,11,1))
        self.ciudades.append(Ciudad(23,10,7))
        self.ciudades.append(Ciudad(24,13,6))
        self.ciudades.append(Ciudad(25,12,8))

        return self.ciudades


    def shuffleCiudades(self):
        time.sleep(0.005)
        primeraCiudad = self.ciudades[0]
        nuevoOrdenMundial = self.ciudades[1:len(self.ciudades)]
    
        random.shuffle(nuevoOrdenMundial)
        copiaCiudades = []
        copiaCiudades.append(primeraCiudad)
        copiaCiudades.extend(nuevoOrdenMundial)
        copiaCiudades.append(primeraCiudad)
        return copiaCiudades

class Nodo():
    def __init__(self, ciudades, recorrido = None):
        self.ciudades = ciudades
        if recorrido != None:
            self.recorrido = recorrido
        else:
            self.recorrido = Utils.calcularRecorrido(self.ciudades)

    def findCiudad(self, no_ciudad):
        for index in range(len(self.ciudades)):
            if self.ciudades[index].no_ciudad == no_ciudad:
                return index

        return -1

    def __str__(self):
        return "Nodo{ ciudades: "+str(self.ciudades)+", "+color.UNDERLINE+"recorrido: "+str(self.recorrido)+color.END+"}"

def genColleccion(cities):
    """
    Debido a que hacer una permutacion de 25 en las 25 ciudades tarda demaciado, 
    opte por hacer 5 permutaciones de 5 digitos en rangos de numeros
    de modo que en ningun rango se repiten numeros de otros rangos(permutaciones)
    """
    poblacion = []
    for i in range(100):
        #Genera un orden de recorrido para la cuidades
        t = Nodo(cities.shuffleCiudades())        
        poblacion.append(t)

    poblacion.sort(key= lambda x: x.recorrido, reverse= False)
    return poblacion

def cruza(nodo1, nodo2):
    #Generar arreglo vacio (de puros None)
    nuevasCiudades = [None for i in range(len(nodo1.ciudades))]

    #Asignar la primera y segunda ciudad
    nuevasCiudades[0] = nodo1.ciudades[0]
    i = 1
    nuevasCiudades[i] = nodo1.ciudades[i]
    stopIndex = len(nodo1.ciudades) - 2
    stopIndex2 = 1
    
    i = nodo1.findCiudad(nodo2.ciudades[i].no_ciudad)
    
    while(i != stopIndex and i != stopIndex2):
        nuevasCiudades[i] = nodo1.ciudades[i]
        i = nodo1.findCiudad(nodo2.ciudades[i].no_ciudad)
    
    nuevasCiudades[i] = nodo1.ciudades[i]
    while(None in nuevasCiudades):
        i = nuevasCiudades.index(None)
        if(nodo2.ciudades[i].no_ciudad == nuevasCiudades[1].no_ciudad):
            nuevasCiudades[i] = nodo2.ciudades[stopIndex]
        else:
            nuevasCiudades[i] = nodo2.ciudades[i]
    return nuevasCiudades

def merge(generacion):
    nuevaGeneracion = []
    tam = 50
    for step in range(1,5,1):
        i = 0
        c = 0
        tCounter = 0
        while(i < tam and tCounter < 25):
            tCounter += 1
            if i+step >= tam:
                indiceCiclado = i+step - tam
                nuevaGeneracion.append(Nodo(cruza(generacion[i],generacion[indiceCiclado])))
                #print("MERGE ",step," - ",tCounter," - ",i+1," con ",indiceCiclado+1)
            else:
                nuevaGeneracion.append(Nodo(cruza(generacion[i],generacion[i+step])))
                #print("MERGE ",step," - ",tCounter," - ",i+1," con ",i+step+1)

            c += 1
            if c == step:
                i = i + step + 1
                c = 0
            else:
                i = i + 1
    
    return nuevaGeneracion

    

def imprimirNodos(nodos):
    for i in range(len(nodos)):
        print()
        print(color.BOLD,"*",i+1,color.END,nodos[i])


if __name__ == '__main__':
    cities = Ciudades()
    cities.genCiudades()
    #IMPRIMIR ARCHIVO
    outputFile = open("result.txt", "+w")
    
    generacionInicial = genColleccion(cities)
    #imprimirNodos(generacionInicial)

    #Seleccionar los 50 mejores:
    generacionInicial = generacionInicial[:50]
    #imprimirNodos(generacionInicial)
    generacion = 1
    nuevaGeneracion = None

    print("generacion\tnodo\trecorrido\t\t\t\t\tciudades", file=outputFile)
    gen = 1
    for i in range(len(generacionInicial)):
        print(str(gen) + "\t\t\t" + str(i+1) + "\t\t" + str(generacionInicial[i].recorrido) + "\t\t\t" + str(generacionInicial[i].ciudades), file=outputFile)
    
    while(gen < 100):
        print("**** ===== GEN ",gen,"===== ",file=outputFile)
        if nuevaGeneracion == None:
            nuevaGeneracion = merge(generacionInicial)
        else:
            nuevaGeneracion = merge(nuevaGeneracion)
        
        nuevaGeneracion.sort(key= lambda x: x.recorrido, reverse= False)
        nuevaGeneracion = nuevaGeneracion[:50]

        for i in range(len(nuevaGeneracion)):
            print(str(gen) + "\t\t\t" + str(i+1) + "\t\t" + str(nuevaGeneracion[i].recorrido) + "\t\t\t" + str(nuevaGeneracion[i].ciudades), file=outputFile)
        #Mutación avl
        nuevaGeneracion[0].ciudades[4], nuevaGeneracion[0].ciudades[9] = nuevaGeneracion[0].ciudades[9], nuevaGeneracion[0].ciudades[4]
        print(" ==== Nodo mutado ==== ", file=outputFile)
        print("2\t\t\t1\t\t----------------\t\t\t" + str(nuevaGeneracion[0].ciudades), file=outputFile)
        
        gen += 1

    print("Recorrido final: ",nuevaGeneracion[0].recorrido)
    outputFile.close()
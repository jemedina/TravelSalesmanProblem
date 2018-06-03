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



class Ciudad():
    def __str__(self):
        return "Ciudad{no: "+color.RED+str(self.no_ciudad)+color.END+", x: "+color.BLUE+str(self.x)+color.END+", y: "+color.BLUE+str(self.y)+color.END+"}"
        #return str(self.no_ciudad)

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

    #Metodo para generar 25 ciudades 
    def genCiudades(self):
        for i in range(25):
            self.ciudades.append(Ciudad(i+1))
            #print("Ciudad: ", self.ciudades[i].no_ciudad, "coordenadas(",
            #      self.ciudades[i].x, ",", self.ciudades[i].y, ")")   

        return self.ciudades

    def genCiudades2(self):
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



    #Metodo para calcular el recorrido total de un posible orden a visitar de ciudades
    def calcularRecorrido(self,copiaCiudades,size=25):
        time.sleep(0.005)
        self.recorrido=0
        for i in range(size):
            #print("i=",i)
            #print("vamos a visitar la ciudad en el lugar ", orden[i])
                #print("visitando city",self.ciudades[orden[i]].no_ciudad)
            #if i == 24:
            #    ruta = Ruta(copiaCiudades[25], copiaCiudades[0])
            #else:
            ruta = Ruta(copiaCiudades[i], copiaCiudades[i+1])
                #print("Ruta: ", ruta.distancia)
            self.recorrido += ruta.distancia
        #print("Recorrido: ", self.recorrido)
        return self.recorrido

    def actualizarOrden(self):
        primeraCiudad = self.ciudades[0]
        nuevoOrdenMundial = self.ciudades[1:len(self.ciudades)]
    
        random.shuffle(nuevoOrdenMundial)
        copiaCiudades = []
        copiaCiudades.append(primeraCiudad)
        copiaCiudades.extend(nuevoOrdenMundial)
        copiaCiudades.append(primeraCiudad)
        return copiaCiudades

class Nodo():
    def __init__(self, ciudades, recorrido):
        self.ciudades = ciudades
        self.recorrido = recorrido
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
        copiaCiudades = cities.actualizarOrden()
        t= Nodo(copiaCiudades, cities.calcularRecorrido(copiaCiudades))        
        poblacion.append(t)

    poblacion.sort(key= lambda x: x.recorrido, reverse= False)
    return poblacion


def imprimirNodos(nodos):
    for i in range(len(nodos)):
        print()
        print(color.BOLD,"*",i+1,color.END,nodos[i])

if __name__ == '__main__':
    cities = Ciudades()
    #print("############################################Generando cuidades############################################")
    cities.genCiudades2()


    #print("############################################calculando sus rutas y recorrido############################################")
    #calcula el recorrido total entre las cuidades 
    #########cities.calcularRecorrido(orden_ciudades[0])

    #generacion es una lista de 100 elementos la cual tiene [objeto de las ciudades, el recorrido entre ellas(diferente)]
    generacion = genColleccion(cities)
    imprimirNodos(generacion)
    #print(list(generacion))

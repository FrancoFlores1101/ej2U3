import numpy as np
from ClaseFlores import flor
import csv
class manejadorFlores:
    __dimension=10
    __cantidad=0
    __incremento=5
    __arreglo=None
    def __init__(self):
        self.__dimension=10
        self.__cantidad=0
        self.__cantidad=0
        self.__arreglo=np.empty(10,dtype=flor)

    def agregar(self,unaflor):
        if self.__cantidad == self.__dimension
            self.__dimension+=self.__incremento
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad]=unaflor
        self.__cantidad+=1

    def leercsv(self):
        archivo=open('flores.csv')
        reader=csv.reader(archivo)
        for row in reader:
            try:
                unaflor=flor(row[0],row[1],row[2],row[3])
            except:
                print('finalizada lectura del archivo')
            else:
                self.agregar(unaflor)
        archivo.close()

    def buscarFlorPorNumero(self, numero:int):
        i = 0
        while i < self.__cantidad and self.__arreglo[i].getNumero() != numero:
            i += 1
        if i == self.__cantidad:
            i = -1
        return i

    def getFlorPorNumero(self, numero:int):
        unaFlor = None
        indice = self.buscarFlorPorNumero(numero)
        if indice == -1:
            print("[ERROR] No se encontro la flor")
        else:
            unaFlor = self.__arreglo[indice]
        return unaFlor
    def aumentar(self,n):
        indice=self.buscarFlorPorNumero(n)
        if indice != -1
            self.__arreglo[indice].aumentarventa()
    def mostrarventas(self):
        for flor in self.__arreglo:
            print('{0} {1} {2}'.format(flor.getnombre(),flor.getcolor(),flor.getventa()))

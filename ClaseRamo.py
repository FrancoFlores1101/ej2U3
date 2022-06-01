from manejadorFlores import manejadorFlores
from ClaseFlores import  flor

class ramo:
    __tamanio=None
    __flores=None
    def __init__(self,tamanio):
        self.__tamanio=tamanio
        self.__flores=manejadorFlores()
    def agregarflor(self,flor):
        self.__flores.agregar(flor)
    def gettamaño(self):
        return self.__tamanio
    def contarflores(self):
        for flor in manejadorFlores:
            print('{0} {1}'.format(flor.getnombre(),flor.getcolor()))

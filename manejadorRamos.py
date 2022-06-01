from ClaseRamo import ramo
from manejadorFlores import manejadorFlores
class manejadorRamos:
    __listaramos=[]
    def __init__(self):
        __listaramos=[]
    def agregarramos(self,unRamo):
        self.__listaramos.append(unRamo)
    def ingresarTamañoRamo(self):
        tamaño = self.__ingresador.inputInt("Ingrese el tamaño del ramo\n[1] Chico\n[2] Mediano\n[3] Grande\n--> ")
        while not 1<=tamaño<=3:
            print("Valor invalido, reintente")
            tamaño = self.__ingresador.inputInt("Ingrese el tamaño del ramo\n[1] Chico\n[2] Mediano\n[3] Grande\n--> ")
        tamaño = self.__tamaños[tamaño - 1]
        return tamaño

    def crearRamo(self,unManejadorFlores:manejadorFlores):
        tamaño=self.ingresarTamañoRamo()
        unRamo=ramo(tamaño)
        for flor in unManejadorFlores:
            print("[{0}] {1} {2}".format(flor.getNumero(), flor.getNombre(), flor.getColor()))
        numero = int(input())
        while numero != 0:
            unaFlor = unManejadorFlores.getFlorPorNumero(numero)
            if isinstance(unaFlor,flor):
                unRamo.agregarFlor(unaFlor)
                unManejadorFlores.
                print("Flor agregada")
            numero = input()
        self.agregarRamo(unRamo)
    def mostrarportamanio(self):
        tamaño=self.ingresarTamañoRamo()
        for ramo in self.__listaramos:
            if tamaño==ramo.gettamaño()
                ramo.contarflores()

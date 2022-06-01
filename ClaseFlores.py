class flor:
    __numero=None
    __nombre=None
    __color=None
    __descripcion=None
    __cantidadvendida=0
    def __init__(self,num,nom,col,des):
        self.__numero=num
        self.__nombre=nom
        self.__color=col
        self.__descripcion=des
    def getnumero(self):
        return self.__numero
    def getnombre(self):
        return self.__nombre
    def getcolor(self):
        return self.__color
    def getdescripcion(self):
        return self.__descripcion
    def aumentarventa(self):
        self.__cantidadvendida+=1
    def getventa(self):
        return self.__cantidadvendida

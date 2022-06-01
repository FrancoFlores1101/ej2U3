from manejadorFlores import manejadorFlores
from manejadorRamos import  manejadorRamos
if __name__ == '__main__':
    unmanejador=manejadorRamos
    otromanejador=manejadorFlores
    otromanejador.leercsv()
    menu=menu(unmanejador,otromanejador)

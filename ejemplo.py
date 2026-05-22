from Clases.LSE import LSE
from subprocess import run
from random import randrange

if __name__=='__main__':
    run('cls', shell=True)

    L = LSE()

    for i in range ( randrange(20) ):   # No se sabe cuantos nodos se insertaran (maximo 20)
        L.insertaAlUltimo( randrange(100) )
    L.muestraLSE()
    print('\n\n')

    n = L.cuentaNodos()
    print(f'En la lista, hay {n} nodo(s)')

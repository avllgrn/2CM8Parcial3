from subprocess import run
from Clases.ClaseCola import Cola

class IteradorLSE:
    def __init__(self, L):
        self.aux = L.primero

    def __iter__(self):
        return self

    def __next__(self):
        if self.aux != None:
            n = self.aux
            self.aux = self.aux.siguiente
            return n
        else:
            raise StopIteration

class LSE (Cola):

    def __iter__(self):
        return IteradorLSE(self)

    def __str__(self):
        cadena = ''
        for n in self:
            cadena += str(n)
        return cadena

if __name__ == '__main__':
    run('cls', shell=True)

    L = LSE()

    L.push(1)
    L.push(3)
    L.push(5)
    L.push(7)
    L.push(9)

    for dato in L:
        print(dato, end='')
    print()

    print(L)
    print()

    print('\n\nFin de programa\n\n')
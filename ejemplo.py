from subprocess import run

class IteradorUnitarioAscendente:
    def __init__(self, n):
        self.ini = 0
        self.fin = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.ini <= self.fin:
            d = self.ini
            self.ini += 1
            return d
        else:
            raise StopIteration

class IteradorUnitarioDescendente:
    def __init__(self, n):
        self.ini = 0
        self.fin = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.fin >= self.ini:
            d = self.fin
            self.fin -= 1
            return d
        else:
            raise StopIteration

if __name__ == '__main__':
    run('cls', shell=True)

    I = IteradorUnitarioAscendente(10)
    for dato in I:
        print(dato)
    print()

    I = IteradorUnitarioDescendente(10)
    for dato in I:
        print(dato)
    print()

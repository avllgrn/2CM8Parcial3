from subprocess import run

class IteradorFibonacci:
    def __init__(self, terminos):
        self.a = 0
        self.b = 1
        self.i = 0
        self.terminos = terminos

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.terminos and (self.i == 0 or self.i == 1):
            d = self.i
            self.i += 1
            return d
        elif self.i <= self.terminos:
            c = self.a + self.b
            self.a = self.b
            self.b = c
            self.i += 1
            return c
        else:
            raise StopIteration

if __name__ == '__main__':
    run('cls', shell=True)

    n = float(input('Dame n '))
    print('\n\n')

    I = IteradorFibonacci( n )
    for dato in I:
        print(dato)
    print()


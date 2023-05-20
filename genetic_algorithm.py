import convert
import numpy as np

class genetic_algorithm:
    #construtor
    def __init__(self):
        pass

    #padronização do tamanho dos cromossomos binários
    def standard(self, bin):
        if len(bin) < 3:
            rect = '0' *  (3 - len(bin))
            bin = rect + bin
        return bin

    #função original
    def f(self, x, y):
        return (x ** 3 + 2 * y ** 4) ** (1/2)

    #função de avaliação
    def g(self, x, y):
        return 1 + f(x, y)

    #inicializar a população
    def init(self, size):
        population = []
        for i in range(size):
            #gera um par aleatório no intervalo [0, 7]
            pair = np.random.randint(0, 8, (2))
            #converte pra binário e concatena
            ind = ''
            ind = ind + self.standard(convert.dec_to_bin(pair[0]))
            ind = ind + self.standard(convert.dec_to_bin(pair[1]))
            #gerando a população inicial
            population.append({
                'individual': ind,
                'x': pair[0],
                'y': pair[1]
            })
        
        return population
    

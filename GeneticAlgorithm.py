import convert
import numpy as np
from math import floor


# standardizing binary chromosomes size
def standard(binary):
    if len(binary) < 3:
        rect = '0' * (3 - len(binary))
        binary = rect + binary
    return binary


# original function
def f(x, y):
    return (x ** 3 + 2 * y ** 4) ** (1 / 2)


# evaluating function
def g(x, y):
    return 1 + f(x, y)


def mutation(chromosome):
    r = ''

    for i in range(len(chromosome)):
        prob = np.random.random()  # random number between 0 and 1

        if prob < 0.05:  # 5% of chance of mutation for each gene
            r = r + ('0' if chromosome[i] == '1' else '1')
        else:
            r = r + chromosome[i]

    return r


def prep_kids(kids):
    r = []
    for i in range(len(kids)):
        x = kids[i][:-3]
        y = kids[i][3:]
        r.append({
            'individual': kids[i],
            'x': convert.bin_to_dec(x),
            'y': convert.bin_to_dec(y)
        })

    return r


class GeneticAlgorithm:
    # constructor
    def __init__(self, size):
        self.size = size
        self.population = []
        self.init_population(size)
        self.evaluation()

    # initializing population
    def init_population(self, size):
        for i in range(size):
            # generates a random pair in range [0, 7]
            pair = np.random.randint(0, 8, 2)

            # converts to binary and concatenates them
            ind = ''
            ind = ind + standard(convert.dec_to_bin(pair[0]))
            ind = ind + standard(convert.dec_to_bin(pair[1]))

            # appends individual to the population
            self.population.append({
                'individual': ind,
                'x': pair[0],
                'y': pair[1]
            })

    # evaluate all the individuals in the population
    def evaluation(self):
        # model = {'individual': '',
        #          'evaluation': '',
        #          'probability': '',
        #          'portion': ''
        #      }

        total = 0

        for i in range(len(self.population)):  # self.population = [[x1, y1], [x2, y2], ... , [xn, yn]]
            evaluation = g(self.population[i]['x'], self.population[i]['y'])
            total = total + (1 / evaluation)  # inverted values bc we want minimizing

            self.population[i]['evaluation'] = evaluation

        r = 0  # starting point of the roulette
        for i in range(len(self.population)):
            self.population[i]['probability'] = (1 / self.population[i]['evaluation']) / total
            self.population[i]['portion'] = [r, r + self.population[i]['probability'] * 360]
            r = self.population[i]['portion'][1] + 0.1

    # select parents for crossover
    def roulette(self):
        # random number of pair for crossover
        n = np.random.randint(1, 5)

        parents = []
        chosen = []

        while len(parents) < n:
            aux = [-1, -1]

            for j in [0, 1]:
                # choose a random number between 0 and 360
                c = np.random.randint(361)

                for k in range(len(self.population)):
                    low = floor(self.population[k]['portion'][0])
                    high = floor(self.population[k]['portion'][1])

                    if c in range(low, high):
                        aux[j] = k

            if (aux[0] != aux[1] != -1) and (aux[0] not in chosen) and (aux[1] not in chosen):
                parents.append(aux)
                chosen.append(aux[0])
                chosen.append(aux[1])

        return parents, chosen

    def crossover(self, parents):
        kids = []
        len_ind = len(self.population[0]['individual'])

        for i in range(len(parents)):
            p = np.random.randint(1, len_ind)  # cutting point

            j = parents[i]

            # print(f'\ncorte: {p}')
            # print(f'parents: {population[j[0]]["individual"]} e {population[j[1]]["individual"]}')

            first_parent_1 = self.population[j[0]]['individual'][:-1 * (len_ind - p)]
            first_parent_2 = self.population[j[0]]['individual'][p:]

            second_parent_1 = self.population[j[1]]['individual'][:-1 * (len_ind - p)]
            second_parent_2 = self.population[j[1]]['individual'][p:]

            first_kid = first_parent_1 + second_parent_2
            second_kid = second_parent_1 + first_parent_2

            # print(f'kids: {first_kid} e {second_kid}')

            # random mutation

            first_kid = mutation(first_kid)
            second_kid = mutation(second_kid)

            kids.append(first_kid)
            kids.append(second_kid)

        return kids

    def reset_population(self, kids, chosen):
        kids = prep_kids(kids)
        if len(kids) != self.size:
            for i in range(self.size):
                if i not in chosen:
                    kids.append(self.population[i])
        self.population = kids[:]
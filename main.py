from GeneticAlgorithm import GeneticAlgorithm

genetic_algorithm = GeneticAlgorithm(8)
genetic_algorithm.evaluation()
it = 50

for i in range(1, it+1):
    print(f'\n--------------- iteração {i} ---------------')
    parents, chosen = genetic_algorithm.roulette()
    kids = genetic_algorithm.crossover(parents)
    genetic_algorithm.reset_population(kids, chosen)
    genetic_algorithm.evaluation()

    better = genetic_algorithm.population[0]

    for i in range(genetic_algorithm.size):
        if genetic_algorithm.population[i]['evaluation'] < better['evaluation']:
            better = genetic_algorithm.population[i]

    print(f'melhor: {better}')

print('\n--------------- final ---------------')
result = genetic_algorithm.population[0]

for i in range(genetic_algorithm.size):
    if genetic_algorithm.population[i]['evaluation'] < result['evaluation']:
        result = genetic_algorithm.population[i]

print('resultado:')
print(result)
print('população final:')

for i in range(genetic_algorithm.size):
    print(genetic_algorithm.population[i])

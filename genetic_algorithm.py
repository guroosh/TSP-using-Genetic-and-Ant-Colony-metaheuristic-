import math
import random
from random import randint, sample
from matplotlib import pyplot as plt

import utils

NUMBER_OF_ITERATIONS = 100  # number of iterations for the algorithm to run
INITIAL_POPULATION = 200  # initial population
NUMBER_OF_POPULATION = 40  # number of population after every iteration
NUMBER_OF_COUPLES = 20  # used in selecting couples in selection(), selection2(), selection3()
K_IN_TOURNAMENT_SELECTION = 20  # percentage -> 0 to 100
MUTATION_PROBABILITY = 25  # percentage -> 0 to 100
NUMBER_OF_SWAPS = 2  # used in mutation function
CROSSOVER_TYPE = 1  # 1 for random, 2 for roulette wheel, 3 for tournament selection, 0 for all three


def populate(number_of_cities):
    genes = []
    num = INITIAL_POPULATION
    for i in range(num):
        a = sample(range(0, number_of_cities), number_of_cities)
        genes.append(a)
    return genes


# EVALUATES THE DISTANCE OF A SINGLE GENE
def evaluate(x, number_of_cities, points):
    total = 0
    first = x[0]
    for i in range(len(x) - 1):
        total += utils.dist(x[i], x[i + 1], points)
    total += utils.dist(x[number_of_cities - 1], first, points)
    return total


# RETURNS THE BEST GENE
def evaluation(genes, number_of_cities, points):
    min_gene = None
    min_dist = float('inf')
    for x in genes:
        dist1 = evaluate(x, number_of_cities, points)
        if dist1 < min_dist:
            min_dist = dist1
            min_gene = x
    ret_gene = min_gene[:]
    ret_gene.append(min_gene[0])
    return ret_gene, min_dist


def print_answer(max_gene, max_num, counter1):
    print(counter1, ': ', max_num, '   ', max_gene)


# CHOOSES THE BEST PARENTS FROM THE TOTAL POPULATION (depends on the NUMBER_OF_POPULATION parameter)
def reduce_population(genes, number_of_cities, points):
    list_genes = {}
    for x in genes:
        temp = evaluate(x, number_of_cities, points)
        str1 = ''
        for y in x:
            str1 += str(y) + '_'
        list_genes[str1] = temp
    sorted1 = sorted(list_genes.items(), key=lambda v: v[1])
    sorted_top = []
    for i in range(min(len(sorted1), NUMBER_OF_POPULATION)):
        sliced = sorted1[i][0].split('_')
        temp = []
        for j in range(len(sliced) - 1):
            temp.append(int(sliced[j]))
        sorted_top.append(temp)
    return sorted_top


# UNIFORM crossover BETWEEN TWO PARENTS P1 and P2
def crossover(p1, p2, number_of_cities):
    chk = {}
    for i in range(number_of_cities):
        chk[i] = 0
    child = [-1] * number_of_cities
    for x in range(len(p1)):
        if x % 2 == 0:
            child[x] = p1[x]
            chk[p1[x]] = 1
    y = 1
    for x in range(len(p2)):
        if chk[p2[x]] == 0:
            child[y] = p2[x]
            y += 2
    return child


# SELECTION FUNCTION FOR SELECTING RANDOM COUPLES
def selection(genes, number_of_cities):
    children = []

    for i in range(NUMBER_OF_COUPLES):
        a = genes[randint(0, len(genes) - 1)]
        b = genes[randint(0, len(genes) - 1)]
        child = crossover(a, b, number_of_cities)
        children.append(child)
    genes.extend(children)
    return genes


# RETURNS A GENE USING ROULETTE WHEEL SELECTION
def choose_parent_using_RWS(genes, S, number_of_cities, points):
    P = randint(0, int(S))
    for x in genes:
        P += evaluate(x, number_of_cities, points)
        if P > S:
            return x
    return genes[-1]


# SELECTION FUNCTION FOR SELECTING COUPLES USING ROULETTE WHEEL SELECTION
def selection2(genes, number_of_cities, points):
    children = []
    S = 0
    for x in genes:
        S += evaluate(x, number_of_cities, points)
    for i in range(NUMBER_OF_COUPLES):
        a = choose_parent_using_RWS(genes, S, number_of_cities, points)
        b = choose_parent_using_RWS(genes, S, number_of_cities, points)
        child = crossover(a, b, number_of_cities)
        children.append(child)
    genes.extend(children)
    return genes


# RETURNS A GENE USING TOURNAMENT SELECTION
def choose_parent_using_TS(genes, number_of_cities, points):
    sample_size = len(genes) * (K_IN_TOURNAMENT_SELECTION / 100)
    sample = random.sample(genes, int(sample_size) + 1)
    best_value = math.inf
    best_gene = None
    for x in sample:
        this_value = evaluate(x, number_of_cities, points)
        if this_value < best_value:
            best_value = this_value
            best_gene = x
    return best_gene


# SELECTION FUNCTION FOR SELECTING COUPLES USING TOURNAMENT SELECTION
def selection3(genes, number_of_cities, points):
    children = []
    for i in range(NUMBER_OF_COUPLES):
        a = choose_parent_using_TS(genes, number_of_cities, points)
        b = choose_parent_using_TS(genes, number_of_cities, points)
        child = crossover(a, b, number_of_cities)
        children.append(child)
    genes.extend(children)
    return genes


def mutation(genes, number_of_cities):
    # pm = randint(0, 100)                      # Use to mutate only with a probability of MUTATION_PROBABILITY
    pm = 0  # Use to always mutate
    final = genes[:]
    for x in genes:
        temp = []
        for i in range(NUMBER_OF_SWAPS):
            y = x[:]
            a = sample(range(0, number_of_cities), 2)
            if pm < MUTATION_PROBABILITY:
                y[a[0]], y[a[1]] = y[a[1]], y[a[0]]
                temp.append(y)
        final.extend(temp)
    return final


def execute(local_points, number_of_cities):
    points = local_points
    range_var = 1
    if CROSSOVER_TYPE == 0:
        range_var = 3
    for loop in range(range_var):
        print(points)
        print('RUNNING ', NUMBER_OF_ITERATIONS, ' iterations....')

        counter1 = 1
        print("Genetic Algorithm")
        global_min_path_genetic = []
        global_minima_genetic = float('inf')

        population = populate(number_of_cities)
        min_gene, min_num = evaluation(population, number_of_cities, points)
        print_answer(min_gene, min_num, counter1)
        counter1 += 1

        for i in range(NUMBER_OF_ITERATIONS):
            parents = reduce_population(population, number_of_cities, points)
            if CROSSOVER_TYPE == 0:
                if loop == 0:
                    children = selection(parents, number_of_cities)
                elif loop == 1:
                    children = selection2(parents, number_of_cities, points)
                else:
                    children = selection3(parents, number_of_cities, points)
            else:
                if CROSSOVER_TYPE == 1:
                    children = selection(parents, number_of_cities)
                elif CROSSOVER_TYPE == 2:
                    children = selection2(parents, number_of_cities, points)
                else:
                    children = selection3(parents, number_of_cities, points)
            population = mutation(children, number_of_cities)
            min_gene, min_num = evaluation(population, number_of_cities, points)
            if min_num < global_minima_genetic:
                global_minima_genetic = min_num
                global_min_path_genetic = min_gene
            print_answer(min_gene, min_num, counter1)
            counter1 += 1

        print()
        print('After ', NUMBER_OF_ITERATIONS, ' iterations:-')
        print('Best path from genetic algorithm       : ', global_min_path_genetic, '     ', global_minima_genetic)

        plot_x = []
        plot_y = []

        for p in global_min_path_genetic:
            plot_x.append(points[p][0])
            plot_y.append(points[p][1])

        if CROSSOVER_TYPE == 0:
            if loop == 0:
                plt.plot(plot_x, plot_y, 'bo-', linewidth=7, label='random ' + "{:.2f}".format(global_minima_genetic))
            if loop == 1:
                plt.plot(plot_x, plot_y, 'yo-', linewidth=5, label='roulette wheel ' + "{:.2f}".format(global_minima_genetic))
            if loop == 2:
                plt.plot(plot_x, plot_y, 'ro-', linewidth=2, label='tournament ' + "{:.2f}".format(global_minima_genetic))
        else:
            if CROSSOVER_TYPE == 1:
                plt.plot(plot_x, plot_y, 'bo-', linewidth=2, label='random ' + "{:.2f}".format(global_minima_genetic))
            if CROSSOVER_TYPE == 2:
                plt.plot(plot_x, plot_y, 'yo-', linewidth=2, label='roulette wheel ' + "{:.2f}".format(global_minima_genetic))
            if CROSSOVER_TYPE == 3:
                plt.plot(plot_x, plot_y, 'ro-', linewidth=2, label='tournament ' + "{:.2f}".format(global_minima_genetic))
        plt.plot(plot_x, plot_y, 'ko')

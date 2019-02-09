# TSP-using-metaheuristic-genetic-and-ant-colony-
Code to solve "travelling salesman problem" using "genetic algorithm" and "ant colony optimization"

Parameters in Genetic Algorithm:

    NUMBER_OF_ITERATIONS = 100  # number of iterations for the algorithm to run

    INITIAL_POPULATION = 200  # initial population

    NUMBER_OF_POPULATION = 40  # number of population after every iteration

    NUMBER_OF_COUPLES = 20  # used in selecting couples in selection(), selection2(), selection3()

    K_IN_TOURNAMENT_SELECTION = 20  # percentage -> 0 to 100

    MUTATION_PROBABILITY = 25  # percentage -> 0 to 100

    NUMBER_OF_SWAPS = 2  # used in mutation function

    CROSSOVER_TYPE = 1  # 1 for random, 2 for roulette wheel, 3 for tournament selection, 0 for all three


Parameters in Ant Colony Optimization:

    NUMBER_OF_ITERATIONS = 100  # number of iterations for the algorithm to run

    EVAPORATION_FACTOR = 0.5  # number between 0 and 1; 0 for complete evaporation, 1 for no evaporation

    UPDATED_PHEROMONE_VALUE = 7  # exact pheromone value for each ant travelled, initial value is 1

    ALPHA = 1  # parameter to control the influence of previous trails on the edge

    BETA = 1  # parameter to control the influence of the desirability of the edge

import ant_colony_optimization
import genetic_algorithm
import init_data

GRID_SIZE = 100  # only used in random points generation
DATA_ENTRY_POINT = 1  # 1 for random, 2 for loading from file

number_of_cities = input('Enter number of cities: ')
NUMBER_OF_CITIES = int(number_of_cities)
if NUMBER_OF_CITIES < 2:
    NUMBER_OF_CITIES = 2
points = init_data.get_nodes(DATA_ENTRY_POINT, NUMBER_OF_CITIES, GRID_SIZE)
NUMBER_OF_CITIES = len(points)

# STARTING GENETIC ALGORITHM
genetic_algorithm.execute(points, NUMBER_OF_CITIES)

# STARTING ANT COLONY OPTIMIZATION
ant_colony_optimization.execute(points, NUMBER_OF_CITIES)

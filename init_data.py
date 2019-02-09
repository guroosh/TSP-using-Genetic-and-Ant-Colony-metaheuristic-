import random


DATA_FILE = 'data2'  # format of data file: "index x-coordinate y-coordinate"


def get_nodes(data_entry_point, number_of_cities, grid_size):
    points = []
    if data_entry_point == 1:
        # GENERATING RANDOM DATA
        for j in range(number_of_cities):
            x = random.uniform(0, grid_size)
            y = random.uniform(0, grid_size)
            points.append((x, y))
    else:
        # READING DATA FROM FILE
        data_counter = 0
        with open(DATA_FILE, 'r') as in_file:
            for line in in_file:
                words = line.split()
                x = float(words[1])
                y = float(words[2])
                points.append((x, y))
                data_counter += 1
                if data_counter == number_of_cities:
                    break
    return points

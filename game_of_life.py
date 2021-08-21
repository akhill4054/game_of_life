import time
import sys

# To clear the console
sys.stdout.flush()

# Initial configuations.
grid_size = 20
generations_count = 20
frame_delay_in_seconds = 0.5
# List of tuples with two values, (x, y) each (x, y) represent 
# the coordiantes of a seed point which is alive on the grid.
# Note: Top left point is (1, 1) and bottom most is (n, n),
# where n = grid_size.
seed_points = [(8, 8), (8, 9), (8, 10), (7, 10), (6, 9)]

# Utility methods.
get_new_grid = lambda size: [[0 for i in range(size)] for i in range(size)]

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            cell_value = grid[i][j]
            sys.stdout.write('{}  '.format('#' if cell_value else '.'))
        sys.stdout.write('\n')
    sys.stdout.write('\n')

# Generating the grid (2D list of nxn size, where n = grid_size).
grid = get_new_grid(grid_size)

# Reflecting seed points on the grid.
for point in seed_points:
    grid[point[0] - 1][point[1] - 1] = 1

def generate_next_generation(old_generation):
    # Generating the next generation
    new_generation = get_new_grid(grid_size)

    for i in range(grid_size):
        for j in range(grid_size):
            # Current cell is i, j
            # i -> row index, j -> column index
            # Count it's neighbors.
            neighbor_count = 0

            # Top
            if i > 0: 
                neighbor_count += grid[i - 1][j]
                # Top-left
                if j > 0: neighbor_count += old_generation[i - 1][j - 1]
                # Top-right
                if j < grid_size - 1: neighbor_count += old_generation[i - 1][j + 1]
            # Bottom
            if i < grid_size - 1:
                neighbor_count += grid[i + 1][j]
                # Bottom-left
                if j > 0: neighbor_count += old_generation[i + 1][j - 1]
                # Bottom-right
                if j < grid_size - 1: neighbor_count += old_generation[i + 1][j + 1]
            # Left
            if j > 0:
                neighbor_count += old_generation[i][j - 1]
            # Right
            if j < grid_size - 1: 
                neighbor_count += old_generation[i][j + 1]
            
            if neighbor_count == 3:
                # Cell becomes alive due to reproduction, if dead.
                # If alive then it will stay alive.
                new_generation[i][j] = 1
            elif 2 <= neighbor_count < 3:
                # Cell lives on to the next generation, if alive.
                new_generation[i][j] = old_generation[i][j]
            # else: Cell dies either by overcrowding or underpopulation.

    return new_generation

for i in range(generations_count):
    # Wait before clearing the console.
    time.sleep(frame_delay_in_seconds)
    sys.stdout.flush()
    # Generate the new generation and replace old one
    # with it.
    grid = generate_next_generation(grid)
    print_grid(grid)
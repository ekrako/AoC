def parse_input(lines):
    """Parse the input string into a grid and find starting position/direction."""
    grid = [list(line.strip()) for line in lines]

    start_pos = next(
        (x, y)
        for y, line in enumerate(grid)
        for x, value in enumerate(line)
        if value in "<>^v"
    )
    start_dir = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}[
        grid[start_pos[1]][start_pos[0]]
    ]
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    directions = (
        directions[: directions.index(start_dir)]
        + directions[directions.index(start_dir) :]
    )

    return grid, start_pos, directions


def simulate_guard_path(grid, start_pos, directions):
    """Simulate the guard's path and return the set of visited positions."""
    # Directions: up, right, down, left (clockwise order)

    current_pos = start_pos
    height = len(grid)
    width = len(grid[0])

    while True:
        # Calculate next position
        grid[current_pos[1]][current_pos[0]] = "X"
        next_x, next_y = (
            current_pos[0] + directions[0][0],
            current_pos[1] + directions[0][1],
        )

        # Check if we're about to leave the mapped area
        if next_x < 0 or next_x >= width or next_y < 0 or next_y >= height:
            break

        # Check if there's an obstacle ahead
        if grid[next_y][next_x] == "#":
            # Turn right
            directions = directions[1:] + directions[:1]
            next_x, next_y = current_pos
        current_pos = (next_x, next_y)
    return grid


def count_Xs(grid):
    return sum(1 for row in grid for cell in row if cell == "X")


def get_next_moves(pos,directions, grid):
    x, y = pos
    moves = []
    # Check all four directions
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # up, down, left, right
        new_x, new_y = x + dx, y + dy
        if (
            0 <= new_y < len(grid)
            and 0 <= new_x < len(grid[0])
            and grid[new_y][new_x] != "#"
        ):
            moves.append((new_x, new_y))
    return moves


def simulate_path_with_obstruction(grid, start_pos, directions, obstruction_pos):
    # Create a copy of the grid with the obstruction
    height = len(grid)
    width = len(grid[0])
    if obstruction_pos == start_pos:
        return False

    # Place obstruction
    ox, oy = obstruction_pos
    if grid[oy][ox] == "#":
        return False
    grid[oy][ox] = "#"

    # Simulate path
    pos = start_pos
    visited = [(*directions[0],*pos)]

    while True:
        next_x, next_y = (
            pos[0] + directions[0][0],
            pos[1] + directions[0][1],
        )
        # Check if we're about to leave the mapped area
        if next_x < 0 or next_x >= width or next_y < 0 or next_y >= height:
            grid[oy][ox] = "."
            return False
        # Check if there's an obstacle ahead
        if grid[next_y][next_x] == "#":
            # Turn right
            if (*directions, *pos) in visited:
                grid[oy][ox] = "."
                return True
            visited.append((*directions, *pos))
            directions = directions[1:] + directions[:1]
            next_x, next_y = pos
        pos = (next_x, next_y)
        


def solve_part2(grid, start_pos, directions):
    return sum(
        simulate_path_with_obstruction(grid, start_pos, directions.copy(), (x, y))
        for y in range(len(grid))
        for x in range(len(grid[0]))
        if grid[y][x] == "."
    )

# Test input
test_input = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

with open("input6.txt") as f:
    lines = f.readlines()
print(count_Xs(simulate_guard_path(*parse_input(test_input.strip().splitlines()))))
print(count_Xs(simulate_guard_path(*parse_input(lines))))
print(solve_part2(*parse_input(test_input.strip().splitlines())))
print(solve_part2(*parse_input(lines)))

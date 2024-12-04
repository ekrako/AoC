import itertools
from collections import defaultdict


with open("input4.txt") as f:
    lines = f.readlines()

def rev_string(s: str) -> str:
    return "".join(reversed(s))


def transpose(matrix: list[str]) -> list[str]:
    return list(map("".join, list(zip(*matrix))))


def diagonals(matrix: list[str]) -> tuple[list[str], list[str]]:
    rows = len(matrix)
    cols = len(matrix[0])
    diagonal1 = defaultdict(list)  # For the top right to bottom left
    diagonal2 = defaultdict(list)  # For the top left to bottom right
    for i, j in itertools.product(range(rows), range(cols)):
        diagonal1[i - j].append(matrix[i][j])
        diagonal2[i + j].append(matrix[i][j])
    diagonal1 = ["".join(x) for x in diagonal1.values()]
    diagonal2 = ["".join(x) for x in diagonal2.values()]
    return diagonal1, diagonal2


def countString(line: str, value: str = "XMAS") -> int:
    return line.count(value) + rev_string(line).count(value)

lines = [x.strip() for x in lines]
print(
    sum(
        countString(line, "XMAS")
        for line in itertools.chain(lines, transpose(lines), *diagonals(lines))
    )
)

# Part 2
a_loc = itertools.chain(
    *[
        [(i, j) for j, value in enumerate(line) if value == "A"]
        for i, line in enumerate(lines)
    ]
)
a_loc = list(
    filter(lambda c: 0 < c[0] < len(lines) - 1 and 0 < c[1] < len(lines[0]) - 1, a_loc)
)
print(
    sum(
        "".join((lines[a_row - 1][a_col - 1], lines[a_row + 1][a_col + 1]))
        in {"MS", "SM"}
        and "".join((lines[a_row - 1][a_col + 1], lines[a_row + 1][a_col - 1]))
        in {"MS", "SM"}
        for a_row, a_col in a_loc
    )
)

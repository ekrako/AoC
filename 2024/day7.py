from functools import reduce
from itertools import product


def calculate_expression(result, oper_num):
    """Calculate result of expression with given operator and number."""
    oper, num = oper_num
    oper_dict = {
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
        "||": lambda x, y: int(str(x) + str(y)),
    }
    return oper_dict[oper](result, num)


def evaluate_expression(numbers, operators):
    """Evaluate expression left-to-right with given numbers and operators."""
    return reduce(calculate_expression, zip(operators, numbers[1:]), numbers[0])


def generate_operator_combinations(num_positions, operators):
    """Generate all possible combinations of + and * operators."""
    return [list(comb) for comb in product(operators, repeat=num_positions)]


def can_equation_be_true(test_value, numbers, operators):
    """Check if equation can be made true with any combination of operators."""
    operator_combinations = generate_operator_combinations(len(numbers) - 1, operators)
    return any(
        evaluate_expression(numbers, operators) == test_value
        for operators in operator_combinations
    )


def parse_line(line):
    """Parse line into test value and list of numbers."""
    test_part, numbers_part = line.split(":")
    return int(test_part), [int(x) for x in numbers_part.strip().split()]


def solve_calibration(lines, operators):
    """Process input and return sum of valid test values."""
    return sum(
        parse_line(line)[0]
        for line in lines
        if line and can_equation_be_true(*parse_line(line), operators)
    )


# Example input
example_input = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
with open("input7.txt") as f:
    lines = f.readlines()
# Test with example
result = solve_calibration(example_input.strip().split("\n"), ["+", "*"])
print(f"Result for example: {result}")
assert result == 3749, f"Expected 3749 but got {result}"
result = solve_calibration(lines, ["+", "*"])
print(f"Result for file: {result}")
result = solve_calibration(example_input.strip().split("\n"), ["+", "*", "||"])
print(f"Result for example: {result}")
assert result == 11387, f"Expected 11387 but got {result}"
result = solve_calibration(lines, ["+", "*", "||"])
print(f"Result for file: {result}")
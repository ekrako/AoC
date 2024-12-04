with open("input2.txt") as f:
    lines = f.readlines()
    lines = [x.split(" ") for x in lines]
    lines = [[int(x) for x in line] for line in lines]
def check_line(line):
    return (sorted(line) == line or sorted(line, reverse=True) == line) and all(0 < abs(a1 - a2) < 4 for a1, a2 in zip(line[:-1], line[1:]))
def isSafe(line):
    return any(check_line(line[:i] + line[i+1:]) for i in range(len(line)))

print(sum(1 if check_line(line) else 0 for line in lines))
print(sum(1 if isSafe(line) else 0 for line in lines))

with open('input.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]
lines = [line.split('   ') for line in lines]
lines = [[int(x) for x in line] for line in lines]
input1, input2 = zip(*lines)
print(sum(abs(a1-a2) for a1, a2 in zip(sorted(input1), sorted(input2))))
print(sum(a1*input2.count(a1) for a1 in input1))
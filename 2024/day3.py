import re

with open("input3.txt") as f:
    lines = f.readlines()
# lines = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
pattern = r"(?:mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))"
print(
    sum(
        sum(int(a or "0") * int(b or "0") for a, b, _, _ in re.findall(pattern, line))
        for line in lines
    )
)
# lines = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]

enabled = True
print(
    sum(
        sum(
            (
                int(a or "0") * int(b or "0")
                if (enabled := (enable != "") or (enabled and disable == ""))
                else 0
            )
            for a, b, enable, disable in re.findall(pattern, line)
        )
        for line in lines
    )
)

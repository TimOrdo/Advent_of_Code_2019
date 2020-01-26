summary = 0

with open("input.txt") as file:
    for line in file.read().splitlines():
        summary += int(line) // 3 - 2

print(summary)

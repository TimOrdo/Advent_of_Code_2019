answer_list = list()


def fuel_math(mass: int) -> int:
    answer = mass // 3 - 2
    if answer <= 0:
        return 0
    else:
        answer_list.append(answer)
        return fuel_math(answer)


with open("input.txt") as file:
    for line in file.read().splitlines():
        fuel_math(int(line))

print(sum(answer_list))

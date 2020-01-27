import re
from itertools import product


def incode(noun: int, verb: int, inlist: list) -> int:
    in_list = inlist.copy()
    in_list[1] = noun
    in_list[2] = verb
    for i in range(0, len(in_list), 4):
        if in_list[i] == 1:
            in_list[in_list[i + 3]] = in_list[in_list[i + 1]] + in_list[
                in_list[i + 2]]
        elif in_list[i] == 2:
            in_list[in_list[i + 3]] = in_list[in_list[i + 1]] * in_list[
                in_list[i + 2]]
        elif in_list[i] == 99:
            break
    return in_list[0]


with open('input.txt', 'r') as file:
    input_string = file.read()

pattern = re.compile(r'\d+')
inlist = list(map(int, re.findall(pattern, input_string)))

for noun, verb in product(range(0,100), range(0, 100)):
    if incode(noun, verb, inlist) == 19690720:
        print(noun * 100 + verb)
        break

import re


def incode(noun: int, verb: int, in_list: list) -> int:
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

print(incode(12, 2, inlist))

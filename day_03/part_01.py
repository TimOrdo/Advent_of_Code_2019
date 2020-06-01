input_list = list()
first_list = [[0, 0]]
second_list = [[0, 0]]
answer_list = list()

with open('input.txt', 'r') as file:
    for line in file.read().splitlines():
        input_list.append(line.split(','))

for bindex, big_item in enumerate(input_list):
    for index, small_item in enumerate(big_item):
        if bindex == 0:
            if small_item[0] == 'R':
                first_list.append([first_list[index][0] + int(small_item[1:]),
                                   first_list[index][1]])
            elif small_item[0] == 'U':
                first_list.append([first_list[index][0],
                                   first_list[index][1] + int(small_item[1:])])
            elif small_item[0] == 'L':
                first_list.append([first_list[index][0] - int(small_item[1:]),
                                   first_list[index][1]])
            elif small_item[0] == 'D':
                first_list.append([first_list[index][0],
                                   first_list[index][1] - int(small_item[1:])])
        elif bindex == 1:
            if small_item[0] == 'R':
                second_list.append([second_list[index][0] + int(small_item[1:]),
                                   second_list[index][1]])
            elif small_item[0] == 'U':
                second_list.append([second_list[index][0],
                                   second_list[index][1] + int(small_item[1:])])
            elif small_item[0] == 'L':
                second_list.append([second_list[index][0] - int(small_item[1:]),
                                   second_list[index][1]])
            elif small_item[0] == 'D':
                second_list.append([second_list[index][0],
                                   second_list[index][1] - int(small_item[1:])])

for bindex in range(len(second_list) - 1):
    for sindex in range(len(first_list) - 1):
        if second_list[bindex][1] == second_list[bindex+1][1]:
            a = second_list[bindex + 1][1]
            b = first_list[sindex][1]
            c = first_list[sindex + 1][1]
            d = first_list[sindex][0]
            e = second_list[bindex][0]
            f = second_list[bindex + 1][0]
            if b > c:
                if b > a > c:
                    if e > f:
                        if e > d > f:
                            answer_list.append([d, a])
                    elif f > e:
                        if f > d > e:
                            answer_list.append([d, a])
            elif b < c:
                if c > a > b:
                    if e > f:
                        if e > d > f:
                            answer_list.append([d, a])
                    elif f > e:
                        if f > d > e:
                            answer_list.append([d, a])
        if second_list[bindex][0] == second_list[bindex + 1][0]:
            a = first_list[sindex][1]
            b = second_list[bindex][1]
            c = second_list[bindex + 1][1]
            d = second_list[bindex][0]
            e = first_list[sindex][0]
            f = first_list[sindex + 1][0]
            if b > c:
                if b > a > c:
                    if e > f:
                        if e > d > f:
                            answer_list.append([d, a])
                    elif f > e:
                        if f > d > e:
                            answer_list.append([d, a])
            elif b < c:
                if c > a > b:
                    if e > f:
                        if e > d > f:
                            answer_list.append([d, a])
                    elif f > e:
                        if f > d > e:
                            answer_list.append([d, a])
answer = abs(answer_list[0][0]) + abs(answer_list[0][1])
for item in answer_list:
    helper = abs(item[0]) + abs(item[1])
    if helper < answer:
        answer = helper

print(answer)





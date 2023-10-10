import os

list_x = [i for i in range(2, 7)], [i for i in range(2, 5)][::-1],['б','в','г','д'][::-1]

def create_list(list_x):
    x = list_x[0]
    list_answer = []
    for i in list_x[1:]:
        list_answer.append(f'{x}-{i}')
        x = i
    return list_answer

[os.makedirs(os.path.join('Этап_1', f'ось_{i}')) for i in create_list(list_x[0])]
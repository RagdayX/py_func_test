import os

axes = [[i for i in range(2, 24)], [i for i in range(2, 24)][::-1], ['б','в','г','д'], ['б','в','г','д'][::-1]]
stage_1 = [[i for i in range(2, 7)], [i for i in range(2, 5)][::-1],['б','в','г','д'][::-1]]



def create_folders(list_x:list, name_folder:str='folder'):
    for i in list_x:
        os.mkdir(f'{name_folder}_{i}')

def create_list(list_x):
    x = list_x[0]
    list_answer = []
    for i in list_x[1:]:
        list_answer.append(f'{x}-{i}')
        x = i
    return list_answer

def main(stage):
    x = input('Вы хотите создать папку?(да/нет)\n:')
    if x == 'да':
        name = 'этап'
        num = input('Введите номер папки: ')
        create_folders([num], name)
        os.chdir(f'{name}_{num}')
        print(f'Вы в папке {name}_{num}')
        floor = int(input('Введите сколько создать папок: '))
        name = 'этаж'
        create_folders(range(1, floor+1), name)
        list_x = os.listdir()
        for i in list_x:
            os.chdir(i)
            for el in stage:
                create_folders(create_list(el), 'в_осях')
            os.chdir('..')


if __name__ == '__main__':
    main(stage_1)

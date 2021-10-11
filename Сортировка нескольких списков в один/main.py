def quick_merge(listoflists):                                              #На вход функции даётся список списков
    res = []                                                               #Создание переменной, которую вернёт функция

    while len([j for i in listoflists for j in i]) > 0:                    #условие цикла: если длина списка списков становится нулевой, то цикл заканчивается
        comparison = [listoflists[i][0] for i in range(len(listoflists))]  #создание переменной, содержащей 0-ые элементы каждого списка
        res += [min(comparison)]                                           #добавление в результирующую переменную наименьшего из трёх числа
        listoflists[comparison.index(min(comparison))].pop(0)              #удаление первого элемента списка, содержащего наименьший первый элемент
        if len(listoflists[comparison.index(min(comparison))]) <= 0:       #если длина списка становится нулевой, то выполняется if
            listoflists.pop(comparison.index(min(comparison)))             #удаление нулевого списка

    return res                                                             #возвращение результата

n = [[int(i) for i in input().split()] for _ in range(int(input()))]       #создание списка со списками
print(*quick_merge(n))                                                     #вывод на экран суммарного списка
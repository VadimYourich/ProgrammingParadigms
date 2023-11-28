""" Задача №1.
Дан список целых чисел numbers. 
Необходимо написать в императивном стиле процедуру для
сортировки числа в списке в порядке убывания.
Можно использовать любой алгоритм сортировки. """


def sort_list_imperative(numbers):
    length = len(numbers)
    for i in range(length-1):
        for j in range(length-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    print(numbers)

print('\nIn the imperative style:')
numbers = [3, 3, 4, 1, 0, 7, 8]
print(numbers)
sort_list_imperative(numbers)


""" Задача №2.
Написать точно такую же процедуру, но в декларативном стиле. """

def sort_list_declarative(numbers):   
    numbers.sort(reverse=True)
    print(numbers)

print('\nIn declarative style:')
numbers2 = [3, 3, 4, 1, 0, 7, 8]
print(numbers2)
sort_list_declarative(numbers2)
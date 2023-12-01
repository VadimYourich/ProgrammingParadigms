""" Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами). Можете
использовать любую парадигму, но рекомендую использовать
функциональную, т.к. в этом примере она значительно
упростит вам жизнь. """

import math

def pearsonCorrelation(array_1, array_2):

    # array_1, array_2 - массивы значений
    # Проверка на то, что массивы одинаковой длины
    if len(array_1) != len(array_2):
        raise ValueError("Массивы должны быть одинаковой длины")

    n = len(array_1)

    # Расчет среднего значения
    mean_x = sum(array_1) / n
    mean_y = sum(array_2) / n

    variance_x = sum([(xi - mean_x) ** 2 for xi in array_1]) / float(len(array_1))
    variance_y = sum([(yi - mean_y) ** 2 for yi in array_2]) / float(len(array_2))

    covariance = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(array_1,array_2)]) / float(len(array_1)) 
    correlation = covariance / (math.sqrt(variance_x * variance_y))

    return correlation

array_1 = [3,3,5,4,6,3,8]
array_2 = [2,4,8,7,5,6,5]

correlation = round(pearsonCorrelation(array_1, array_2),4)
print(f"Корреляция Пирсона: {correlation}")
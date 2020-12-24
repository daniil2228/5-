# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_06_02_04.
#
# Выполнил: Солодухин Даниил
# Группа: АДЭУ-201

# алгоритм ищет числа от 1 до введенного пользователем, которые делятся только на 1 или на себя
# сложность O(N+2)


def foo(n):
    res = []
    for i in range(1, n + 1): #O(N)
        divisors = 0 #O(1)
        j = 2 #O(1)
        while j < i and divisors == 0: #O(1)
            if i % j == 0: #O(1)
                divisors += 1 #O(1)
            j += 1 #O(1)

        if divisors == 0: #O(1)
            res.append(i) #O(1)

    return res
print(foo(99))
#(O(N)+O(1)+O(1))*((O(1)*(O(1)+O(1)+O(1))+O(1)+O(1))=O((N+2)*(3+2))=O(5*(N+2))=O(N+2)

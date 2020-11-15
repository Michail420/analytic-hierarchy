import numpy as np
def vector(matrix):
    """Функция вычисляющая приоритетный вектор"""
    vect = matrix[:, 0]
    w = vect / vect.sum()
    return w

def matrix(number):
    """Функция для создания парной матрицы """
    A = np.ones([number, number])
    importance = [i for i in range(1, 10)] # список допустимых значений важности

    for i in range(0, number):
        for j in range(0, number):
            if i < j:
                a = str(input(f'На сколько критерий {i+1} Важнее чем {j+1}? Введите целое число от 1 до 9: '))
                if a.isdigit() and float(a) in importance: # обработка ошибок
                    A[i,j] = float(a)
                    A[j, i] = 1 / float(a)
                else:
                    print("Ошибка. Попробуйье еще раз. \n")
                    main()
    return A

def main():
    number = str(input("Сколько критериев вы хотите ввести? Введите целое число: "))
    if number.isdigit(): # обработка ошибок
        A = matrix(int(number))
        weights = vector(A)
        for i in range(len(weights)):
            print(f'Критерий {i+1} = {np.round(weights[i], 2)}')
    else:
        print("Ошибка. Попробуйье еще раз. \n")
        main()


if __name__ == "__main__":
    main()


import math
import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings(action='once')


# обобратка ошибок 1) лог от 0 2) сущ единственного решения
def log_list(list_a):
    log_list_a = []
    for element in list_a:
        log_list_a.append(math.log(element))

    return log_list_a


def import_data(file_path):
    list_of_data = []
    with open(file_path, "r") as reader:
        for line in reader:
            list_of_data.append(float(line.split()[0]))
    return list_of_data


def the_least_squares_method_for_a_linear_function(list_of_y, list_of_x):
    number_of_elements = len(list_of_y)
    iterator = 0
    matrix_A = ([0, 0, 0], [0, 0, 0])
    while iterator < number_of_elements:
        matrix_A[0][0] += list_of_x[iterator] ** 2
        matrix_A[0][1] += list_of_x[iterator]
        matrix_A[0][2] += list_of_x[iterator] * list_of_y[iterator]
        matrix_A[1][0] += list_of_x[iterator]
        matrix_A[1][1] = number_of_elements
        matrix_A[1][2] += list_of_y[iterator]
        iterator += 1

    matrix_determinant = matrix_A[0][0] * matrix_A[1][1] - matrix_A[0][1] * matrix_A[1][0]
    if matrix_determinant != 0:  # Cramer's method has one solution
        a = round((matrix_A[0][2] * matrix_A[1][1] - matrix_A[0][1] * matrix_A[1][2]) / matrix_determinant, 2)
        b = round((matrix_A[0][0] * matrix_A[1][2] - matrix_A[0][2] * matrix_A[1][0]) / matrix_determinant, 2)
        return a, b

    return 0


def matrix_determinant_by_three(matrix_of_size_three):
    return round(float(matrix_of_size_three[0][0] * matrix_of_size_three[1][1] * matrix_of_size_three[2][2] + \
                       matrix_of_size_three[0][1] * matrix_of_size_three[1][2] * matrix_of_size_three[2][0] + \
                       matrix_of_size_three[0][2] * matrix_of_size_three[1][0] * matrix_of_size_three[2][1] - \
                       matrix_of_size_three[0][2] * matrix_of_size_three[1][1] * matrix_of_size_three[2][0] - \
                       matrix_of_size_three[0][0] * matrix_of_size_three[1][2] * matrix_of_size_three[2][1] - \
                       matrix_of_size_three[0][1] * matrix_of_size_three[1][0] * matrix_of_size_three[2][2]), 4)


def the_least_squares_method_for_a_quadratic_function(list_of_y, list_of_x):
    number_of_elements = len(list_of_y)
    iterator = 0
    matrix_A = ([0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0])
    while iterator < number_of_elements:
        matrix_A[0][0] += list_of_x[iterator] ** 4
        matrix_A[0][1] += list_of_x[iterator] ** 3
        matrix_A[0][2] += list_of_x[iterator] ** 2
        matrix_A[0][3] += (list_of_x[iterator] ** 2) * list_of_y[iterator]
        matrix_A[1][0] += list_of_x[iterator] ** 3
        matrix_A[1][1] += list_of_x[iterator] ** 2
        matrix_A[1][2] += list_of_x[iterator]
        matrix_A[1][3] += list_of_x[iterator] * list_of_y[iterator]
        matrix_A[2][0] += list_of_x[iterator] ** 2
        matrix_A[2][1] += list_of_x[iterator]
        matrix_A[2][2] = number_of_elements
        matrix_A[2][3] += list_of_y[iterator]
        iterator += 1

    matrix_by_three = [
        [matrix_A[0][0], matrix_A[0][1], matrix_A[0][2]], [matrix_A[1][0], matrix_A[1][1], matrix_A[1][2]],
        [matrix_A[2][0], matrix_A[2][1], matrix_A[2][2]]]
    matrix_determinant = matrix_determinant_by_three(matrix_by_three)
    if matrix_determinant != 0:  # Cramer's method has one solution
        matrix_by_three = (
            [matrix_A[0][3], matrix_A[0][1], matrix_A[0][2]], [matrix_A[1][3], matrix_A[1][1], matrix_A[1][2]],
            [matrix_A[2][3], matrix_A[2][1], matrix_A[2][2]])
        a = round(float(matrix_determinant_by_three(matrix_by_three) / matrix_determinant), 2)
        matrix_by_three = (
            [matrix_A[0][0], matrix_A[0][3], matrix_A[0][2]], [matrix_A[1][0], matrix_A[1][3], matrix_A[1][2]],
            [matrix_A[2][0], matrix_A[2][3], matrix_A[2][2]])
        b = round(float(matrix_determinant_by_three(matrix_by_three) / matrix_determinant), 2)
        matrix_by_three = (
            [matrix_A[0][0], matrix_A[0][1], matrix_A[0][3]], [matrix_A[1][0], matrix_A[1][1], matrix_A[1][3]],
            [matrix_A[2][0], matrix_A[2][1], matrix_A[2][3]])
        c = round(float(matrix_determinant_by_three(matrix_by_three) / matrix_determinant), 2)
        return a, b, c

    return 0


def linear_function(list_of_y, list_of_x):
    list_of_linear_function_values = []
    a, b = the_least_squares_method_for_a_linear_function(list_of_y, list_of_x)  # y = ax + b
    for x in list_of_x:
        list_of_linear_function_values.append(round(a * x + b, 2))
    return list_of_linear_function_values, a, b


def degree_function(list_of_y, list_of_x):
    list_of_degree_function_values = []
    log_list_of_x = log_list(list_of_x)
    log_list_of_y = log_list(list_of_y)
    log_a, log_b = the_least_squares_method_for_a_linear_function(log_list_of_y, log_list_of_x)
    log_b = round(math.exp(log_b), 2)
    for x in list_of_x:  # y = b * x^a
        list_of_degree_function_values.append(round(log_b * x ** log_a, 2))
    return list_of_degree_function_values, log_a, log_b


def exponential_function(list_of_y, list_of_x):
    list_of_exponential_function_values = []
    log_list_of_y = log_list(list_of_y)
    poc_a, poc_b = the_least_squares_method_for_a_linear_function(log_list_of_y, list_of_x)
    poc_b = round(math.exp(poc_b), 2)
    for x in list_of_x:  # y = b * exp^ax
        list_of_exponential_function_values.append(round(poc_b * math.exp(x * poc_a), 2))
    return list_of_exponential_function_values, poc_a, poc_b


def quadratic_function(list_of_y, list_of_x):
    list_of_quadratic_function_values = []
    a, b, c = the_least_squares_method_for_a_quadratic_function(list_of_y, list_of_x)  # y = ax + b
    for x in list_of_x:
        list_of_quadratic_function_values.append(round(a * x ** 2 + b * x + c, 2))
    return list_of_quadratic_function_values, a, b, c


def error_rate(list_of_y, list_of_z):
    ans = 0
    number_of_elements = len(list_of_y)
    iterator = 0
    while iterator < number_of_elements:
        ans += (list_of_y[iterator] - list_of_z[iterator]) ** 2
        iterator += 1
    return round(ans, 4)


if __name__ == '__main__':
    main_list_of_x = import_data("import_data_x.txt")
    main_list_of_y = import_data("import_data_y.txt")

    z_lin, a_lin, b_lin = linear_function(main_list_of_y, main_list_of_x)
    z_deg, a_deg, b_deg = degree_function(main_list_of_y, main_list_of_x)
    z_exp, a_exp, b_exp = exponential_function(main_list_of_y, main_list_of_x)
    z_quad, a_quad, b_quad, c_quad = quadratic_function(main_list_of_y, main_list_of_x)

    dict_of_error = {"Линейная функция": error_rate(main_list_of_y, z_lin),
                     "Степенная функция": error_rate(main_list_of_y, z_deg),
                     "Показательная функция": error_rate(main_list_of_y, z_exp),
                     "Квадратичная функция": error_rate(main_list_of_y, z_quad)}

    print(
        f"\nЛинейная функция.\t\tПогрешность:\t {dict_of_error['Линейная функция']}\tПараметры:\ta = {a_lin}\tb = {b_lin}"
        f"\nСтепенная функция.\t\tПогрешность:\t {dict_of_error['Степенная функция']}\tПараметры:\ta = {a_deg}\tb = {b_deg}"
        f"\nПоказательная функция.\tПогрешность:\t {dict_of_error['Показательная функция']}\tПараметры:\ta = {a_exp}\tb = {b_exp}"
        f"\nКвадратичная функция.\tПогрешность:\t {dict_of_error['Квадратичная функция']}\tПараметры:\ta = {a_quad}\tb = {b_quad}\tc = {c_quad}"
        f"\n\nВ данной задаче лучшей аппроксимирующей функцией является: {min(dict_of_error, key=dict_of_error.get)}")

    plt.figure(figsize=(10, 5))
    plt.plot(main_list_of_x, main_list_of_y, 'ro')
    plt.plot(main_list_of_x, z_lin, label=r'$f_1(x)=ax+b$')  # Линейная функция
    plt.plot(main_list_of_x, z_deg, label=r'$f_2(x)=bx^a$')  # Степенная функция
    plt.plot(main_list_of_x, z_exp, label=r'$f_3(x)=be^{ax}$')  # Показательная функция
    plt.plot(main_list_of_x, z_quad, label=r'$f_4(x)=ax^2+bx+c$')  # Квадратичная функция
    plt.xlabel(r'$x$', fontsize=14)
    plt.ylabel(r'$f(x)$', fontsize=14)
    plt.grid(True)
    plt.legend(loc='best', fontsize=12)
    plt.savefig('figure_with_legend.png')
    plt.show()

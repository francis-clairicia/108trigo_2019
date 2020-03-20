# -*- coding: Utf-8 -*

from matrix import Matrix

MAX_ITERATION = 100

def factorial(n: int):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def my_exp(matrix: Matrix):
    result = Matrix(matrix.lines, matrix.columns)
    for i in range(MAX_ITERATION + 1):
        result += (matrix ** i) * (1 / factorial(i))
    return result

def my_cos(matrix: Matrix):
    result = Matrix(matrix.lines, matrix.columns)
    for i in range(MAX_ITERATION + 1):
        result += (matrix ** (2 * i)) * pow(-1, i) * (1 / factorial(2 * i))
    return result

def my_sin(matrix: Matrix):
    result = Matrix(matrix.lines, matrix.columns)
    for i in range(MAX_ITERATION + 1):
        result += (matrix ** (2 * i + 1)) * pow(-1, i) * (1 / factorial(2 * i + 1))
    return result

def my_cosh(matrix: Matrix):
    result = Matrix(matrix.lines, matrix.columns)
    for i in range(MAX_ITERATION + 1):
        result += (matrix ** (2 * i)) * (1 / factorial(2 * i))
    return result

def my_sinh(matrix: Matrix):
    result = Matrix(matrix.lines, matrix.columns)
    for i in range(MAX_ITERATION + 1):
        result += (matrix ** (2 * i + 1)) * (1 / factorial(2 * i + 1))
    return result
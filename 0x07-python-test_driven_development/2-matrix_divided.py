<<<<<<< HEAD
#!/usr/bin/python3

def matrix_divided(matrix, div):

    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

=======
#!/usr/bin/python3


def matrix_divided(matrix, div):

    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
>>>>>>> 38492aa2f652bda047895a4871f5a072d0aa3090

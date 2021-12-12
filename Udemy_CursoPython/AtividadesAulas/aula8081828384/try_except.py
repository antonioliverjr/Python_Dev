def divide(n1, n2):
    # if n2 == 0:
    #     raise ValueError('n2 não pode ser igual a zero.')
    # return n1 / n2
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log: ', error)
        raise

try:
    print(divide(2, 0))
except Exception as error:
    print(error)
# try:
#     print(divide(2, 0))
# except ZeroDivisionError as error:
#     print(error)
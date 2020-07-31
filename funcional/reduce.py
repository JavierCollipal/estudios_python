import functools

listForReduce = [1, 2, 3, 4, 5]


# investigar sobre lambdas
def test_basic_reduce():
    print(functools.reduce(lambda a, b: a + b, listForReduce))

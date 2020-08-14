if __name__ == '__main__':

    def evaluate_print(i, number):
        if i < number:
            print(i * i)


    def print_less_range(number):

        for i in range(number):
            evaluate_print(i, number)


    n = int(input())
    print_less_range(n)

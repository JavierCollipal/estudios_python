def gregorian_rules_evaluator(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 == 0:
        return False


def is_leap(year):
    return gregorian_rules_evaluator(year)


year = int(input())

is_leap(year)

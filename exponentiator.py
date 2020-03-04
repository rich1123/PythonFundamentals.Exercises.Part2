def exponentiate(a, b):
    return a ** b


"""function for raising input number to a given power """


def raise_to_fourth_power(a):
    return exponentiate(a, 4)


""""takes single param to pass through exponeniate function to give param power to 4th value"""


square = lambda x: x ** 2;

cube = lambda x: x ** 3;


"""square and cube are lambdas(inline functions loaded into variables; scope isn't global"""


print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))
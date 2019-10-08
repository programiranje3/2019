"""The very first module in a more structured version of the project.
"""

# A simple function


def print_woodstock(location, year):
    """The docstring of print_woodstock().
    """
    print('Woodstock was held in {}, in {}.'.format(location, year))


if __name__ == '__main__':

    # Hello world: the print() built-in function and the + operator

    # print('Woodstock ' + 'was held in ' + str(1969))
    # print('Woodstock was held in', 1969)
    # print('Woodstock was held in {}, in {}.'.format(1969, 'Bethel'))
    # print()

    # Printing with classical formatting (%)

    print('%d %s %5.2f' % (12, 'Woodstock', 13.2))

    # The input() built-in function

    # woodstock = input('Woodstock was held in: ')
    # print(woodstock)
    # print('Woodstock was held in: ', end='')
    # woodstock = input()
    # print(woodstock)
    # print()

    # A simple function and function call

    print_woodstock('Bethel', 1969)

    # Taking care of the module __name__

    print(__name__)

    # A simple loop and the range() built-in function

    for i in range(5):
        # if i == 2:
        #     break
        # if i == 2:
        #     continue
        print(i)

    # A simple list, accessing list elements, printing lists

    woodstock_list = ['Woodstock', 1969, 'Bethel']
    print(woodstock_list)
    print(type(woodstock_list[2]))
    print(woodstock_list[1])
    print(woodstock_list[-1])
    print(woodstock_list[1:-1])
    print(woodstock_list[1:])

    # Looping through list elements - for and enumerate()

    for i in woodstock_list:
        print(i)
    print()

    # Printing a list using enumerate()
    print(enumerate(woodstock_list))
    print(list(enumerate(woodstock_list)))
    for e in enumerate(woodstock_list):
        print(e)
    for i, v in enumerate(woodstock_list):
        print(i, v)
        print(str(i) + ':', v)

    # Global variables: __name__, __file__, __doc__,...

    print(__name__)
    print(__file__)
    # Printing docstrings
    print(print_woodstock.__doc__)







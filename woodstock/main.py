# # Hello world: the print() built-in function and the + operator
#
# print('Woodstock ' + 'was held in ' + str(1969))
# print('Woodstock was held in', 1969)
# print('Woodstock was held in {}, in {}.'.format(1969, 'Bethel'))
# print()
#
#
# # The input() built-in function
#
# # woodstock = input('Woodstock was held in: ')
# # print(woodstock)
# # print('Woodstock was held in: ', end='')
# # woodstock = input()
# # print(woodstock)
# # print()
#
# # A simple function and function call
#
#
# def print_woodstock(location, year):
#     """The docstring of print_woodstock().
#     """
#     print('Woodstock was held in {}, in {}.'.format(location, year))
#
#
# print_woodstock('Bethel', 1969)
#
#
# # A simple loop and the range() built-in function
#
#
# # A simple list, accessing list elements, printing lists
#
#
# # Looping through list elements - for and enumerate()
#
#
# # Global variables: __name__, __file__, __doc__,...
#

from woodstock.python import inception

inception.print_woodstock('Bethel', 1969)
print(__name__)
print(inception.__name__)

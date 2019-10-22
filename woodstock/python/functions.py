"""Demonstrates details of writing Python functions: annotations, default args, kwargs
"""


# def demonstrate_annotations(festival, year=1969):
def demonstrate_annotations(festival: str, year: int = 1969) -> str:
    """Demonstrates how to use annotations of
    function parameters/arguments (<arg>: <type>) and of function return type (def f(...) -> <type>:).
    """

    # Print the function parameters/arguments
    print(festival + ',', year)
    print()

    # Print the value of the __annotations__ attribute of this function
    print(demonstrate_annotations.__annotations__)
    print()

    # Print the name and the docstring of this function
    print(demonstrate_annotations.__name__ + ':')
    print(demonstrate_annotations.__doc__)
    print()

    # Return a formatted string (including function parameters/arguments)
    return f'Just called {demonstrate_annotations.__name__}({festival}, {year})'


def show_festival(name, year=1969, location='Bethel'):
    """Demonstrates default arguments/parameters.
    """

    # Print the function arguments/parameters in one line
    print(f'{name}:', f'{year}, {location}')


def use_flexible_arg_list(prompt: str, *headliners):
    """Demonstrates flexible number of arguments/parameters.
    """

    # Print the prompt and the list of festival headliners in one line
    # print(f'{prompt}:',
    #       f'{headliners}')
    # print(f'{prompt}:',
    #       f'{list(headliners)}')
    # print(f'{prompt}:',
    #       ', '.join(list(headliners)))
    # print(f'{prompt}:',
    #       ', '.join(list(headliners)) + ',...')
    print(f'{prompt}:' if headliners else f'{prompt}',
          ', '.join(list(headliners)) + ',...' if headliners else '')


def use_all_categories_of_args(prompt, *headliners, year=1969, **location_details):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    """

    # Print all arguments/parameters, including the keyword arguments/parameters, in one line
    print(f'{prompt}: ' + ', '.join(headliners) + ',...' if headliners else f'{prompt}',
          f'({year})' if not location_details else f'({year}, ' + ', '.join([v for v in location_details.values()]) + ')')


if __name__ == "__main__":

    # pass
    # print(demonstrate_annotations('Woodstock'))
    # print(demonstrate_annotations('Monterey Pop', 1967))
    # print(demonstrate_annotations('Monterey Pop', year=1967))
    # print()

    # show_festival('Isle of Wight Festival', year=1970, location='Isle of Wight')
    # show_festival('Woodstock')
    # print()

    # headliners = ['Jimi Hendrix', 'Jefferson Airplane', 'Grateful Dead']
    # # headliners = []
    # use_flexible_arg_list('Woodstock', *headliners)

    # headliners = ['Jimi Hendrix', 'Jefferson Airplane', 'Grateful Dead']
    headliners = []
    use_all_categories_of_args('Woodstock', *headliners, year=1969, place='Bethel', state='NY')


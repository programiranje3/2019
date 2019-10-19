"""Demonstrates details of writing Python functions: annotations, default args, kwargs
"""


def demonstrate_annotations(festival, year=1969):
    """Demonstrates how to use annotations of
    function parameters/arguments (<arg>: <type>) and of function return type (def f(...) -> <type>:).
    """

    # Print the function parameters/arguments
    print()

    # Print the value of the __annotations__ attribute of this function
    print()

    # Print the name and the docstring of this function
    print()

    # Return a formatted string (including function parameters/arguments)


def show_festival(name, year=1969, location='Bethel'):
    """Demonstrates default arguments/parameters.
    """

    # Print the function arguments/parameters in one line


def use_flexible_arg_list(prompt: str, *headliners):
    """Demonstrates flexible number of arguments/parameters.
    """

    # Print the prompt and the list of festival headliners in one line


def use_all_categories_of_args(prompt, *headliners, year=1969, **location_details):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    """

    # Print all arguments/parameters, including the keyword arguments/parameters, in one line


if __name__ == "__main__":

    pass
    # demonstrate_annotations('Woodstock')
    # demonstrate_annotations('Monterey Pop', 1967)
    # demonstrate_annotations('Monterey Pop', year=1967)
    # print()



"""Demonstrates dictionaries
From: https://qr.ae/TWCAvj:
Python uses dictionaries all over the place:
- the variables and functions in a module - stored in a dictionary
- the local variables in a function - stored in a dictionary
- the implementation of a function - a dictionary
- a class is a dictionary
- an instance of a class is another dictionary
- the modules your program has imported - you guessed it - another dictionary
- even Python set objects are implemented as modified dictionaries
To paraphrase Tim Peter's 'Zen of Python': "dictionaries are great - let's do more of them".
Read more at https://qr.ae/TWCAvj.
"""


def demonstrate_dictionaries():
    """Creating and using dictionaries.
    """

    # Create a blank (empty) dictionary
    w = dict()
    w = {}
    print(w)
    print(type(w))
    print()

    # create a non-empty dictionary
    w = {'name': 'Woodstock', 'year': 1969}
    print(w)
    print()

    # Print a non-empty dictionary
    #   - print all items using the items() function
    #   - print one item per line
    print(w.items())
    for k, v in (w.items()):
        print(str(k) + ':', v)
    print()

    # pprint dictionary in one column
    from pprint import pprint
    pprint(w, width=1)
    print()

    # Add/Remove items to/from a dictionary
    w['location'] = 'Bethel'
    print(w)
    del w['location']
    print(w)
    print()

    # Update a dictionary with the items from another dictionary or from an iterable of (k, v) pairs using dict.update()
    w1 = {'location': 'Bethel', 'date': 'Aug 15-18'}
    w.update(w1)
    print(w)
    # w1 = {'location': 'Bethel, NY', 'date': 'Aug 15-18'}
    # w.update(w1)
    w1 = (('location', 'Bethel, NY'), ('date', 'Aug 15-18'))
    w.update(w1)
    print(w)
    print()

    # Using the keys() and values() functions
    print(w.keys())
    print(w.values())
    print(list(w.keys()))
    print(list(w.values()))
    print()


def sort_dictionary(d, by):
    """Sorting a dictionary by keys or by values.
    """

    # # using zip()
    # if by == 'k':
    #     return dict(sorted(zip(d.keys(), d.values())))
    # elif by == 'v':
    #     return dict(sorted(zip(d.values(), d.keys())))
    # else:
    #     return None

    # # using operator.itemgetter()
    # from operator import itemgetter
    # if by == 'k':
    #     return dict(sorted(d.items(), key=itemgetter(0)))
    # elif by == 'v':
    #     return dict(sorted(d.items(), key=itemgetter(1)))
    # else:
    #     return None

    # using lambda
    if by == 'k':
        return dict(sorted(d.items(), key=lambda item: item[0]))
    elif by == 'v':
        return dict(sorted(d.items(), key=lambda item: item[1]))
    else:
        return None


def demonstrate_dict_sorting():
    """Demonstrate sorting a dictionary.
    """

    w = {'name': 'Woodstock', 'year': '1969'}
    w1 = {'location': 'Bethel', 'date': 'Aug 15-18'}
    w.update(w1)
    print(sort_dictionary(w, 'k'))
    print(sort_dictionary(w, 'v'))
    print(sort_dictionary(w, '576'))


if __name__ == '__main__':

    # pass
    # demonstrate_dictionaries()
    demonstrate_dict_sorting()


"""Demonstrates sets
"""


def demonstrate_sets():
    """Creating and using sets.
    """

    # Create a set with an attempt to duplicate items
    w = {'Woodstock', 1969, 'Bethel', 1969}
    print(w)
    print(type(w))
    print()

    # Demonstrate some of the typical set operators:
    #     & (intersection)
    #     | (union)
    #     - (difference)
    #     ^ (disjoint)
    print(w & {'Woodstock', 'Aug 15-18', 'groovy'})
    print(w | {'Woodstock', 'Aug 15-18', 'groovy'})
    print(w - {'Woodstock', 'Aug 15-18', 'groovy'})
    print(w ^ {'Woodstock', 'Aug 15-18', 'groovy'})
    print()


if __name__ == '__main__':

    # pass
    demonstrate_sets()


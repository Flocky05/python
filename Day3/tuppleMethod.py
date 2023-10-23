""" A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list. """


""" why we use tupple over list as they are almost same

We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
Since tuples are immutable, iterating through a tuple is faster than with a list. So there is a slight performance boost.
Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

 """


def multiple():
    return 3, 4


things = 'alu', 'badam', 'lebu', 'tomato'
print(things)

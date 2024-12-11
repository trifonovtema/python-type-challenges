"""
TODO:

The function `add` accepts two arguments and returns a value, they all have the same type.
The type can only be str or int.
"""


def add[T: (str, int)](a: T, b: T) -> T:
    return b


from typing import assert_type

assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)

# add(["1"], ["2"])  # expect-type-error
# add("1", 2)  # expect-type-error

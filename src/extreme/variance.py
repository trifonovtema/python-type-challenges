"""
TODO: Annotate function `f` and `g`, to make tests pass.
"""

"""
TODO: Annotate function `f` and `g`, to make tests pass.
"""
from typing import Sequence, List


def f(a: List[int | str]):
    pass


# def g(a:List[int]|List[int|str]|str|bytes|Tuple[int,str,int]):
#     pass


def g(a: Sequence[int | str]):
    pass


l1: list[int] = [1, 2]
# f(l1)  # expect-type-error
g(l1)

l2: list[int | str] = [1, 2]
f(l2)
g(l2)

# f(1)  # expect-type-error
# f("abc")  # expect-type-error
g("abc")
g(b"abc")
g([1, "2"])
g((1, "2", 3))
# g(1)  # expect-type-error
# g({1})  # expect-type-error

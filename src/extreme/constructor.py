"""
TODO:

Define a decorator `constructor_parameter` that accepts the type of Foo.
and return a wrapper function with the same signature as the constructor of Foo,
and function decorated by `constructor_parameter` can be called with an instance of Foo.
"""

from typing import Callable


def constructor_parameter[ # type:ignore
    **P, T, R
](cls: Callable[P, T],) -> Callable[[Callable[[T], R]], Callable[P, R]]:
    ...


from typing import Any


class Foo:
    a: int
    b: str

    def __init__(self, a: int, b: str) -> None: ...


@constructor_parameter(Foo)
def func_pass(foo: Foo) -> list[Foo]:  # type:ignore
    ...


res = func_pass(1, "2")
res[0].a.bit_length()
res[0].b.upper()


@constructor_parameter(Foo)
def func_fail(foo: Foo) -> list[Any]:  # type:ignore
    ...


# func_fail("1", "2")  # expect-type-error
# func_fail([1, 2, 3])  # expect-type-error

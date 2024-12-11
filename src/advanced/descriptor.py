"""
TODO:

Create a descriptor and annotate the __get__ method.
"""

from typing import overload, Any, Self


class Descriptor:
    @overload
    def __get__(self, instance: None, owner: type) -> Self: ...

    @overload
    def __get__(self, instance: Any, owner: type) -> str: ...

    def __get__(self, instance: Any, owner: type) -> Self | str:
        return self if instance is None else "1"


class TestClass:
    a = Descriptor()


def descriptor_self(x: Descriptor) -> None: ...


def string_value(x: str) -> None: ...


descriptor_self(TestClass.a)
string_value(TestClass().a)
# descriptor_self(TestClass().a)  # expect-type-error
# string_value(TestClass.a)  # expect-type-error

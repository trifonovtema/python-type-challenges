"""
TODO:

`return_self` should return an instance of the same type as the current enclosed class.
"""

from typing import TypeVar, Self

T = TypeVar("T", bound="Foo")


class Foo:
    def return_self(self: T) -> T:
        return self


#
# class Foo:
#     def return_self(self)->Self:
#         ...


class SubclassOfFoo(Foo):
    pass


f: Foo = Foo().return_self()
sf: SubclassOfFoo = SubclassOfFoo().return_self()

# sf: SubclassOfFoo = Foo().return_self()  # expect-type-error

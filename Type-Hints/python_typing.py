
# mypy: static code analysis tool.
# x: str = 1

# def add_numbers(a: int, b: int, c: int) -> int:
#     return a + b + c

# x = add_numbers(1, 2, 3)
# print(x)

# 
from typing import List
x: List[List[int]] = [[1, 2], [3, 4]]

from typing import Dict
x: Dict[str, str] = {
    "a": "b"
}

from typing import Set
x: Set[float] = {"a", "b"}

from typing import Vector
Vector = List[float]


def foo(v: Vector) -> Vector:
    print(v)

foo()

Vector = List[Vector]
def foo(v: Vector) -> Vector:
    pass

foo()

# 
from typing import Optional
def foo(output: Optional[bool] = False):
    pass

foo()

from typing import Any
def foo(output: Any):
    pass

foo()

# 
from typing import Sequence
def foo(seq: Sequence[str]):
    ...

foo(("a", "b", "c"))
foo(["a", "b", "c"])

from typing import Tuple
x: tuple[int, int, int] = (1, 2, 3, "hello")

# callable -> when we want to accept the function as a parameter. 
from typing import Callable

def add(x: int, y: int) -> int:
    return x + y

def foo(func: Callable[[int, int, Optional[int]], int]):
    func(1, 2)

foo(add)

# 
def foo() -> Callable[[int, int], int]:
    def add(x: int, y: int) -> int:
        return x + y
    
    return add

foo()

# 
def foo() -> Callable[[int, int], int]:
    func: Callable[[int, int], int] = lambda x, y: x + y
    return func

foo()

# Generic. 
from typing import TypeVar

T = TypeVar("T")

def get_item(lst: List[T], index: int) -> T:
    return lst[index]

get_item()

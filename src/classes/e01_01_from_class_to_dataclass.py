
""" Original code for exercise 1
class A:
  def __init__(self) -> None:
    self._length = 0

class B:
  def __init__(self, x: int, y: str = "hello", l: list[int] | None = None) -> None:
    self.x = x
    self.y = y
    self.l = [] if not l else l

class C:
  def __init__(self, a: int = 3) -> None:
    self.a = a
    self.b = a + 3

"""

# Exercise 1
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class A:
  __length: int = field(default=0, init=False)

@dataclass
class B:
  x: int
  y: str = "hello"
  l: list[int] = field(default_factory=list)


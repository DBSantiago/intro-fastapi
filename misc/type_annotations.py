"""
    This is an introduction to type annotations.
    We can insert type annotations on:
    - Variables
    - Functions and Methods
    - Classes
    - Collections
"""
from typing import List, Tuple, Dict

sentence: str = "Hi, this is a string"
integer: int = 30
decimal: float = 3.14
boolean: bool = True

my_list: List[int] = [8, 9, 10]
my_paragraph: List[str] = [sentence, sentence, sentence]

my_tuple: Tuple[str, str, str] = ("localhost", "3306", "root")

my_dict: Dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3
}


def sum_two_numbers(num1: int, num2: int) -> int:
    return num1 + num2


def average(numbers: List[int]) -> float:
    return sum(numbers) / len(numbers)


class User:
    """
        Represents a user.
    """

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def say_hello(self) -> str:
        return f"Hello, {self.username}!"

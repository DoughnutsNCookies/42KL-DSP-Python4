import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student Class"""
    name: str = ""
    surname: str = ""
    active: bool = True
    login: str = ""
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Post init method"""
        self.name = self.name
        self.surname = self.surname
        self.login = (self.name[0] + self.surname)

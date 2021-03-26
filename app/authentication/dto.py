from dataclasses import dataclass


@dataclass
class UserDTO:
    email: str
    username: str
    password: str

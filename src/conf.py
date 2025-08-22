from dataclasses import dataclass

@dataclass(frozen=True)
class conf:
    a : int = 16
    b : int = 4

import formulaTypes as ft
from queue import LifoQueue as Stack
from enum import Enum

class StateStatus(Enum):
    Failure = 0 # formula is not in assumptions and we have reached maximum proof depth
    InProgress = 1 # formula is not in assumptions, but we havent reached maximum proof depth yet 
    Success = 2 # formula is in assumptions

class SingleState:
    def __init__(self, f: ft.Formula, assumptions: Stack[ft.Formula] = [], depth: int = 0) -> None:
        assert issubclass(type(f), ft.Formula), "f is not a subclass of Formula!"
        assert isinstance(depth, int) and depth >= 0, "depth must be non-negative integer!"
        self.formulaToBeProved = f
        self.assumptions = assumptions
        self.depth = depth
        self.stateStatus = StateStatus.InProgress
        # todo: ???

class Proof:
    def __init__(self, f: ft.Formula, maxLeafs: int) -> None:
        assert issubclass(type(f), ft.Formula), "f is not a subclass of Formula!"
        assert isinstance(maxLeafs, int) and maxLeafs >= 1, "Maximum amount of leafs allowed must be positive integer!"
        self.stack: Stack[SingleState] = Stack(maxLeafs)
        self.stack.put_nowait(SingleState(f))
        # todo: ???
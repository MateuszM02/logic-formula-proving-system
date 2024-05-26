import formulaTypes as ft
import proof
from random import choice

class Network: # to be done
    def __init__(self) -> None:
        f = ft.Disjunction(ft.Variable("p"), ft.Negation(ft.Variable("p")))
        p = proof.Proof(f, 3, 3)
        self.move(p)

    def move(self, p: proof.Proof):
        status = proof.state.StateStatus.InProgress
        while status == proof.state.StateStatus.InProgress:
            moves = p.get_possible_moves()
            move = choice(moves)
            status = p.make_move(move)
            0

Network()
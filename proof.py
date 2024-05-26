import formulaTypes as ft
import introductionRules as irule
import eliminationRules as erule
import state
from queue import LifoQueue as Stack

class Proof:
    def __init__(self, f: ft.Formula, maxLeafs: int, maxDepth: int) -> None:
        assert issubclass(type(f), ft.Formula), "f is not a subclass of Formula!"
        assert isinstance(maxLeafs, int) and maxLeafs >= 1, "Maximum amount of leafs allowed must be positive integer!"
        assert isinstance(maxDepth, int) and maxDepth >= 1, "Maximum depth allowed must be positive integer!"
        
        self.stack: Stack[state.SingleState] = Stack(maxLeafs)
        self.stack.put_nowait(state.SingleState(f))
        self.maxDepth = maxDepth
        # todo: ???

    def get_possible_moves(self) -> list[ft.Rule]:
        formula = self.stack.queue[-1].formulaToBeProved
        match type(formula):
            case ft.TrueF:
                return []
            case ft.FalseF:
                return [erule.NegationElimination]
            case ft.Variable: # should there be irule.NegationIntroduction ???
                return [erule.ConjunctionElimination, erule.DisjunctionElimination,
                        erule.ImplicationElimination, erule.FalseElimination]
            case ft.Negation:
                return [irule.NegationIntroduction,
                        erule.ConjunctionElimination, erule.DisjunctionElimination,
                        erule.ImplicationElimination, erule.FalseElimination]
            case ft.Conjunction: # should there be irule.NegationIntroduction, erule.ConjunctionIntroduction, etc. ???
                return [irule.ConjunctionIntroduction]
            case ft.Disjunction: # should there be irule.NegationIntroduction, erule.ConjunctionIntroduction, etc. ???
                return [irule.DisjunctionIntroduction1, irule.DisjunctionIntroduction2]
            case ft.Implication: # should there be irule.NegationIntroduction, erule.ConjunctionIntroduction, etc. ???
                return [irule.ImplicationIntroduction]
            case _:
                raise f"unknown formula type: {self.stack.queue[-1].formulaToBeProved}"
            
    def make_move(self, rule: ft.Rule, alpha: ft.Formula=None, beta: ft.Formula=None) -> state.StateStatus:
        assert rule in self.get_possible_moves(), "picked invalid rule!"
        current_state = self.stack.get_nowait()

        if beta is not None:
            next_states: tuple[state.SingleState] = rule.use_rule(current_state, alpha, beta)
        elif alpha is not None:
            next_states: tuple[state.SingleState] = rule.use_rule(current_state, alpha)
        else:
            next_states: tuple[state.SingleState] = rule.use_rule(current_state)

        if (next_states[0].depth >= self.maxDepth):
            return state.StateStatus.Failure
        
        count = len(self.stack.queue)
        for new_state in next_states:
            if (count > self.stack.maxsize):
                return state.StateStatus.Failure
            if (not new_state.is_proven()):
                self.stack.put_nowait(new_state)
                count += 1

        return  state.StateStatus.Success \
                if count == 0 \
                else state.StateStatus.InProgress
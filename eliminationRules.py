import formulaTypes as ft
import state
from abc import abstractmethod
from copy import deepcopy

class NegationElimination(ft.Rule):
    @abstractmethod
    def __init__(self):
        pass

    def use_rule(current_state: state.SingleState, alpha: ft.Formula)->tuple[state.SingleState]:
        assert isinstance(current_state, state.SingleState), "Given argument is not a proof state!"
        assert isinstance(current_state.formulaToBeProved, ft.FalseF), "Formula not a False!"
        assert issubclass(type(alpha), ft.Formula), "Given argument is not a subclass of Formula!"
        
        new_state1 = state.SingleState(
            alpha,
            current_state.assumptions,
            current_state.depth + 1)
        
        new_state2 = state.SingleState(
            ft.Negation(alpha),
            current_state.assumptions,
            current_state.depth + 1)
        return (new_state1, new_state2)

class ConjunctionElimination(ft.Rule):
    @abstractmethod
    def __init__(self):
        pass

    def use_rule(current_state: state.SingleState, alpha: ft.Formula)->tuple[state.SingleState]:
        assert isinstance(current_state, state.SingleState), "Given argument is not a proof state!"
        assert isinstance(current_state.formulaToBeProved, ft.Formula), "Given state has invalid formula!"
        assert issubclass(type(alpha), ft.Formula), "Given argument is not a subclass of Formula!"
        
        new_state = state.SingleState(
            ft.Conjunction(current_state.formulaToBeProved, alpha),
            current_state.assumptions,
            current_state.depth + 1)
        return new_state,
    
class DisjunctionElimination(ft.Rule):
    @abstractmethod
    def __init__(self):
        pass

    def use_rule(current_state: state.SingleState, alpha: ft.Formula, beta: ft.Formula)->tuple[state.SingleState]:
        assert isinstance(current_state, state.SingleState), "Given argument is not a proof state!"
        assert isinstance(current_state.formulaToBeProved, ft.Formula), "Given state has invalid formula!"
        assert issubclass(type(alpha), ft.Formula), "Given argument is not a subclass of Formula!"
        assert issubclass(type(beta), ft.Formula), "Given argument is not a subclass of Formula!"
        
        new_assumptions1 = deepcopy(current_state.assumptions)
        new_assumptions1.append(alpha)
        new_assumptions2 = deepcopy(current_state.assumptions)
        new_assumptions2.append(beta)

        new_state1 = state.SingleState(
            ft.Disjunction(alpha, beta),
            current_state.assumptions,
            current_state.depth + 1)
        new_state2 = state.SingleState(
            current_state.formulaToBeProved,
            new_assumptions1,
            current_state.depth + 1)
        new_state3 = state.SingleState(
            current_state.formulaToBeProved,
            new_assumptions2,
            current_state.depth + 1)
        return (new_state1, new_state2, new_state3)

class ImplicationElimination(ft.Rule):
    @abstractmethod
    def __init__(self):
        pass

    def use_rule(current_state: state.SingleState, alpha: ft.Formula)->tuple[state.SingleState]:
        assert isinstance(current_state, state.SingleState), "Given argument is not a proof state!"
        assert isinstance(current_state.formulaToBeProved, ft.Formula), "Given state has invalid formula!"
        assert issubclass(type(alpha), ft.Formula), "Given argument is not a subclass of Formula!"
       
        new_state1 = state.SingleState(
            alpha, 
            current_state.assumptions, 
            current_state.depth + 1)
        new_state2 = state.SingleState(
            ft.Implication(alpha, current_state.formulaToBeProved),
            current_state.assumptions, 
            current_state.depth + 1)
        return (new_state1, new_state2)
    
class FalseElimination(ft.Rule):
    @abstractmethod
    def __init__(self):
        pass

    def use_rule(current_state: state.SingleState)->tuple[state.SingleState]:
        assert isinstance(current_state, state.SingleState), "Given argument is not a proof state!"
        assert isinstance(current_state.formulaToBeProved, ft.Formula), "Given state has invalid formula!"
       
        new_state = state.SingleState(
            ft.FalseF(),
            current_state.assumptions, 
            current_state.depth + 1)
        return new_state,
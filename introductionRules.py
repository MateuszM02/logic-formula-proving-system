import formulaTypes as ft
import state
from abc import ABC, abstractmethod
from copy import deepcopy

class NegationIntroduction(ft.Rule):
    @abstractmethod
    def __init__(self):
        pass

    def use_rule(current_state: state.SingleState)->tuple[state.SingleState]:
        assert isinstance(current_state, state.SingleState), "Given argument is not a proof state!"
        assert isinstance(current_state.formulaToBeProved, ft.Negation), "Formula not a negation!"
        
        notNegatedFormula = current_state.formulaToBeProved.formula
        new_assumptions = deepcopy(current_state.assumptions)
        new_assumptions.append(notNegatedFormula)
        
        new_state = state.SingleState(
            ft.FalseF(), 
            new_assumptions, 
            current_state.depth + 1)
        return new_state,

class ConjunctionIntroduction(ft.Rule):
    @abstractmethod
    def __init__(self):
        pass

    def use_rule(current_state: state.SingleState)->tuple[state.SingleState]:
        assert isinstance(current_state, state.SingleState), "Given argument is not a proof state!"
        assert isinstance(current_state.formulaToBeProved, ft.Conjunction), "Formula not a conjunction!"
        
        new_state1 = state.SingleState(
            current_state.formulaToBeProved.formula1,
            current_state.assumptions,
            current_state.depth + 1)
        
        new_state2 = state.SingleState(
            current_state.formulaToBeProved.formula2,
            current_state.assumptions,
            current_state.depth + 1)
        return (new_state1, new_state2)

class DisjunctionIntroduction(ft.Rule, ABC):
    @abstractmethod
    def use_rule(current_state: state.SingleState) -> state.SingleState:
        pass

class DisjunctionIntroduction1(DisjunctionIntroduction):
    def use_rule(current_state: state.SingleState) -> state.SingleState:
        assert isinstance(current_state, state.SingleState), "Given argument is not a proof state!"
        assert isinstance(current_state.formulaToBeProved, ft.Disjunction), "Formula not a disjunction!"
        
        new_state1 = state.SingleState(
            current_state.formulaToBeProved.formula1,
            current_state.assumptions,
            current_state.depth + 1)
        return new_state1,

class DisjunctionIntroduction2(DisjunctionIntroduction):
    def use_rule(current_state: state.SingleState) -> state.SingleState:
        assert isinstance(current_state, state.SingleState), "Given argument is not a proof state!"
        assert isinstance(current_state.formulaToBeProved, ft.Disjunction), "Formula not a disjunction!"
        
        new_state2 = state.SingleState(
            current_state.formulaToBeProved.formula2,
            current_state.assumptions,
            current_state.depth + 1)
        return new_state2,

class ImplicationIntroduction(ft.Rule):
    @abstractmethod
    def __init__(self):
        pass

    def use_rule(current_state: state.SingleState)->tuple[state.SingleState]:
        assert isinstance(current_state, state.SingleState), "Given argument is not a proof state!"
        assert isinstance(current_state.formulaToBeProved, ft.Implication), "Formula not an implication!"
        
        alpha = current_state.formulaToBeProved.formula1
        beta = current_state.formulaToBeProved.formula2

        new_assumptions = deepcopy(current_state.assumptions)
        new_assumptions.append(alpha)
        
        new_state = state.SingleState(
            beta, 
            new_assumptions, 
            current_state.depth + 1)
        return new_state,
import formulaTypes as ft
import state
from abc import abstractmethod
from copy import deepcopy

class NegationIntroduction():
    @abstractmethod
    def __init__(self):
        pass

    def use_rule(current_state: state.SingleState):
        assert isinstance(current_state, state.SingleState), "Given argument is not a proof state!"
        assert isinstance(current_state.formulaToBeProved, ft.Negation), "Formula not a negation!"
        
        notNegatedFormula = current_state.formulaToBeProved.formula
        new_assumptions = deepcopy(current_state.assumptions)
        new_assumptions.put_nowait(notNegatedFormula)
        
        new_state = state.SingleState(
            ft.FalseF(), 
            new_assumptions, 
            current_state.depth + 1)
        return new_state

class ConjunctionIntroduction():
    @abstractmethod
    def __init__(self):
        pass

    def use_rule(current_state: state.SingleState):
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
    
class DisjunctionIntroduction():
    @abstractmethod
    def __init__(self):
        pass

    def use_rule1(current_state: state.SingleState):
        assert isinstance(current_state, state.SingleState), "Given argument is not a proof state!"
        assert isinstance(current_state.formulaToBeProved, ft.Disjunction), "Formula not a disjunction!"
        
        new_state1 = state.SingleState(
            current_state.formulaToBeProved.formula1,
            current_state.assumptions,
            current_state.depth + 1)
        return new_state1
    
    def use_rule2(current_state: state.SingleState):
        assert isinstance(current_state, state.SingleState), "Given argument is not a proof state!"
        assert isinstance(current_state.formulaToBeProved, ft.Disjunction), "Formula not a disjunction!"
        
        new_state2 = state.SingleState(
            current_state.formulaToBeProved.formula2,
            current_state.assumptions,
            current_state.depth + 1)
        return new_state2

class ImplicationIntroduction():
    @abstractmethod
    def __init__(self):
        pass

    def use_rule(current_state: state.SingleState):
        assert isinstance(current_state, state.SingleState), "Given argument is not a proof state!"
        assert isinstance(current_state.formulaToBeProved, ft.Implication), "Formula not an implication!"
        
        alpha = current_state.formulaToBeProved.formula1
        beta = current_state.formulaToBeProved.formula2

        new_assumptions = deepcopy(current_state.assumptions)
        new_assumptions.put_nowait(alpha)
        
        new_state = state.SingleState(
            beta, 
            new_assumptions, 
            current_state.depth + 1)
        return new_state
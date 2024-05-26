from abc import ABC, abstractmethod

class Rule(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def use_rule(self, current_state):
        pass

class Formula(ABC):
    @abstractmethod
    def __init__(self):
        pass

class TrueF(Formula): # T
    def __init__(self):
        pass

    def __eq__(self, other):
        return isinstance(other, TrueF)

class FalseF(Formula): # F
    def __init__(self):
        pass

    def __eq__(self, other):
        return isinstance(other, FalseF)

class Variable(Formula): # p, q
    legalVariableNames = ["p", "q"]

    def __init__(self, var):
        assert var in self.legalVariableNames, f"{var} is not a correct variable name!"
        self.variable = var

    def __eq__(self, other):
        return  isinstance(other, Variable) and \
                self.variable == other.variable

class Negation(Formula): # not p
    def __init__(self, f: Formula):
        assert issubclass(type(f), Formula), "f is not a subclass of Formula!"
        self.formula = f

    def __eq__(self, other):
        return  isinstance(other, Negation) and \
                self.formula == other.formula

class Conjunction(Formula): # p ^ q
    def __init__(self, f1: Formula, f2: Formula):
        assert issubclass(type(f1), Formula), "f1 is not a subclass of Formula!"
        assert issubclass(type(f2), Formula), "f2 is not a subclass of Formula!"
        self.formula1 = f1
        self.formula2 = f2

    def __eq__(self, other):
        return  isinstance(other, Conjunction) and \
                self.formula1 == other.formula1 and \
                self.formula2 == other.formula2
    
class Disjunction(Formula): # p v q
    def __init__(self, f1: Formula, f2: Formula):
        assert issubclass(type(f1), Formula), "f1 is not a subclass of Formula!"
        assert issubclass(type(f2), Formula), "f2 is not a subclass of Formula!"
        self.formula1 = f1
        self.formula2 = f2

    def __eq__(self, other):
        return  isinstance(other, Conjunction) and \
                self.formula1 == other.formula1 and \
                self.formula2 == other.formula2

class Implication(Formula): # p => q
    def __init__(self, f1: Formula, f2: Formula):
        assert issubclass(type(f1), Formula), "f1 is not a subclass of Formula!"
        assert issubclass(type(f2), Formula), "f2 is not a subclass of Formula!"
        self.formula1 = f1
        self.formula2 = f2

    def __eq__(self, other):
        return  isinstance(other, Conjunction) and \
                self.formula1 == other.formula1 and \
                self.formula2 == other.formula2
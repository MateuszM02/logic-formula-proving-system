from abc import ABC, abstractmethod

class Formula(ABC):
    @abstractmethod
    def __init__(self):
        pass

class TrueF(Formula): # T
    def __init__(self):
        pass

class FalseF(Formula): # F
    def __init__(self):
        pass

class Variable(Formula): # p, q
    legalVariableNames = ["p", "q"]

    def __init__(self, var):
        assert var in self.legalVariableNames, "var is not a correct variable name!"
        self.variable = var

class Negation(Formula): # not p
    def __init__(self, f: Formula):
        assert issubclass(type(f), Formula), "f is not a subclass of Formula!"
        self.formula = f

class Conjunction(Formula): # p ^ q
    def __init__(self, f1: Formula, f2: Formula):
        assert issubclass(type(f1), Formula), "f1 is not a subclass of Formula!"
        assert issubclass(type(f2), Formula), "f2 is not a subclass of Formula!"
        self.formula1 = f1
        self.formula2 = f2
    
class Disjunction(Formula): # p v q
    def __init__(self, f1: Formula, f2: Formula):
        assert issubclass(type(f1), Formula), "f1 is not a subclass of Formula!"
        assert issubclass(type(f2), Formula), "f2 is not a subclass of Formula!"
        self.formula1 = f1
        self.formula2 = f2

class Implication(Formula): # p => q
    def __init__(self, f1: Formula, f2: Formula):
        assert issubclass(type(f1), Formula), "f1 is not a subclass of Formula!"
        assert issubclass(type(f2), Formula), "f2 is not a subclass of Formula!"
        self.formula1 = f1
        self.formula2 = f2
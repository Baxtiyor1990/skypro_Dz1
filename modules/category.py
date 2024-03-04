from abc import ABC, abstractmethod

class Category(ABC):
    @abstractmethod
    def some_abstract_method(self):
        pass

from abc import ABC, abstractmethod
class Question(ABC):
    @abstractmethod
    def evaluate_answer(self): pass
class MCQQuestion(Question):
    def evaluate_answer(self): print("Evaluating MCQ")
m = MCQQuestion()
m.evaluate_answer()

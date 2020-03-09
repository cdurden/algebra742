import common
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor, split_symbols
transformations = (standard_transformations + (implicit_multiplication_application, convert_xor, split_symbols, ))
class SolutionQuestion(Question):
    def scripts(self):
        return([])
    def check_answer(self):
        from sympy import *
        x = symbols("x")
        params = self.params()
        try:
            expr = parse_expr(params['statement']).subs(x,parse_expr(self.form.answer.data))
            correct = bool(expr)
        except:
            correct = False
        return(correct)
common.QuestionClasses['Question.SolutionQuestion'] = SolutionQuestion

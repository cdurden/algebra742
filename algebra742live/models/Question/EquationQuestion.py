from . import Question
from sympy import simplify, groebner, symbols
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor, split_symbols
from sympy.polys.polytools import is_zero_dimensional
transformations = (standard_transformations + (implicit_multiplication_application, convert_xor, split_symbols, ))
class EquationQuestion(Question):
    def scripts(self):
        return([])
    def check_answer(self):
        params = self.params()
        try:
            input_lhs, input_rhs = [parse_expr(_hs, transformations=transformations) for _hs in self.form.answer.data.split("=")]
            lhs,rhs = [parse_expr(_hs, transformations=transformations) for _hs in params['equation'].split("=")]
            x,y = symbols('x,y')
            F = groebner([lhs-rhs,input_lhs-input_rhs], x, y, order='lex')
            correct = not is_zero_dimensional(F)
            print(F)
        except:
            correct = False
        return(correct)

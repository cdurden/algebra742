from . import Question
from sympy import simplify
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor, split_symbols
transformations = (standard_transformations + (implicit_multiplication_application, convert_xor, split_symbols, ))
class EquationQuestion(Question):
    def scripts(self):
        return([])
    def check_answer(self):
        params = self.params()
        input_lhs, input_rhs = [parse_expr(_hs, transformations=transformations) for _hs in self.form.answer.data.split("=")]
        lhs,rhs = [parse_expr(_hs, transformations=transformations) for _hs in params['equation'].split("=")]
        print(simplify(lhs-rhs+input_lhs-input_rhs))
        correct = simplify(lhs-rhs+input_lhs-input_rhs)==0
        return(correct)

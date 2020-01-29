from . import Question
from sympy import simplify, groebner, symbols
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor, split_symbols
#from sympy.polys.groebnertools import groebner
from sympy.polys.rings import ring
from sympy.polys.domains import ZZ
from sympy.polys.orderings import lex
transformations = (standard_transformations + (implicit_multiplication_application, convert_xor, split_symbols, ))
class EquationQuestion(Question):
    def scripts(self):
        return([])
    def check_answer(self):
        params = self.params()
        input_lhs, input_rhs = [parse_expr(_hs, transformations=transformations) for _hs in self.form.answer.data.split("=")]
        lhs,rhs = [parse_expr(_hs, transformations=transformations) for _hs in params['equation'].split("=")]
        #print(simplify(lhs-rhs+input_lhs-input_rhs))
        #R = ring("x,y", ZZ, lex)
        x,y = symbols('x,y')
        print(groebner([lhs-rhs,input_lhs-input_rhs], x, y, order='lex'))
        correct = simplify(lhs-rhs+input_lhs-input_rhs)==0
        return(correct)

from pylatex import Document, Section, Enumerate, Itemize, Package, NoEscape
from pylatex.utils import escape_latex
from Questions import QuestionSets
import jinja2
import os
from sympy import latex
from sympy import simplify, symbols, latex
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application, convert_xor, split_symbols
transformations = (standard_transformations + (implicit_multiplication_application, convert_xor, split_symbols, ))

loader = jinja2.FileSystemLoader(searchpath="./templates")
jenv = jinja2.Environment(loader=loader)
latex_jinja_env = jinja2.Environment(
    block_start_string='\BLOCK{',
    block_end_string='}',
    variable_start_string='\VAR{',
    variable_end_string='}',
    comment_start_string='\#{',
    comment_end_string='}',
    line_statement_prefix='%%',
    line_comment_prefix='%#',
    trim_blocks=True,
    autoescape=False,
    loader=loader)

def GenerateAssignmentPdf(assignment, filepath=None):
    doc = Document()
    #doc.packages.append(Package('geometry'))
    #doc.packages.append(Package('geometry', options=['tmargin=3cm',
    #                                                 'lmargin=2cm']))
    doc.packages.append(Package('geometry', options=['tmargin=1cm', 'bmargin=2cm', 'lmargin=1cm']))
    doc.packages.append(Package('multicol'))
    doc.packages.append(Package('graphicx'))
    doc.packages.append(Package('adjustbox'))
    #doc.packages.append(Package('tikz'))
    doc.packages.append(NoEscape('\usepackage{tkz-euclide}'))
    doc.packages.append(NoEscape('\usepackage{pgfplots}'))
    doc.append(NoEscape(r'\usetikzlibrary{arrows.meta}'))
    doc.packages.append(Package('amsmath'))
    doc.packages.append(Package('scalefnt'))
    doc.append(NoEscape('\setlength\itemsep{-2cm}'))
    QuestionData = QuestionSets[assignment]['Questions'] 
    with doc.create(Section(QuestionSets[assignment]['Title'],numbering=False)):
#    \begin{center}
#    \fbox{\fbox{\parbox{5.5in}{\centering
#    Answer the questions in the spaces provided on the
#    question sheets. Be sure to \textbf{show your work to earn full credit.} You \textbf{MAY} use a calculator to help you. If you run out of room for an answer, raise your hand to ask for an extra piece of paper.
#}}}
#    \end{center}
#    \vspace{0.1in}
        doc.append(NoEscape(r'''
    \makebox[\textwidth]{Name and period:\enspace\hrulefill} '''))
        #doc.append(NoEscape(r'\textbf{Learning Goal: }'+QuestionSets[assignment]['LearningGoal']+''))
        doc.append(NoEscape(r'\begin{multicols}{2}'))
        #doc.append(NoEscape(r'    \begin{table}[htb] \begin{tabular}{|*{2}{>{\centering\arraybackslash}p{0.5\textwidth}|}}'))
        with doc.create(Enumerate(enumeration_symbol=r"\arabic*)", options={'start': 1})) as enum:
        #with doc.create(Itemize(options={'start': 1})) as enum:
            for Question in QuestionData:
                for Parameters in Question['ParameterSetVariants']:
                    if 'equation' in Parameters.keys():
                        equation = Parameters['equation']
                        lhs, rhs = equation.split("=")
                        #Parameters['equation_latex'] = "{:s}={:s}".format(latex(parse_expr(lhs,transformations=transformations, evaluate=False)),latex(parse_expr(rhs,transformations=transformations, evaluate=False)))
                    try:
                        template = jenv.get_template(Question['LatexTemplate'])
                    except:
                        template = jenv.get_template(Question['Template'])
                    Parameters['tex'] = True
                    out = template.render(**Parameters)
                    #enum.add_item(NoEscape(out))
                    #doc.append(NoEscape(out))
                    doc.append(NoEscape(r'\item\adjustbox{valign=t}{'+out+'}'))
                    #enum.add_item(NoEscape(Question['Question']))
                    #doc.append("\n\n")
                    if Question['Type'] == 'SelectMultiple':
                        with doc.create(Enumerate(enumeration_symbol=r"\alph*)")) as enumb:
                            for choice in Parameters['choices']:
                                #doc.append(NoEscape(r'\item '+prompt))
                                enumb.add_item(NoEscape(choice[1]))
                    if Question['Type'] == 'Matching':
                        with doc.create(Enumerate(enumeration_symbol=r"\alph*)")) as enumb:
                            for prompt in Parameters['prompts']:
                                #doc.append(NoEscape(r'\item '+prompt))
                                enumb.add_item(NoEscape(prompt))
                    letters = ['a','b','c','d']
#                    if 'Choices' in Parameters:
#                        for i,Choice in enumerate(Parameters['Choices']):
#                            if Choice['type'] == 'image':
#                                doc.append(letters[i]+')')
#                                doc.append(NoEscape(r'\includegraphics[width=0.2\columnwidth]{'+Choice['path']+'}'))
                    doc.append(NoEscape(r'\vspace{'+Question['SpaceAfter']+r'}'))
    #doc.append(NoEscape(r'    \end{tabular}\end{table}'))
    doc.append(NoEscape(r'\end{multicols}'))
    if filepath is None:
        doc.generate_pdf(filepath=os.path.abspath(os.path.join(os.path.dirname(__file__),'resources',assignment)))
    else:
        doc.generate_pdf(filepath=filepath)

def GenerateProblemsInFourQuadrants(assignment, filepath=None):
    doc = Document()
    doc.packages.append(Package('geometry', options=['landscape','tmargin=2cm',
                                                     'lmargin=2cm', 'rmargin=2cm', 'bmargin=2cm']))
    doc.packages.append(Package('amsmath'))
    doc.packages.append(Package('environ'))
    doc.packages.append(Package('tikz'))
    doc.packages.append(Package('graphicx'))
    #doc.packages.append(NoEscape('\usepackage{tkz-euclide}'))
    #doc.packages.append(Package('scalefnt'))
    doc.append(NoEscape(r'\usetikzlibrary{positioning}'))
    newenv = r"""
    \makeatletter
    \newsavebox{\measure@tikzpicture}
    \NewEnviron{scaletikzpicturetowidth}[1]{%
      \def\tikz@width{#1}%
      \def\tikzscale{1}\begin{lrbox}{\measure@tikzpicture}%
      \BODY
      \end{lrbox}%
      \pgfmathparse{#1/\wd\measure@tikzpicture}%
      \edef\tikzscale{\pgfmathresult}%
      \BODY
    }
    \makeatother
    """
    doc.append(NoEscape(newenv))
    #doc.packages.append(Package('multicol'))
    #doc.append(NoEscape(r'\begin{multicols}{2}'))
    #QuestionData = QuestionSets[assignment] 
    QuestionData = QuestionSets[assignment]['Questions']
    for Question in QuestionData:
        ex = []
        for Parameters in Question['ParameterSetVariants']:
            template = jenv.get_template(Question['LatexTemplate'])
            ex.append(template.render(**Parameters))
        template = latex_jinja_env.get_template('ProblemsInFourQuadrants.tex')
        out = template.render(ex1 = ex[0], ex2 = ex[1], ex3 = ex[2], ex4 = ex[3])
        doc.append(NoEscape(out))
    if filepath is None:
        #doc.generate_tex(filepath=os.path.abspath(os.path.join(os.path.dirname(__file__),'resources',assignment)))
        doc.generate_pdf(filepath=os.path.abspath(os.path.join(os.path.dirname(__file__),'resources',assignment)))
    else:
        #doc.generate_tex(filepath=filepath)
        doc.generate_pdf(filepath=filepath)


def GenerateArrowDiagram(filepath, Parameters):
    doc = Document(documentclass="standalone", document_options=NoEscape("varwidth,convert={density=300,size=1080x800,outext=.png}"))
    doc.packages.append(Package('amsmath'))
    doc.packages.append(Package('tikz'))
    template = jenv.get_template('ArrowDiagram.tex')
    out = template.render(**Parameters)
    doc.append(NoEscape(out))
    doc.generate_tex(filepath=filepath)

#assignment = 'TwoStepEquations'
#GenerateAssignmentPdf(assignment)
#assignment = 'AlgebraicAndVerbalExpressions'
#GenerateAssignmentPdf(assignment)
#assignment = 'TermsAndFactors'
#GenerateAssignmentPdf(assignment)
#assignment = 'ReciprocalPairsAndZeroPairs'
#GenerateAssignmentPdf(assignment)
#assignment = 'SolveEquationsGuided'
#assignment = 'SimplifyUsingDistributiveProperty'
#assignment = 'ClassworkOct25'
#assignment = 'ClassworkOct30B'
#GenerateAssignmentPdf(assignment)
#assignment = 'ClassworkNov8A'
#GenerateAssignmentPdf(assignment)
#assignment = 'ClassworkNov8B'

#assignment = 'SolvingEquationsTest'
#assignment = 'WODBFunctions'
#assignment = 'EvaluateFunctions'
#assignment = 'FunctionsTest'
assignment = "UsingZeroPairsAndReciprocalPairs"
assignment = "LinearEquationsInStandardFormB"
assignment = "LinearEquationsInStandardFormPart2"
assignment = "StainedGlassGraphs"
assignment = "GraphingLinearEquationsSpeedDating"
assignment = "GraphingLinearEquationsSpeedDatingQuestions"
assignment = "GraphingLinearEquationsTest"
assignment = "CalculatingSlopeClasswork"
assignment = 'GraphLineGivenPointAndSlope'
assignment = 'MixedPracticeJanuary13'
assignment = 'SlopeInterceptChallengeJanuary13'
assignment = "TypesOfSlopeClasswork"
assignment = 'LinearEquationsPart2Review'
assignment = 'SlopeInterceptClassworkJanuary13'
assignment = "ArithmeticSequencesJanuary22"
assignment = "LinearEquationsTest3"
assignment = "LinearEquationsTest2Retry"
assignment = "LinearEquationsTest2RetryLG1"
assignment = "AddEmUpLinearEquations2"
assignment = "Feb3CW"
assignment = "Feb4CW"
assignment = "Feb7HW"
assignment = "Feb10CW"
assignment = "Feb12HW"
assignment = "Feb18CW"
assignment = "Feb19CW"
assignment = "LinearEquationsTest4"
assignment = "LinearEquationsTest4RetryPractice"
#assignment = "Feb10HW"
GenerateAssignmentPdf(assignment)
#assignment = "LinearEquationsTest2RetryLG4"
#GenerateAssignmentPdf(assignment)
#assignment = "LinearEquationsTest2RetryLG5"
#GenerateAssignmentPdf(assignment)
#assignment = 'PracticeTest'
#GenerateAssignmentPdf('PracticeTest')
#GenerateAssignmentPdf('PracticeZeroPairsAndReciprocalPairs')
#GenerateProblemsInFourQuadrants('AddEmUpIntegersAndEquations')
#GenerateProblemsInFourQuadrants('AddEmUpLinearEquations2')
#letters = ['a','b','c','d']
#signs = [('',''),('','-'),('-',''),('-','-')]
#for q,Question in enumerate(QuestionSets[assignment]['Questions']):
#    if Question['Type']=='ArrowDiagram':
#        for (i, Parameters) in enumerate(Question['ParameterSetVariants']):
#            for j,(signa, signb) in enumerate(signs):
#                a = Parameters['a']
#                b = Parameters['b']
#                Parameters0 = Parameters
#                Parameters0['signa'] = signa
#                Parameters0['signb'] = signb
#                Parameters0['c'] = int('{:s}{:s}'.format(signa,a))+int('{:s}{:s}'.format(signb,b))
#                GenerateArrowDiagram("resources/ArrowDiagrams/ArrowDiagram-{:d}-{:d}{:s}".format(q,i,letters[j]), Parameters0)

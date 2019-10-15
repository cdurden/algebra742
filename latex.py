from pylatex import Document, Section, Enumerate, Package, NoEscape
from pylatex.utils import escape_latex
from Questions import QuestionSets
import jinja2
import os
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
    doc.packages.append(Package('geometry', options=['tmargin=1cm',
                                                     'lmargin=1cm']))
    doc.packages.append(Package('multicol'))
    doc.packages.append(Package('graphicx'))
    doc.packages.append(Package('amsmath'))
    QuestionData = QuestionSets[assignment]['Questions'] 
    with doc.create(Section('')):
        doc.append(NoEscape(r'''
    \begin{center}
    \fbox{\fbox{\parbox{5.5in}{\centering
    Answer the questions in the spaces provided on the
    question sheets. If you run out of room for an answer,
    raise your hand to ask for an extra piece of paper.}}}
    \end{center}
    \vspace{0.1in}
    \makebox[\textwidth]{Name and period:\enspace\hrulefill} '''))
        doc.append(NoEscape(r'\begin{multicols}{2}'))
        with doc.create(Enumerate(enumeration_symbol=r"\arabic*)", options={'start': 1})) as enum:
            for Question in QuestionData:
                for Parameters in Question['ParameterSetVariants']:
                    template = jenv.get_template(Question['Template'])
                    out = template.render(**Parameters)
                    enum.add_item(NoEscape(out))
                    #enum.add_item(NoEscape(Question['Question']))
                    doc.append("\n\n")
                    letters = ['a','b','c','d']
#                    if 'Choices' in Parameters:
#                        for i,Choice in enumerate(Parameters['Choices']):
#                            if Choice['type'] == 'image':
#                                doc.append(letters[i]+')')
#                                doc.append(NoEscape(r'\includegraphics[width=0.2\columnwidth]{'+Choice['path']+'}'))
                    doc.append(NoEscape(r'\vspace{'+Question['SpaceAfter']+r'}'))
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
    QuestionData = QuestionSets[assignment] 
    for Question in QuestionData:
        ex = []
        for Parameters in Question['ParameterSetVariants']:
            template = jenv.get_template(Question['Template'])
            ex.append(template.render(**Parameters))
        template = latex_jinja_env.get_template('ProblemsInFourQuadrants.tex')
        out = template.render(ex1 = ex[0], ex2 = ex[1], ex3 = ex[2], ex4 = ex[3])
        doc.append(NoEscape(out))
    if filepath is None:
        doc.generate_tex(filepath=os.path.abspath(os.path.join(os.path.dirname(__file__),'resources',assignment)))
    else:
        doc.generate_tex(filepath=filepath)


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
assignment = 'ReciprocalPairsAndZeroPairs'
GenerateAssignmentPdf(assignment)
#assignment = 'PracticeTest'
#GenerateAssignmentPdf('PracticeTest')
#GenerateAssignmentPdf('PracticeZeroPairsAndReciprocalPairs')
#GenerateProblemsInFourQuadrants('AddEmUpIntegersAndEquations')
letters = ['a','b','c','d']
signs = [('',''),('','-'),('-',''),('-','-')]
for q,Question in enumerate(QuestionSets[assignment]['Questions']):
    if Question['Type']=='ArrowDiagram':
        for (i, Parameters) in enumerate(Question['ParameterSetVariants']):
            for j,(signa, signb) in enumerate(signs):
                a = Parameters['a']
                b = Parameters['b']
                Parameters0 = Parameters
                Parameters0['signa'] = signa
                Parameters0['signb'] = signb
                Parameters0['c'] = int('{:s}{:s}'.format(signa,a))+int('{:s}{:s}'.format(signb,b))
                GenerateArrowDiagram("resources/ArrowDiagrams/ArrowDiagram-{:d}-{:d}{:s}".format(q,i,letters[j]), Parameters0)

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
    doc.packages.append(Package('amsmath'))
    doc.append(NoEscape(r'\begin{multicols}{2}'))
    QuestionData = QuestionSets[assignment] 
    with doc.create(Section('Practice Using Zero Pairs and Reciprocal Pairs')):
        with doc.create(Enumerate(enumeration_symbol=r"\arabic*)", options={'start': 1})) as enum:
            for Question in QuestionData:
                for Parameters in Question['ParameterSetVariants']:
                    template = jenv.get_template(Question['Template'])
                    out = template.render(**Parameters)
                    enum.add_item(NoEscape(out))
                    #enum.add_item(NoEscape(Question['Question']))
                    doc.append(NoEscape(r'\vspace{'+Question['SpaceAfter']+r'}'))
    doc.append(NoEscape(r'\end{multicols}'))
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
    doc.generate_pdf(filepath=filepath)


def GenerateArrowDiagram(filepath, Parameters):
    doc = Document(documentclass="standalone", document_options=NoEscape("convert={density=300,size=1080x800,outext=.png}"))
    doc.packages.append(Package('amsmath'))
    doc.packages.append(Package('tikz'))
    template = jenv.get_template('ArrowDiagram.tex')
    out = template.render(**Parameters)
    doc.append(NoEscape(out))
    doc.generate_tex(filepath=filepath)

#assignment = 'PracticeTest'
#GenerateAssignmentPdf('PracticeTest')
#GenerateAssignmentPdf('PracticeZeroPairsAndReciprocalPairs')
GenerateProblemsInFourQuadrants('AddEmUpIntegersAndEquations')
#for q,Question in enumerate(QuestionSets[assignment]):
#    if Question['Type']=='ArrowDiagram':
#        for (i, Parameters) in enumerate(Question['ParameterSetVariants']):
#            GenerateArrowDiagram("ArrowDiagram-{:d}-{:d}".format(q,i), Parameters)

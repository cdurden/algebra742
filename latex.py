from pylatex import Document, Section, Enumerate, Package, NoEscape
from pylatex.utils import escape_latex
from Questions import QuestionSets
import jinja2
loader = jinja2.FileSystemLoader(searchpath="./templates")
jenv = jinja2.Environment(loader=loader)

def GenerateAssignmentPdf(assignment, filepath=None):
    doc = Document()
    doc.packages.append(Package('geometry', options=['tmargin=1cm',
                                                     'lmargin=1cm']))
    doc.packages.append(Package('multicol'))
    doc.packages.append(Package('amsmath'))
    doc.append(NoEscape(r'\begin{multicols}{2}'))
    QuestionData = QuestionSets[assignment] 
    with doc.create(Section('Equations and Integers Practice')):
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
GenerateAssignmentPdf('PracticeZeroPairsAndReciprocalPairs')
#for q,Question in enumerate(QuestionSets[assignment]):
#    if Question['Type']=='ArrowDiagram':
#        for (i, Parameters) in enumerate(Question['ParameterSetVariants']):
#            GenerateArrowDiagram("ArrowDiagram-{:d}-{:d}".format(q,i), Parameters)

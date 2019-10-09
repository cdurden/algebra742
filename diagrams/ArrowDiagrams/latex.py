from pylatex import Document, Section, Enumerate, Package, NoEscape
from pylatex.utils import escape_latex
#from Questions import EPQuestionData as QuestionData

def GenerateArrowDiagram(filepath, params):
    doc = Document(documentclass="standalone", document_options=NoEscape("convert={density=300,size=1080x800,outext=.png}"))
    doc.packages.append(Package('amsmath'))
    doc.packages.append(Package('tikz'))
    tikztex = r"""\usetikzlibrary{arrows}
    \begin{tikzpicture}
    \draw[latex-] (-6.5,0) -- (6.5,0) ;
    \draw[-latex] (-6.5,0) -- (6.5,0) ;
    \foreach \x in  {-6,-4,-2,0,2,4,6}
    \draw[shift={(\x,0)},color=black] (0pt,3pt) -- (0pt,-3pt);
    \foreach \x in {-6,-4,-2,0,2,4,6}
    \draw[shift={(\x,0)},color=black] (0pt,0pt) -- (0pt,-3pt) node[below] 
    {$\x$};
    \draw[->] (0,1.0) -- ({:d},1.0);
    \draw[->] ({:d},0.5) -- ({:d},0.5);
    \draw[very thick    ] (0.92,0) -- (1.92,0);
    \end{tikzpicture}"""
    #print(tikztex)
    doc.append(NoEscape(tikztex.format(params['a'],params['a'],params['a']+params['b'])))
    doc.generate_pdf(filepath=filepath)

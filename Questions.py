QuestionSets = {
    'BalancingCandy': {
        'ProvideImmediateFeedback': True,
        'Questions': [
        {
            'Type': 'SetUpAndSolveEquationGuided',
            'Template': 'SetUpAndSolveEquationGuided.html',
            'ParameterSetVariants': [
                {'question': 'How much does one starburst weigh?', 'quantities': ['weight of a starburst', 'weight of a skittle'], 'variables': ['t','k'], 'equation': r'6(t+2k)=40k', 'act1_youtube_video_id': 'hKbVTk2Z-kY'},
                {'question': 'How many skittles are in one bag?', 'quantities': ['weight of a bag of skittles', 'weight of one skittle'], 'variables': ['s','t'], 'equation': r'3s+2t=47t', 'act1_youtube_video_id': 'tAaSMnc7ovc'},
                {'question': 'How many skittles are in each of the silver bottles?', 'quantities': ['weight of an empty bottle', 'weight of a skittle', 'weight of a starburst', 'number of skittles in the silver bottle'], 'variables': ['b', 'k', 't', 'g'], 'equation': r'2b+x*k+3t=2b+21k', 'act1_youtube_video_id': 'ySPeCgh31qc'},
                ]
            }
        ]
    },
    'ClassworkOct25': {
        'ProvideImmediateFeedback': True,
        'Questions':
        [
            {
            'Type': 'SolveEquationGuided',
            'Template': 'SolveEquationGuided.html',
            'ParameterSetVariants': [
                {'equation': '3(m+9)-2m=30', 'variables': ['m']},
                {'equation': '3a+a-10=2', 'variables': ['a']},
                {'equation': '3m-1+m-2=5', 'variables': ['m']},
                {'equation': '3(x-1)-x=5', 'variables': ['x']},
                {'equation': '3(2s-1)+5-s=12', 'variables': ['s']},
                {'equation': '3(x-3)-2(12+x)=-1', 'variables': ['x']},
                {'equation': '-3(2t-2)+(2-t)=29', 'variables': ['t']},
                ],
            'SpaceAfter': '4cm',
            }
        ]
    },
    'HWp93': {
        'ProvideImmediateFeedback': True,
        'Questions':
        [
            {
            'Type': 'SolveEquationGuided',
            'Template': 'SolveEquationGuided.html',
            'ParameterSetVariants': [
                {'equation': '3m+4=-11', 'variables': ['m']},
                {'equation': '12=-7f-9', 'variables': ['f']},
                {'equation': '-3=2+a/11', 'variables': ['a']},
                {'equation': '3/2a-8=11', 'variables': ['a']},
                {'equation': '8=(x-5)/7', 'variables': ['x']},
                ],
            'SpaceAfter': '4cm',
            }
        ]
    },
    'CLT': {
        'ProvideImmediateFeedback': True,
        'Questions':
        [
            {
            'Type': 'Simplify',
            'Template': 'Simplify.html',
            'ParameterSetVariants': [
                {'expression': '10x+5x+2'},
                {'expression': '4a-4-7a+1'},
                {'expression': '4z^4-4z^3+2z^4-4z^3'},
                {'expression': '-20w^3-101+40w^3-53'},
                ],
            'SpaceAfter': '4cm',
            },
        ]
    },
    'SimplifyUsingDistributivePropertySpice': {
        'ProvideImmediateFeedback': True,
        'Questions':
        [
            {
            'Type': 'Simplify',
            'Template': 'Simplify.html',
            'ParameterSetVariants': [
                {'expression': '3q+4r+5q+r+1'},
                {'expression': '3(w-5)-2(12+w)'},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'SolveEquationGuided',
            'Template': 'SolveEquationGuided.html',
            'ParameterSetVariants': [
                {'equation': '3(x-1)-2(12+x)=2', 'variables': ['x']},
                ],
            'SpaceAfter': '4cm',
            }
        ]
    },
    'SimplifyUsingDistributivePropertyMild': {
        'ProvideImmediateFeedback': True,
        'Questions':
        [
            {
            'Type': 'Simplify',
            'Template': 'Simplify.html',
            'ParameterSetVariants': [
                {'expression': '3q+4r+5q+r+1'},
                {'expression': '-3s+4b-7s-b-1'},
                {'expression': '3(w-5)-2(12+w)'},
                ],
            'SpaceAfter': '4cm',
            },
        ]
    },
    'SimplifyUsingDistributiveProperty': {
        'ProvideImmediateFeedback': True,
        'Questions':
        [
            {
            'Type': 'Simplify',
            'Template': 'Simplify.html',
            'ParameterSetVariants': [
                {'expression': '3q+4r+5q+r+1'},
                {'expression': '-3s+4b-7s-b-1'},
                {'expression': '3(w-5)-2(12+w)'},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'SolveEquationGuided',
            'Template': 'SolveEquationGuided.html',
            'ParameterSetVariants': [
                {'equation': '3m+m-10=2', 'variables': ['m']},
                {'equation': '3m-1+m-2=5', 'variables': ['m']},
                {'equation': '3(x-1)-2(12+x)=2', 'variables': ['x']},
                ],
            'SpaceAfter': '4cm',
            }
        ]
    },
    'DifferenceBetweenConstantAndCoefficient': {
        'ProvideImmediateFeedback': False,
        'Questions':
        [
            {
            'Type': 'OpenResponse',
            'Template': 'DifferenceBetweenConstantAndCoefficient.html',
            'ParameterSetVariants': [{}],
            }
        ]
    },
    'WritingAndSolvingOneStepEquations': {
        'ProvideImmediateFeedback': True,
        'Questions': [
        {
            'Type': 'SetUpAndSolveEquationGuided',
            'Template': 'SetUpAndSolveEquationGuided.html',
            'ParameterSetVariants': [
                {'question': 'Lisa is cooking muffins. The recipe calls for 7 cups of sugar. She has already put in 2 cups. How many more cups does she need to put in?', 'quantities': ['how many more cups of sugar Lisa needs to put in'], 'variables': ['a'], 'equation': r'7=2+a'},
                {'question': 'After paying \$5 for a salad, Norachai has \$27. How much money did he have before buying the salad?', 'quantities': ['how much money Norachai had before buying the salad'], 'variables': ['a'], 'equation': r'27=a-5'},
                {'question': 'How many packages of diapers can you buy with \$40 if one package costs \$8?','quantities': ['how many packages of diapers you can buy'], 'variables': ['a'], 'equation': r'40=8a'},
                {'question': 'Christa is saving for a new tablet. It costs 70 dollars, including tax. She has already saved 35 dollars. How much more does she need to save?', 'quantities': ['how much more money Christa needs to save'], 'variables': ['a'], 'equation': r'70=35+a'},
                {'question': 'Bella bought packs of stickers to give to her friends. Each pack cost 4 dollars. She spent a total of 12 dollars on stickers. How many packs did she buy?', 'quantities': ['how many packs of stickers Bella bought'], 'variables': ['x'], 'equation': r'12=4x'},
                {'question': 'Robert had money in his savings account. He spent 35 dollars of it on a new jacket. He has 70 dollars left. How much money did he have in his savings before he bought the jacket?', 'quantities': ['how much money Robert had in his savings account before he bought the jacket'], 'variables': ['x'], 'equation': r'70=x-35'},
                {'question': 'Pete played in two basketball games. He scored 4 fewer points in the second game than in the first. He scored 12 points in the second game. How many points did he score in the first game?', 'quantities': ['how many points Pete scored in the first game'], 'variables': ['x'], 'equation': r'12=x-4'},
                {'question': 'Bella brought stickers to school to give to 12 of her friends. Each friend received 4 stickers. How many stickers did she bring to school?', 'quantities': ['how many stickers Bella brought to school'], 'variables': ['x'], 'equation': r'x=12*4'},
                ]
            },
        ]
    },
    'CommunicatingReasoning': {
        'ProvideImmediateFeedback': False,
        'Questions': [
        {
            #'Type': 'AddSubtractIntegerDirections',
            'Type': 'MC',
            'Template': 'Empty.html',
            'ParameterSetVariants': [{}],
            'Choices': [('0', 'I did not communicate my reasoning'), ('1','I presented my reasoning for some problems'), ('2','I presented my reasoning for every problem'), ('3','I presented a detailed argument, including all steps needed to reach all of my conclusions')],
            'Question': 'How well did you communicate your reasoning on this assignment?',
            }
        ]
    },
    'DifferenceBetweenTermAndFactor': {
        'ProvideImmediateFeedback': False,
        'Questions':
        [
            {
            'Type': 'OpenResponse',
            'Template': 'DifferenceBetweenTermAndFactor.html',
            'ParameterSetVariants': [{}],
            }
        ]
    },
    'SolveEquationsGuided': {
        'ProvideImmediateFeedback': True,
        'Questions':
        [
            {
            'Type': 'SolveEquationGuided',
            'Template': 'SolveEquationGuided.html',
            'ParameterSetVariants': [
                {'equation': r'2x+15=83', 'variables': ['x']}, 
                {'equation': r'1/4(x+2)=10', 'variables': ['x']},
                {'equation': r'2/3x+10=31', 'variables': ['x']},
                {'equation': r'1/5(x+5)=10', 'variables': ['x']},
                {'equation': r'3x+-3=30', 'variables': ['x']},
                {'equation': r'1/3(x+-3)=10', 'variables': ['x']},
                {'equation': r'2/3(x+12)=10', 'variables': ['x']},
                {'equation': r'5/6x+10=20', 'variables': ['x']},
                {'equation': r'-3/4x+6=9', 'variables': ['x']},
                {'equation': r'2/5(x-10)=20', 'variables': ['x']},
                {'equation': r'-3/8x-5=9', 'variables': ['x']},
                {'equation': r'(x-5)/3=9', 'variables': ['x']},
                {'equation': r'-2x-5=9-x', 'variables': ['x']},
                {'equation': r'(x-5)/3=2x+1', 'variables': ['x']},
                ],
            'SpaceAfter': '4cm',
            }
        ]
    },
    'ReciprocalPairsAndZeroPairs': {
        'ProvideImmediateFeedback': True,
        'Questions': [
        {
            #'Type': 'SolveEquation',
            'Type': 'Expression',
            'Template': 'ReciprocalPair.html',
            'ParameterSetVariants': [
                {'expression': r'\frac{4}{3}','CorrectAnswer': '3/4'},
                {'expression': r'\frac{2}{3}','CorrectAnswer': '3/2'},
                {'expression': r'3', 'CorrectAnswer': '1/3'}, 
                {'expression': r'-\frac{2}{3}','CorrectAnswer': '-3/2'},
                {'expression': r'-\frac{1}{3}','CorrectAnswer': '-3'},
                {'expression': r'-5','CorrectAnswer': '-1/5'},
                {'expression': r'-\frac{2}{3}','CorrectAnswer': '-3/2'},
                ],
            'SpaceAfter': '2cm',
            },
        {
            'Type': 'Expression',
            'Template': 'ZeroPair.html',
            'ParameterSetVariants': [
                {'expression': r'10', 'CorrectAnswer': '-10'}, 
                {'expression': r'-3','CorrectAnswer': '3'},
                {'expression': r'-136','CorrectAnswer': '136'},
                {'expression': r'-\frac{1}{4}','CorrectAnswer': '1/4'},
                ],
            'SpaceAfter': '2cm',
            },
        {
            'Type': 'Expression',
            'Template': 'IdentifyConstant.html',
            'ParameterSetVariants': [
                {'expression': r'3x+10', 'CorrectAnswer': '10'}, 
                {'expression': r'2x+15=83', 'CorrectAnswer': '15'}, 
                {'expression': r'\frac{1}{3}x+(-136)','CorrectAnswer': '-136'},
                ],
            'SpaceAfter': '2cm',
            },
        {
            'Type': 'Expression',
            'Template': 'IdentifyCoefficient.html',
            'ParameterSetVariants': [
                {'expression': r'3x', 'CorrectAnswer': '3'}, 
                {'expression': r'\frac{1}{3}(x+3)=9','CorrectAnswer': '1/3'},
                {'expression': r'-\frac{1}{4}(x+2)=10','CorrectAnswer': '-1/4'},
                ],
            'SpaceAfter': '2cm',
            },
        ]
        },
    'TwoStepEquations': {
        'ProvideImmediateFeedback': True,
        'Questions': [
        {
            #'Type': 'SolveEquation',
            'Type': 'Numerical',
            'Template': 'SolveEquation.html',
            'ParameterSetVariants': [
                {'equation': r'3x+10=70', 'CorrectAnswer': 20}, 
                {'equation': r'\frac{1}{3}(x+3)=9','CorrectAnswer': 24},
                {'equation': r'-\frac{1}{4}(x+2)=10','CorrectAnswer': -42},
                {'equation': r'2x+15=83', 'CorrectAnswer': 34}, 
                {'equation': r'\frac{1}{4}(x+2)=10','CorrectAnswer': 38},
                {'equation': r'5x+301=-405+301','CorrectAnswer': -81},
                {'equation': r'7(x-1)=70','CorrectAnswer': 11},
                {'equation': r'\frac{1}{3}x+(-136)=-158','CorrectAnswer': -66},
                {'equation': r'\frac{1}{2}x+93=-211','CorrectAnswer': -608},
                #{'equation': 'x+(-225)=-300','CorrectAnswer': -75},
                {'equation': r'\frac{1}{5}(x+25)=-25','CorrectAnswer': -150},
                {'equation': r'\frac{1}{2}(2x+4)=-8','CorrectAnswer': -10},
                ],
                #{'equation': r'\frac{1}{3}x+(-45)=-75','CorrectAnswer': -90},],
            'SpaceAfter': '5cm',
            },
        ]
        },
    'AlgebraicAndVerbalExpressions': {
        'ProvideImmediateFeedback': True,
        'Questions': [
        {
            #'Type': 'AddSubtractIntegerDirections',
            'Type': 'Expression',
            'Template': 'VerbalToAlgebraicExpression.html',
            'ParameterSetVariants': [
                {'verbal_expression': '3 decreased by the product of 5 and x', 'CorrectAnswer': '3-5x'},
                {'verbal_expression': 'the sum of x to the 5th power and 3 times y', 'CorrectAnswer': 'x^5+3y'},
                {'verbal_expression': 'the sum of x and 5', 'CorrectAnswer': 'x+5'},
                {'verbal_expression': '4 times the sum of x and 5', 'CorrectAnswer': '4(x+5)'},
                {'verbal_expression': 'the product of 5 and x', 'CorrectAnswer': '5x'},
                {'verbal_expression': 'The difference of 3 times x squared and y', 'CorrectAnswer': '3x^2-y'},
                ],
                #,{'operation': 'adding a negative', 'answer': 'a'},{'operation': 'adding a positive', 'answer': 'b'}],
            'SpaceAfter': '2cm',
            },
        ]},
    'TermsAndFactors': {
        'ProvideImmediateFeedback': True,
        'Questions': [
        {
            #'Type': 'AddSubtractIntegerDirections',
            'Type': 'MC',
            'Template': 'IdentifySumTermsProductFactors.html',
            'ParameterSetVariants': [
                {'expression': '5+2x', 'CorrectAnswer': 'a',
                    'Choices': [('a', 'sum'), ('b', 'product')],
                    },
                {'expression': '5(x+3)', 'CorrectAnswer': 'b',
                    'Choices': [('a', 'sum'), ('b', 'product')],
                    },
                {'expression': '3x+5y+4', 'CorrectAnswer': 'a',
                    'Choices': [('a', 'sum'), ('b', 'product')],
                    },
                {'expression': '3(x+y+2)', 'CorrectAnswer': 'b',
                    'Choices': [('a', 'sum'), ('b', 'product')],
                    },
                {'expression': '3(x+1)+4', 'CorrectAnswer': 'a',
                    'Choices': [('a', 'sum'), ('b', 'product')],
                    },
                ],
                #,{'operation': 'adding a negative', 'answer': 'a'},{'operation': 'adding a positive', 'answer': 'b'}],
            'SpaceAfter': '4cm',
            },
        ]},
    'IntegerEquationsTest': {
        'ProvideImmediateFeedback': False,
        'Questions': [
        {
            #'Type': 'AddSubtractIntegerDirections',
            'Type': 'MC',
            'Template': 'AddSubtractIntegerDirections.html',
            'ParameterSetVariants': [{'operation': 'subtracting a negative', 'CorrectAnswer': 'a'},{'operation': 'subtracting a positive', 'CorrectAnswer': 'b'}],
                #,{'operation': 'adding a negative', 'answer': 'a'},{'operation': 'adding a positive', 'answer': 'b'}],
            'Choices': [('a', 'up'), ('b','down')],
            'SpaceAfter': '2cm',
            },
        {
            'Type': 'MC',
            'Template': 'ArrowDiagram.html',
            'ParameterSetVariants': [
                {'expression_type': 'sum', 'expression': '-8-5', 'signa': '-', 'a': '8', 'signb': '-', 'b': '5',
                    'Choices': [('a', '![UpUp](/static/ArrowDiagrams/ArrowDiagram-1-0a.png)'),('b', '![UpDown](/static/ArrowDiagrams/ArrowDiagram-1-0b.png)'), ('c', '![DownUp](/static/ArrowDiagrams/ArrowDiagram-1-0c.png)'), ('d', '![DownDown](/static/ArrowDiagrams/ArrowDiagram-1-0d.png)')],
                    'CorrectAnswer': 'd'},
                {'expression_type': 'sum', 'expression': '3-(-1)', 'signa': '', 'a': '3', 'signb': '', 'b': '1',
                    'Choices': [('a', '![UpUp](/static/ArrowDiagrams/ArrowDiagram-1-1a.png)'),('b', '![UpDown](/static/ArrowDiagrams/ArrowDiagram-1-1b.png)'), ('c', '![DownUp](/static/ArrowDiagrams/ArrowDiagram-1-1c.png)'), ('d', '![DownDown](/static/ArrowDiagrams/ArrowDiagram-1-1d.png)')],
                    'CorrectAnswer': 'a'},
                 ],
#            'Choices': [('a', '![UpUp](/static/ArrowDiagrams/ArrowDiagram-1-1a.png)'),('b', '![UpDown](/static/ArrowDiagrams/ArrowDiagram-1-1b.png)'), ('c', '![DownUp](/static/ArrowDiagrams/ArrowDiagram-1-1c.png)'), ('d', '![DownDown](/static/ArrowDiagrams/ArrowDiagram-1-1d.png)')],
            'SpaceAfter': '0.2cm',
            },
#        {
#            'Type': 'AddSubtractIntegersArrowDiagram',
#            'Template': 'AddSubtractIntegersArrowDiagram.html',
#            'ParameterSetVariants': [{'a': 3, 'op': '-', 'b': -5},{'a': 3, 'op': '-', 'b': -4}],
#            'Question': 'Which diagram represents the expression $3-(-5)$?',
#            'CorrectAnswer': '7',
#            },
        {
            #'Type': 'AddSubtractIntegers',
            'Type': 'Numerical',
            'Template': 'AddSubtractIntegers.html',
            'ParameterSetVariants': [
                {'expression_type': 'sum', 'expression': '-8-5', 'CorrectAnswer': -13},
                {'expression_type': 'sum', 'expression': '3-(-1)', 'CorrectAnswer': 4},
                {'expression_type': 'sum', 'expression': '-34+93', 'CorrectAnswer': 59},
                {'expression_type': 'sum', 'expression': '-27-(-157)', 'CorrectAnswer': 130},],
            'SpaceAfter': '4cm',
            },
        {
            #'Type': 'IdentifyPropertyUsed',
            'Type': 'MC',
            'Template': 'IdentifyPropertyUsed.html',
            'ParameterSetVariants': [{'argument': r'\begin{align*}x+(-5) &= -10 \\ \Rightarrow x+(-5)+5 &= -10+5\end{align*}', 'CorrectAnswer': 'a'}, {'argument': r'\begin{align*}\frac{1}{2}x &= 12 \\ \Rightarrow 2\cdot\frac{1}{2}x &= 2 \cdot 12\end{align*}', 'CorrectAnswer': 'b'}],
            'Choices': [('a', 'Addition Property of Equality'), ('b','Multiplication Property of Equality'), ('c', 'Associative Property'), ('d', 'Additive Identity Property')],
            'SpaceAfter': '2cm',
            },
        {
            #'Type': 'SolveEquation',
            'Type': 'Numerical',
            'Template': 'SolveEquation.html',
            'ParameterSetVariants': [
                {'equation': 'x+15=83', 'CorrectAnswer': 68}, 
                {'equation': 'x+301=-405+301','CorrectAnswer': -405},
                {'equation': 'x+(-136)=-158','CorrectAnswer': -22},
                {'equation': 'x+93=-211','CorrectAnswer': -304},
                #{'equation': 'x+(-225)=-300','CorrectAnswer': -75},
                {'equation': r'\frac{1}{5}x=-25','CorrectAnswer': -125},],
                #{'equation': r'\frac{1}{3}x+(-45)=-75','CorrectAnswer': -90},],
            'SpaceAfter': '5cm',
            },
        ],
        },
    'AddEmUpIntegersAndEquations': [
        {
            #'Type': 'AddSubtractIntegers',
            'Type': 'Numerical',
            'Template': 'Expression.html',
            'ParameterSetVariants': [
                {'expression_type': 'sum', 'expression': '-5+8', 'CorrectAnswer': '3'},
                {'expression_type': 'sum', 'expression': '-3-(-2)', 'CorrectAnswer': '-1'},
                {'expression_type': 'sum', 'expression': '-2-9', 'CorrectAnswer': '-11'},
                {'expression_type': 'sum', 'expression': '-7-(-8)', 'CorrectAnswer': '1'}
                ],
            'SpaceAfter': '4cm',
            },
        {
            #'Type': 'AddSubtractIntegers',
            'Type': 'Numerical',
            'Template': 'Expression.html',
            'ParameterSetVariants': [
                {'expression_type': 'sum', 'expression': '-115+81', 'CorrectAnswer': '3'},
                {'expression_type': 'sum', 'expression': '-131-(-27)', 'CorrectAnswer': '-1'},
                {'expression_type': 'sum', 'expression': '-12-192', 'CorrectAnswer': '-11'},
                {'expression_type': 'sum', 'expression': '-74-(-83)', 'CorrectAnswer': '1'}
                ],
            'SpaceAfter': '4cm',
            },
        {
            #'Type': 'SolveEquation',
            'Type': 'Numerical',
            'Template': 'Equation.html',
            'ParameterSetVariants': [
                {'equation': 'x+112=96', 'CorrectAnswer': '84'},
                {'equation': 'x+25=-111','CorrectAnswer': '-250'},
                {'equation': 'x+(-22)=-108','CorrectAnswer': '-86'},
                {'equation': 'x+(53)=-271','CorrectAnswer': '-324'},
                ],
            'SpaceAfter': '5cm',
            },
        {
            #'Type': 'SolveEquation',
            'Type': 'Numerical',
            'Template': 'Equation.html',
            'ParameterSetVariants': [
                {'equation': r'5x=-175', 'CorrectAnswer': '84'},
                {'equation': r'\frac{1}{3}x=-123','CorrectAnswer': '-250'},
                {'equation': r'-\frac{1}{6}x=-108','CorrectAnswer': '-86'},
                {'equation': r'-8x=256','CorrectAnswer': '-324'},
                ],
            'SpaceAfter': '5cm',
            },
        {
            #'Type': 'SolveEquation',
            'Type': 'Numerical',
            'Template': 'Equation.html',
            'ParameterSetVariants': [
                {'equation': r'5x+(-40)=-120', 'CorrectAnswer': '84'},
                {'equation': r'\frac{1}{3}x+51=-123','CorrectAnswer': '-250'},
                {'equation': r'-\frac{1}{6}x+18=-108','CorrectAnswer': '-86'},
                {'equation': r'-8x+72=56','CorrectAnswer': '-324'},
                ],
            'SpaceAfter': '5cm',
            },
        ],
    'PracticeZeroPairsAndReciprocalPairs': [
        {
            #'Type': 'SolveEquation',
            'Type': 'Numerical',
            'Template': 'SolveEquation.html',
            'ParameterSetVariants': [{'equation': r'\frac{1}{2}x=24', 'CorrectAnswer': '48'},{'equation': r'x+-15=24', 'CorrectAnswer': '39'},  {'equation': '5x=-250','CorrectAnswer': '-50'},{'equation': r'\frac{1}{2}x=-216','CorrectAnswer': '-432'},{'equation': r'x+89=-24', 'CorrectAnswer': '-113'},{'equation': '3x=51','CorrectAnswer': '17'},{'equation': r'\frac{1}{5}x=-60','CorrectAnswer': '-300'},{'equation': r'-\frac{1}{4}x=-60','CorrectAnswer': '240'},{'equation': '-15x=-45','CorrectAnswer': '3'},],
            'SpaceAfter': '5cm',
            },
        {
            #'Type': 'SolveEquation',
            'Type': 'Numerical',
            'Template': 'SolveEquation.html',
            'ParameterSetVariants': [{'equation': r'\frac{1}{2}x+12=96', 'CorrectAnswer': '168'}, {'equation': '5x+25=-250+25','CorrectAnswer': '-50'},{'equation': r'\frac{1}{2}x+(-22)=-216','CorrectAnswer': '-388'},{'equation': 'x+53=-271','CorrectAnswer': '-324'},{'equation': 'x+(-125)=-600','CorrectAnswer': '-475'},{'equation': '-15x=-240','CorrectAnswer': '16'},{'equation': '-15x+(-45)=-75','CorrectAnswer': '2'},],
            'SpaceAfter': '5cm',
            }
    ],
    'DistributiveLaw': [
        {
            #'Type': 'SolveEquation',
            'Type': 'Numerical',
            'Template': 'DistributiveLaw.html',
            'ParameterSetVariants': [{'expression': '3(x+10)', 'CorrectAnswer': '3x+30'}, {'expression': '5(x+5)','CorrectAnswer': '5x+25'},{'expression': r'\frac{1}{2}(x+-22)','CorrectAnswer': '1/2x+-11'},{'expression': '-3(x+17)','CorrectAnswer': '-3x+-51'},{'expression': '5(x+-30)','CorrectAnswer': '5x+-150'},{'expression': '-15(x+14)','CorrectAnswer': '-15x+-210'},{'expression': '-15(x+-3)','CorrectAnswer': '-15x+45'},],
            'SpaceAfter': '5cm',
            },
        ],
    'PracticeTest': [
        {
            #'Type': 'AddSubtractIntegerDirections',
            'Type': 'MC',
            'Template': 'AddSubtractIntegerDirections.html',
            'ParameterSetVariants': [{'operation': 'subtracting a negative', 'CorrectAnswer': 'a'},{'operation': 'subtracting a positive', 'CorrectAnswer': 'b'}],
                #,{'operation': 'adding a negative', 'answer': 'a'},{'operation': 'adding a positive', 'answer': 'b'}],
            'Choices': [('a', 'up'), ('b','down')],
            'Question': 'Suppose you are using a vertical number line, with the positive numbers in the up direction. Which direction do you move along the number line when?',
            'SpaceAfter': '2cm',
            },
#        {
#            'Type': 'ArrowDiagram',
#            'Template': 'ArrowDiagram.html',
#            'ParameterSetVariants': [{'expression_type': 'sum', 'expression': '-25+89'},{'expression_type': 'sum', 'expression': '-32-(-108)'},],
#            'SpaceAfter': '5cm',
#            },
#        {
#            'Type': 'AddSubtractIntegersArrowDiagram',
#            'Template': 'AddSubtractIntegersArrowDiagram.html',
#            'ParameterSetVariants': [{'a': 3, 'op': '-', 'b': -5},{'a': 3, 'op': '-', 'b': -4}],
#            'Question': 'Which diagram represents the expression $3-(-5)$?',
#            'CorrectAnswer': '7',
#            },
        {
            #'Type': 'AddSubtractIntegers',
            'Type': 'Numerical',
            'Template': 'AddSubtractIntegers.html',
            'ParameterSetVariants': [{'expression_type': 'sum', 'expression': '-25+89', 'CorrectAnswer': '64'},{'expression_type': 'sum', 'expression': '-32-(-108)', 'CorrectAnswer': '76'},],
            'SpaceAfter': '4cm',
            },
        {
            #'Type': 'IdentifyPropertyUsed',
            'Type': 'MC',
            'Template': 'IdentifyPropertyUsed.html',
            'ParameterSetVariants': [{'argument': '$(x+5)+(-5) = x+(5+-5)$', 'CorrectAnswer':'c'},{'argument': '$x+0 = x$', 'CorrectAnswer':'d'}, {'argument': r'\begin{align*}x+(-39) &= -101 \\ \Rightarrow x+(-39)+39 &= -101+39\end{align*}', 'CorrectAnswer': 'a'}, {'argument': r'\begin{align*}12x = 12\cdot 14 \\ \Rightarrow x = 14\end{align*}', 'CorrectAnswer': 'b'}],
            'Choices': [('a', 'Addition Property of Equality'), ('b','Multiplication Property of Equality'), ('c', 'Associative Property'), ('d', 'Additive Identity Property')],
            'SpaceAfter': '2cm',
            },
        {
            #'Type': 'SolveEquation',
            'Type': 'Numerical',
            'Template': 'SolveEquation.html',
            'ParameterSetVariants': [{'equation': 'x+12=96', 'CorrectAnswer': '84'}, {'equation': 'x+25=-250+25','CorrectAnswer': '-250'},{'equation': 'x+(-22)=-108','CorrectAnswer': '-86'},{'equation': 'x+53=-271','CorrectAnswer': '-324'},{'equation': 'x+(-125)=-600','CorrectAnswer': '-475'},{'equation': '-15x=-240','CorrectAnswer': '16'},{'equation': '-15x+(-45)=-75','CorrectAnswer': '2'},],
            'SpaceAfter': '5cm',
            },
        ]
    }

APEMPEWholeNumbersData = [
        {
            'Type': 'Numerical',
            'Question': 'Use the algebraic properties to solve the equation: $x+3=9$',
            'CorrectAnswer': '6'
            },
        {
            'Type': 'Numerical',
            'Question': 'Use the algebraic properties to solve the equation: $a+12=17$',
            'CorrectAnswer': '5'
            },
        {
            'Type': 'Numerical',
            'Question': 'Use the algebraic properties to solve the equation: $5b=20$',
            'CorrectAnswer': '4'
            },
        {
            'Type': 'Numerical',
            'Question': 'Use the algebraic properties to solve the equation: $b+16=30$',
            'CorrectAnswer': '14'
            },
        {
            'Type': 'Numerical',
            'Question': 'Use the algebraic properties to solve the equation: $7b=42$',
            'CorrectAnswer': '6'
            }
        ]
EPQuestionData = [
        {
            'Type': 'Numerical',
            'Question': 'Evaluate $5-(-2)$',
            'CorrectAnswer': '7',
            },
        {
            'Type': 'Numerical',
            'Question': 'Evaluate $-4+(-2)$',
            'CorrectAnswer': '-6',
            },
        {
            'Type': 'Numerical',
            'Question': 'Evaluate $-\\frac{3}{4}+\\frac{1}{2}$',
            'CorrectAnswer': '-1/4',
            },
        {
            'Type': 'Numerical',
            'Question': 'Evaluate $-\\frac{5}{6}-\\frac{1}{2}$',
            'CorrectAnswer': '-4/3',
            },
        {
            'Type': 'MC',
            'Question': 'Which of the following shows the addition property of equality?',
            'Choices': [('a', '$a+b=b+c \\\ \Rightarrow \\\ a=c$'),('b', '$c\cdot a = c\cdot b \\\ \Rightarrow\\\ a=c$'),('c', '$(a+b)+c = a+(b+c)$'),('d', '$a + 0 = a$') ],
            'CorrectChoice': 'a'
            },
        {
            'Type': 'Numerical',
            'Question': 'Use the properties of equality to solve the equation: $x+2=8$',
            'CorrectAnswer': '6'
            },
        {
            'Type': 'Numerical',
            'Question': 'Use the properties of equality to solve the equation: $3x=21$',
            'CorrectAnswer': '7'
            },
        {
            'Type': 'Numerical',
            'Question': 'Use the algebraic properties to solve the equation: $x+(-3)=9$',
            'CorrectAnswer': '12'
            },
        {
            'Type': 'Numerical',
            'Question': 'Use the algebraic properties to solve the equation: $x+(-5)=-15$',
            'CorrectAnswer': '-10'
            },
        {
            'Type': 'Numerical',
            'Question': 'Use the algebraic properties to solve the equation: $-5x=-15$',
            'CorrectAnswer': '3'
            },
        {
            'Type': 'Numerical',
            'Question': 'Use the algebraic properties to solve the equation: $\\frac{1}{3}x=9$',
            'CorrectAnswer': '27'
            },
        {
            'Type': 'Numerical',
            'Question': 'Use the algebraic properties to solve the equation: $-\\frac{1}{5}x=5$',
            'CorrectAnswer': '-25'
            },
        {
            'Type': 'MC',
            'Question': 'Is the left hand side of the following expression a sum or a product? $3x+2=8$',
            'Choices': [('a', 'Sum'),('b', 'Product')],
            'CorrectChoice': 'a'
            },
        {
            'Type': 'Numerical',
            'Question': 'Use the properties of equality to solve the equation: $3x+2=8$',
            'CorrectAnswer': '2'
            },
        {
            'Type': 'Numerical',
            'Question': 'Use the algebraic properties to solve the equation: $\\frac{1}{2}x+(-3)=13$',
            'CorrectAnswer': '32'
            },
        ]
BalanceQuestionData = [
        {
            'LHSImage': 'BalanceImages/IMG_1634.jpg',
            'RHSImage': 'BalanceImages/IMG_1635.jpg',
            'LHS': 'a',
            'RHS': '2*b',
            'Variables': ['a', 'b'],
            'Quantities': ['the weight of an orange cube', 'the weight of a small paper clip'] 
            },
        {
            'LHSImage': 'BalanceImages/IMG_1632.jpg',
            'RHSImage': 'BalanceImages/IMG_1633.jpg',
            'LHS': '2*a',
            'RHS': '4*b',
            'Variables': ['a', 'b'],
            'Quantities': ['the weight of an orange cube', 'the weight of a small paper clip'] 
            },
        {
            'LHSImage': 'BalanceImages/IMG_1630.jpg',
            'RHSImage': 'BalanceImages/IMG_1631.jpg',
            'LHS': '3*a',
            'RHS': '6*b',
            'Variables': ['a', 'b'],
            'Quantities': ['the weight of an orange cube', 'the weight of a small paper clip'] 
            },
        {
            'LHSImage': 'BalanceImages/IMG_1627.jpg',
            'RHSImage': 'BalanceImages/IMG_1628.jpg',
            'LHS': '4*a+b',
            'RHS': '9*b',
            'Variables': ['a', 'b'],
            'Quantities': ['the weight of an orange cube', 'the weight of a small paper clip'] 
            },
        {
            'LHSImage': 'BalanceImages/IMG_1621.jpg',
            'RHSImage': 'BalanceImages/IMG_1622.jpg',
            'LHS': '3*a',
            'RHS': '6*b',
            'Variables': ['a', 'b'],
            'Quantities': ['the weight of a nickel', 'the weight of a penny'] 
            },
        {
            'LHSImage': 'BalanceImages/IMG_1619.jpg',
            'RHSImage': 'BalanceImages/IMG_1620.jpg',
            'LHS': '3*a+b',
            'RHS': '7*b',
            'Variables': ['a', 'b'],
            'Quantities': ['the weight of a nickel', 'the weight of a penny'] 
            },
        {
            'LHSImage': 'BalanceImages/IMG_1612.jpg',
            'RHSImage': 'BalanceImages/IMG_1613.jpg',
            'LHS': '2*a+3*b',
            'RHS': '13*b',
            'Variables': ['a', 'b'],
            'Quantities': ['the weight of an S-hook', 'the weight of a pencil tip eraser'] 
            },
        {
            'LHSImage': 'BalanceImages/IMG_1604.jpg',
            'RHSImage': 'BalanceImages/IMG_1605.jpg',
            'LHS': '2*a+b',
            'RHS': '15*b',
            'Variables': ['a', 'b'],
            'Quantities': ['the weight of an eraser', 'the weight of a yellow block'] 
            },
        {
            'LHSImage': 'BalanceImages/IMG_1594.jpg',
            'RHSImage': 'BalanceImages/IMG_1595.jpg',
            'LHS': '3*a+2*b',
            'RHS': '5*b',
            'Variables': ['a', 'b'],
            'Quantities': ['the weight of a clip', 'the weight of a hex nut'] 
            },
        {
            'LHSImage': 'BalanceImages/IMG_1576.jpg',
            'RHSImage': 'BalanceImages/IMG_1577.jpg',
            'LHS': '2*a+b',
            'RHS': '5*b',
            'Variables': ['a', 'b'],
            'Quantities': ['the weight of a hex nut', 'the weight of a dime'] 
            },
        ]


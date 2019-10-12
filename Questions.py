QuestionSets = {
    'IntegerEquationsTest': [
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
                    'Choices': [('a', '![UpUp](static/ArrowDiagrams/ArrowDiagram-1-0a.png)'),('b', '![UpDown](static/ArrowDiagrams/ArrowDiagram-1-0b.png)'), ('c', '![DownUp](static/ArrowDiagrams/ArrowDiagram-1-0c.png)'), ('d', '![DownDown](static/ArrowDiagrams/ArrowDiagram-1-0d.png)')],
                    'CorrectAnswer': 'd'},
                {'expression_type': 'sum', 'expression': '3-(-1)', 'signa': '', 'a': '3', 'signb': '', 'b': '1',
                    'Choices': [('a', '![UpUp](static/ArrowDiagrams/ArrowDiagram-1-1a.png)'),('b', '![UpDown](static/ArrowDiagrams/ArrowDiagram-1-1b.png)'), ('c', '![DownUp](static/ArrowDiagrams/ArrowDiagram-1-1c.png)'), ('d', '![DownDown](static/ArrowDiagrams/ArrowDiagram-1-1d.png)')],
                    'CorrectAnswer': 'a'},
                 ],
            'Choices': [('a', '![UpUp](static/ArrowDiagrams/ArrowDiagram-1-1a.png)'),('b', '![UpDown](static/ArrowDiagrams/ArrowDiagram-1-1b.png)'), ('c', '![DownUp](static/ArrowDiagrams/ArrowDiagram-1-1c.png)'), ('d', '![DownDown](static/ArrowDiagrams/ArrowDiagram-1-1d.png)')],
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
                {'expression_type': 'sum', 'expression': '-8-5', 'CorrectAnswer': '-13'},
                {'expression_type': 'sum', 'expression': '3-(-1)', 'CorrectAnswer': '4'},
                {'expression_type': 'sum', 'expression': '-34+93', 'CorrectAnswer': '59'},
                {'expression_type': 'sum', 'expression': '-27-(-157)', 'CorrectAnswer': '130'},],
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
                {'equation': 'x+15=83', 'CorrectAnswer': '68'}, 
                {'equation': 'x+301=-405+301','CorrectAnswer': '-405'},
                {'equation': 'x+(-136)=-158','CorrectAnswer': '-22'},
                {'equation': 'x+93=-211','CorrectAnswer': '-304'},
                #{'equation': 'x+(-225)=-300','CorrectAnswer': '-75'},
                {'equation': r'\frac{1}{5}x=-25','CorrectAnswer': '-125'},],
                #{'equation': r'\frac{1}{3}x+(-45)=-75','CorrectAnswer': '-90'},],
            'SpaceAfter': '5cm',
            },
        ],
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


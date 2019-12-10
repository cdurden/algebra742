import json
import numpy
numpy.linspace(0, 10, num=4)
grid = numpy.array(numpy.meshgrid(numpy.linspace(-12,12,num=25),numpy.linspace(-12,12,num=25))).T.reshape(-1,2)
grid36x36 = numpy.array(numpy.meshgrid(numpy.linspace(-4,36,num=41),numpy.linspace(-4,36,num=41))).T.reshape(-1,2)
homelessness_grid = numpy.array(numpy.meshgrid(numpy.linspace(2011,2035,num=25),numpy.linspace(0,150000,num=151))).T.reshape(-1,2)
def gen_grid(xmin,xmax,ymin,ymax,dx,dy):
    grid = numpy.array(numpy.meshgrid(numpy.linspace(xmin,xmax,num=(xmax-xmin)/dx+1),numpy.linspace(ymin,ymax,num=(ymax-ymin)/dy+1))).T.reshape(-1,2)
    return(grid)

def frange(x, y, jump):
    while x < y:
        yield x
        x += jump
QuestionSets = {
    'TransformIntoStandardForm': {
        'ProvideImmediateFeedback': True,
        'Title': 'December 10: Transforming a Linear Equation into Standard Form',
        'Questions': [
            {
            'Type': 'SortCards',
            'Template': 'SortCards.html',
            'ParameterSetVariants': [
                {
                    'question': 'Change the equation $x= y -5$ into standard form. Place the cards below in the correct order to show the steps.',
                    'shuffle': [0 ,7 ,7 ,1 ,2 ,3 ,4 ,
                                7 ,7 ,7 ,7 ,7 ,7 ,2 ,
                                7 ,1 ,3 ,0 ,6 ,5 ,5],
                    'solutions': [
                                   [0, 7, 7, 1, 2, 3, 4,
                                    7, 7, 5, 7, 5, 7, 7,
                                    0, 3, 2, 1, 7, 7, 6],
                                   [0, 7, 7, 1, 2, 3, 4,
                                    7, 5, 7, 7, 5, 7, 7,
                                    0, 3, 2, 1, 7, 7, 6],
                                   [0, 7, 7, 1, 2, 3, 4,
                                    5, 7, 7, 7, 5, 7, 7,
                                    0, 3, 2, 1, 7, 7, 6],
                                   [0, 7, 7, 1, 2, 3, 4,
                                    7, 7, 5, 7, 5, 7, 7,
                                    0, 3, 2, 1, 7, 7, 6],
                                   [0, 7, 7, 1, 2, 3, 4,
                                    7, 5, 7, 7, 5, 7, 7,
                                    0, 3, 2, 1, 7, 6, 7],
                                   [0, 7, 7, 1, 2, 3, 4,
                                    5, 7, 7, 7, 5, 7, 7,
                                    0, 3, 2, 1, 6, 7, 7],
                                   ],
                    'cards': ['<img src="/static/deck10/card0.png"/>','<img src="/static/deck10/card1.png"/>', '<img src="/static/deck10/card2.png"/>', '<img src="/static/deck10/card3.png"/>', '<img src="/static/deck10/card4.png"/>', '<img src="/static/deck10/card5.png"/>', '<img src="/static/deck10/card6.png"/>', '<img src="/static/deck10/card7.png"/>', '<img src="/static/deck10/card8.png"/>', '<img src="/static/deck10/card9.png"/>', '<img src="/static/deck10/card10.png"/>']
                    },
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'SetOfCoordinatePairs',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': r'Find the $x$-intercept of the graph. (Tap or click on the point to select it.)', 'a': [0,2], 'b': [3,4], 'variables': ['a','b'],
                    'grid_x': json.dumps([x[0] for x in gen_grid(-8,8,-1,8,1,1)]),
                    'grid_y': json.dumps([x[1] for x in gen_grid(-8,8,-1,8,1,1)]),
                    'x': [1,2],
                    'y': [4,3],
                    'set_of_coordinate_pairs': {(5,0)},
                    'show_points': True,
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'N': json.dumps(1),
                    },
                {'question': r'Find the $y$-intercept of the graph. (Tap or click on the point to select it.)', 'a': [0,2], 'b': [3,4], 'variables': ['a','b'],
                    'grid_x': json.dumps([x[0] for x in gen_grid(-8,8,-1,8,1,1)]),
                    'grid_y': json.dumps([x[1] for x in gen_grid(-8,8,-1,8,1,1)]),
                    'x': [1,2],
                    'y': [4,3],
                    'set_of_coordinate_pairs': {(0,5)},
                    'show_points': True,
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'N': json.dumps(1),
                    },
                {'question': r'Find the $x$-intercept of the graph. (Tap or click on the point to select it.)', 'a': [0,2], 'b': [3,4], 'variables': ['a','b'],
                    'grid_x': json.dumps([x[0] for x in gen_grid(-8,8,-1,8,1,1)]),
                    'grid_y': json.dumps([x[1] for x in gen_grid(-8,8,-1,8,1,1)]),
                    'x': [-4,-2],
                    'y': [4,3],
                    'set_of_coordinate_pairs': {(4,0)},
                    'show_points': True,
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'N': json.dumps(1),
                    },
                {'question': r'Find the $y$-intercept of the graph. (Tap or click on the point to select it.)', 'a': [0,2], 'b': [3,4], 'variables': ['a','b'],
                    'grid_x': json.dumps([x[0] for x in gen_grid(-8,8,-1,8,1,1)]),
                    'grid_y': json.dumps([x[1] for x in gen_grid(-8,8,-1,8,1,1)]),
                    'x': [-4,-2],
                    'y': [4,3],
                    'set_of_coordinate_pairs': {(0,2)},
                    'show_points': True,
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'N': json.dumps(1),
                    },
                ],
            'SpaceAfter': '4cm',
            },
        ]
    },
    'GraphingLinearEquationsSkillsExtra': {
        'ProvideImmediateFeedback': True,
        'Title': 'December 9: Graphing Linear Equations',
        'Questions': [
            {
            'Type': 'InputOutputTableAndSetOfCoordinatePairsEquation',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': r'A rodeo charges \$5 for children and \$10 for adults. The equation $5x+10y=60$ represents the number of children $x$ and adults $y$ who can attend the rodeo with \$60. Find the $x$ and $y$-intercepts and use them to graph the equation. Then explain what the $x$ and $y$-intercepts mean.', 'x': [None,0], 'y': [0,None], 'variables': ['x','y'],
                    'grid_x': json.dumps([x[0] for x in gen_grid(-1,14,-1,14,1,1)]),
                    'grid_y': json.dumps([x[1] for x in gen_grid(-1,14,-1,14,1,1)]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'equation': '5x+10y=60',
                    'explanation': True,
                 },
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTableAndSetOfCoordinatePairsEquation',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': r'An amusement part charges \$50 for admission before 6 PM, and \$20 for admission after 6 PM. On Saturday, the park took in a total of \$20,000. Let $x$ be the admissions sold before 6 PM, and let $y$ be the admissions sold after 6 PM. Fill in the table with possible numbers of admissions, and graph the relationship. Then explain what the $x$ and $y$-intercepts mean.', 'x': [None,None], 'y': [None,None], 'variables': ['x','y'],
                    'grid_x': json.dumps([x[0] for x in gen_grid(-1,14,-1,14,1,1)]),
                    'grid_y': json.dumps([x[1] for x in gen_grid(-1,14,-1,14,1,1)]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'equation': '5x+10y=60',
                    'explanation': True,
                 },
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTableAndSetOfCoordinatePairsEquation',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': r'Use the equation $y=3x+4$ to find the missing entries in the table. Then graph the relationship.', 'x': [0,2,4], 'y': [None,None,None], 'variables': ['x','y'],
                    'grid_x': json.dumps([x[0] for x in gen_grid(-1,8,-1,8,1,1)]),
                    'grid_y': json.dumps([x[1] for x in gen_grid(-1,8,-1,8,1,1)]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'equation': 'y=3x+4',
                 },
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTableAndSetOfCoordinatePairsEquation',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': r'Graph the equation $y=4+x$ by filling in the missing entries of the table and then graphing the points.', 'x': [1,None], 'y': [None,10], 'variables': ['x','y'],
                    'grid_x': json.dumps([x[0] for x in gen_grid(-1,14,-1,14,1,1)]),
                    'grid_y': json.dumps([x[1] for x in gen_grid(-1,14,-1,14,1,1)]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'equation': 'y=4+x',
                    'explanation': False,
                 },
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'SortCards',
            'Template': 'SortCards.html',
            'ParameterSetVariants': [
                {
                    'shuffle': [0 ,1 ,2 ,3 ,10,10,4 ,
                                10,10,10,10,10,10,10,
                                1 ,5 ,1 ,2 ,3 ,3 ,5 ,
                                10,10,10,10,10,10,4 ,
                                5 ,6 ,7 ,6 ,6 ,8 ,9],
                    'solutions': [[0, 1, 2, 3, 10, 10, 4, 5, 10, 10, 10, 5, 10, 10, 10, 10, 2, 3, 5, 1, 4, 10, 10, 6, 10, 6, 10, 6, 10, 10, 7, 3, 8, 1, 9]],
                    'cards': ['<img src="/static/deck5/card0.png"/>','<img src="/static/deck5/card1.png"/>', '<img src="/static/deck5/card2.png"/>', '<img src="/static/deck5/card3.png"/>', '<img src="/static/deck5/card4.png"/>', '<img src="/static/deck5/card5.png"/>', '<img src="/static/deck5/card6.png"/>', '<img src="/static/deck5/card7.png"/>', '<img src="/static/deck5/card8.png"/>', '<img src="/static/deck5/card9.png"/>', '<img src="/static/deck5/card10.png"/>']
                    },
                {
                    'shuffle': [11 ,11 ,0 ,1 ,2 ,3 ,4 ,
                                11 ,11 ,11 ,11 ,11 ,11 ,11 ,
                                1 ,5 ,1 ,7 ,3 ,3 ,5 ,
                                11,10,9 ,9 ,11,11,8 ,
                                5 ,6 ,11,11,6 ,8 ,11],
                    'solutions': [[11, 11, 0, 1, 2, 3, 4, 11, 11, 5, 11, 5, 11, 5, 11, 11, 6, 1, 10, 3, 8, 9, 11, 11, 11, 9, 11, 11, 7, 3, 6, 1, 11, 11, 8],[11, 11, 0, 1, 2, 3, 4, 11, 11, 5, 11, 5, 11, 5, 11, 11, 6, 1, 10, 3, 8, 11, 9, 11, 11, 9, 11, 11, 7, 3, 6, 1, 11, 11, 8],[11, 11, 0, 1, 2, 3, 4, 11, 11, 5, 11, 5, 11, 5, 11, 11, 6, 1, 10, 3, 8, 11, 11, 9, 11, 9, 11, 11, 7, 3, 6, 1, 11, 11, 8]],
                    'cards': ['<img src="/static/deck6/card0.png"/>','<img src="/static/deck6/card1.png"/>', '<img src="/static/deck6/card2.png"/>', '<img src="/static/deck6/card3.png"/>', '<img src="/static/deck6/card4.png"/>', '<img src="/static/deck6/card5.png"/>', '<img src="/static/deck6/card6.png"/>', '<img src="/static/deck6/card7.png"/>', '<img src="/static/deck6/card8.png"/>', '<img src="/static/deck6/card9.png"/>', '<img src="/static/deck6/card10.png"/>', '<img src="/static/deck6/card11.png"/>']
                    },
                {
                    'question': 'Change the equation $2x+3y = 6$ into slope-intercept form. Place the cards below in the correct order to show the steps.',
                    'shuffle': [0 ,4 ,2 ,5 ,10,10,3 ,
                                10,10,10,10,10,10,10,
                                1 ,1 ,1 ,2 ,3 ,4 ,5 ,
                                10,10,10,10,10,10,4 ,
                                5 ,6 ,7 ,7 ,7 ,8 ,9],
                    'solutions': [[0,4,2,5,10,10,3,1,10,10,10,1,10,10,10,10,2,5,1,4,3,10,10,7,10,7,10,7,10,10,6,5,9,4,8]],
                    'cards': ['<img src="/static/deck4/card0.png"/>','<img src="/static/deck4/card1.png"/>', '<img src="/static/deck4/card2.png"/>', '<img src="/static/deck4/card3.png"/>', '<img src="/static/deck4/card4.png"/>', '<img src="/static/deck4/card5.png"/>', '<img src="/static/deck4/card6.png"/>', '<img src="/static/deck4/card7.png"/>', '<img src="/static/deck4/card8.png"/>', '<img src="/static/deck4/card9.png"/>', '<img src="/static/deck4/card10.png"/>']
                    },
                ],
            'SpaceAfter': '4cm',
            },
        ]
    },
    'GraphingLinearEquationsSkills': {
                # Questions:
                # Concepts: A line can be horizontal, vertical, or diagonal. 
                # Concepts: When a line is horizontal or diagonal, we can travel along the x-axis to any given x value, and then we can travel up or down until we reach the graph of the line. By reading the y value of this point, we can determine the y value that corresponds to the given x value. 
                # Concept: We can do something similar with an equation of a line. We can substitute a value for x, and solve the equation for y to find the corresponding value of y.
                # Concepts: We can use different representations of a line (equation, table, graph) to find coordinates of points on the line
                # 0. Create the table for the discrete graph.
                # 1. A question that makes the connection between finding table when a graph has discrete points and when a graph is continuous. 
                # 1. Go over to x=4. How far up do you need to go to reach the graph? This is the y value associated with x=4.
                # 2. Choose any x value, enter it into the first column of the table. Repeate a question like #1 with the chosen x-value. Ensure that students understand that they could have chosen any x value, and used the graph to find the associated y-value.
                # 3. Use the language that y depends on x.
                # 4. Students explain the nature of the relationship. What happens to y when x increases?
                # 5. What happens to the y value when the x value gets bigger?
                # 6. If we have a table of x and y values of a line, we can plot the line. Have students use a table with two entries to graph a line, and then use the graph to find missing entries in the table.
                # 7. Another representation of a line is an equation. Have students use the equation to create a table. Then use the table to graph the line.
                # 8. A special entry in a table, is the entry where either the x value is 0 or the y value is 0. Plot these points. Which axis is the point (0,5) on? 
                # 9. Use an equation to create a table with x and y-intercepts.
        'ProvideImmediateFeedback': True,
        'Title': 'December 9: Graphing Linear Equations',
        'Questions': [
            {
            'Type': 'InputOutputTable',
            'Template': 'Graph.html',
            'ParameterSetVariants': [
                {'question': r'Make a table of the points shown in the coordinate plane.', 'x': [6,4,2,0], 'y': [0,4,8,12], 'variables': ['x ','y ']},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'SetOfCoordinatePairs',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': 'Graph the relationship shown in the table. (Tap on the graph to add each coordinate pair.)',
                    'html': '<br/><table class="iotable"><tr><th>x</th><th>y</th></tr><td>0</td><td>2</td></tr> <tr><td>1</td><td>1</td></tr> <tr><td>2</td><td>0</td></tr> <tr><td>3</td><td>-1</td></tr></table>',
                    'grid_x': json.dumps([x[0] for x in gen_grid(-1,5,-1,5,1,1)]),
                    'grid_y': json.dumps([x[1] for x in gen_grid(-1,5,-1,5,1,1)]),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'set_of_coordinate_pairs': {(0,2),(1,1),(2,0),(3,-1)},
                    'N': json.dumps(4),
                    },
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'SetOfCoordinatePairs',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': r'Find the $x$-intercept of the graph. (Tap or click on the point to select it.)', 'a': [0,2], 'b': [3,4], 'variables': ['a','b'],
                    'grid_x': json.dumps([x[0] for x in gen_grid(-8,8,-1,8,1,1)]),
                    'grid_y': json.dumps([x[1] for x in gen_grid(-8,8,-1,8,1,1)]),
                    'x': [0,2],
                    'y': [3,4],
                    'set_of_coordinate_pairs': {(-6,0)},
                    'show_points': True,
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'N': json.dumps(1),
                    }
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTable',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': r'Use the graph of the line to find the missing value in the table.', 'a': [0,2,4], 'b': [3,4,None], 'variables': ['a','b'],
                    'grid_x': json.dumps([x[0] for x in gen_grid(-1,8,-1,8,1,1)]),
                    'grid_y': json.dumps([x[1] for x in gen_grid(-1,8,-1,8,1,1)]),
                    'x': [0,2,4],
                    'y': [3,4,5],
                    'show_points': True,
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'N': json.dumps(2),
                    }
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTable',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': r'Assume the relationship represented in the table is linear. Graph the line. Then use the graph to find the missing value in the table.', 'a': [6,4,2], 'b': [0,4,None], 'variables': ['a','b'],
                    'grid_x': json.dumps([x[0] for x in gen_grid(-1,8,-1,8,1,1)]),
                    'grid_y': json.dumps([x[1] for x in gen_grid(-1,8,-1,8,1,1)]),
                    'x': [6,4,2],
                    'y': [0,4,8],
                    'show_points': False,
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'set_of_coordinate_pairs': {(6,0),(4,4),(2,8)},
                    'N': json.dumps(2),
                    }
                ],
            'SpaceAfter': '4cm',
            },
#            {
#            'Type': 'InputOutputTableEquation',
#            'Template': 'PlotQuestion.html',
#            'ParameterSetVariants': [
#                {'question': r'Use the equation $y=3x+4$ to find the missing entries in the table.', 'x': [0,2,4], 'y': [None,None,None], 'variables': ['x','y'],
#                    'grid_x': json.dumps([x[0] for x in gen_grid(-1,8,-1,8,1,1)]),
#                    'grid_y': json.dumps([x[1] for x in gen_grid(-1,8,-1,8,1,1)]),
#                    'grid_x': json.dumps([x[0] for x in grid]),
#                    'grid_y': json.dumps([x[1] for x in grid]),
#                    'N': json.dumps(2),
#                    'dtickx': json.dumps(1),
#                    'dticky': json.dumps(1),
#                    'equation': 'y=3x+4',
#                 },
#                ],
#            'SpaceAfter': '4cm',
#            },
            {
            'Type': 'SortCards',
            'Template': 'SortCards.html',
            'ParameterSetVariants': [
                {
                    'question': 'Change the equation $y = 2x+8$ into standard form. Place the cards below in the correct order to show the steps.',
                    'shuffle': [6 ,6 ,0 ,1 ,2 ,3 ,4 ,
                                6 ,6 ,6 ,6 ,6 ,3 ,5 ,
                                6 ,5 ,1 ,5 ,0 ,6 ,4],
                    'solutions': [
                        [6, 6, 0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 6, 6, 5, 3, 0, 1, 6, 6, 4],
                        [6, 6, 0, 1, 2, 3, 4, 6, 5, 6, 6, 5, 6, 6, 5, 3, 0, 1, 6, 6, 4],
                        [6, 6, 0, 1, 2, 3, 4, 6, 6, 5, 6, 5, 6, 6, 5, 3, 0, 1, 6, 6, 4],
                        [6, 6, 0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 6, 6, 5, 3, 0, 1, 6, 4, 6],
                        [6, 6, 0, 1, 2, 3, 4, 6, 5, 6, 6, 5, 6, 6, 5, 3, 0, 1, 6, 4, 6],
                        [6, 6, 0, 1, 2, 3, 4, 6, 6, 5, 6, 5, 6, 6, 5, 3, 0, 1, 6, 4, 6],
                        [6, 6, 0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 6, 6, 5, 3, 0, 1, 4, 6, 6],
                        [6, 6, 0, 1, 2, 3, 4, 6, 5, 6, 6, 5, 6, 6, 5, 3, 0, 1, 4, 6, 6],
                        [6, 6, 0, 1, 2, 3, 4, 6, 6, 5, 6, 5, 6, 6, 5, 3, 0, 1, 4, 6, 6],],
                    'cards': ['<img src="/static/deck7/card0.png"/>','<img src="/static/deck7/card1.png"/>', '<img src="/static/deck7/card2.png"/>', '<img src="/static/deck7/card3.png"/>', '<img src="/static/deck7/card4.png"/>', '<img src="/static/deck7/card5.png"/>', '<img src="/static/deck7/card6.png"/>', '<img src="/static/deck7/card7.png"/>', '<img src="/static/deck7/card8.png"/>', '<img src="/static/deck7/card9.png"/>', '<img src="/static/deck7/card10.png"/>', '<img src="/static/deck7/card11.png"/>']
                    },
                {
                    'question': 'Change the equation $4x = 2y-3$ into standard form. Place the cards below in the correct order to show the steps.',
                    'shuffle': [0, 6 ,6 ,1 ,2 ,3 ,4 ,
                                6 ,6 ,6 ,6 ,6 ,3 ,5 ,
                                6 ,5 ,1 ,2 ,0 ,6 ,7],
                    #'solutions': [[6, 6, 0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 6, 6, 5, 3, 0, 1, 6, 6, 4]],
                    'solutions': [[0, 6, 6, 1, 2, 3, 4, 6, 6, 5, 6, 5, 6, 6, 0, 3, 2, 1, 6, 6, 7],[0, 6, 6, 1, 2, 3, 4, 5, 6, 6, 6, 5, 6, 6, 0, 3, 2, 1, 6, 6, 7],[0, 6, 6, 1, 2, 3, 4, 6, 5, 6, 6, 5, 6, 6, 0, 3, 2, 1, 6, 6, 7],[6, 6, 0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 6, 6, 5, 3, 0, 1, 6, 6, 4],[6, 6, 0, 1, 2, 3, 4, 6, 5, 6, 6, 5, 6, 6, 5, 3, 0, 1, 6, 6, 4],[6, 6, 0, 1, 2, 3, 4, 6, 6, 5, 6, 5, 6, 6, 5, 3, 0, 1, 6, 6, 4],],
                    'cards': ['<img src="/static/deck8/card0.png"/>','<img src="/static/deck8/card1.png"/>', '<img src="/static/deck8/card2.png"/>', '<img src="/static/deck8/card3.png"/>', '<img src="/static/deck8/card4.png"/>', '<img src="/static/deck8/card5.png"/>', '<img src="/static/deck8/card6.png"/>', '<img src="/static/deck8/card7.png"/>', '<img src="/static/deck8/card8.png"/>', '<img src="/static/deck8/card9.png"/>', '<img src="/static/deck8/card10.png"/>', '<img src="/static/deck8/card11.png"/>']
                    },
                {
                    'question': 'Change the equation $x = -2y-5$ into standard form. Place the cards below in the correct order to show the steps.',
                    'shuffle': [0 ,6 ,6 ,1 ,2 ,3 ,4 ,
                                6 ,6 ,6 ,6 ,6 ,0 ,5 ,
                                6 ,5 ,1 ,8 ,7 ,6 ,9],
                    'solutions': [
                        [0, 6, 6, 1, 2, 3, 4,
                         6, 6, 5, 6, 5, 6, 6,
                         0, 8, 7, 1, 6, 6, 9],
                        [0, 6, 6, 1, 2, 3, 4,
                         6, 5, 6, 6, 5, 6, 6,
                         0, 8, 7, 1, 6, 6, 9],
                        [0, 6, 6, 1, 2, 3, 4,
                         5, 6, 6, 6, 5, 6, 6,
                         0, 8, 7, 1, 6, 6, 9],
                        [0, 6, 6, 1, 2, 3, 4,
                         6, 6, 5, 6, 5, 6, 6,
                         0, 8, 7, 1, 6, 9, 6],
                        [0, 6, 6, 1, 2, 3, 4,
                         6, 5, 6, 6, 5, 6, 6,
                         0, 8, 7, 1, 6, 9, 6],
                        [0, 6, 6, 1, 2, 3, 4,
                         5, 6, 6, 6, 5, 6, 6,
                         0, 8, 7, 1, 6, 9, 6],
                        [0, 6, 6, 1, 2, 3, 4,
                         6, 6, 5, 6, 5, 6, 6,
                         0, 8, 7, 1, 9, 6, 6],
                        [0, 6, 6, 1, 2, 3, 4,
                         6, 5, 6, 6, 5, 6, 6,
                         0, 8, 7, 1, 9, 6, 6],
                        [0, 6, 6, 1, 2, 3, 4,
                         5, 6, 6, 6, 5, 6, 6,
                         0, 8, 7, 1, 9, 6, 6],
                        ],
                    'cards': ['<img src="/static/deck9/card0.png"/>','<img src="/static/deck9/card1.png"/>', '<img src="/static/deck9/card2.png"/>', '<img src="/static/deck9/card3.png"/>', '<img src="/static/deck9/card4.png"/>', '<img src="/static/deck9/card5.png"/>', '<img src="/static/deck9/card6.png"/>', '<img src="/static/deck9/card7.png"/>', '<img src="/static/deck9/card8.png"/>', '<img src="/static/deck9/card9.png"/>', '<img src="/static/deck9/card10.png"/>', '<img src="/static/deck9/card11.png"/>']
                    },
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTableAndSetOfCoordinatePairsEquation',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': r'Write the equation $y=3x+6$ in standard form. Fill in the $x$ and $y$-intercepts in the the table. Then graph the relationship.', 'x': [None,0], 'y': [0,None], 'variables': ['x','y'],
                    'grid_x': json.dumps([x[0] for x in gen_grid(-1,8,-1,8,1,1)]),
                    'grid_y': json.dumps([x[1] for x in gen_grid(-1,8,-1,8,1,1)]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'equation': 'y=3x+4',
                 },
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTableAndSetOfCoordinatePairsEquation',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': r'Write the equation $y=4+x$ in standard form. Fill in the $x$ and $y$-intercepts in the table. Then graph the relationship.', 'x': [0,None], 'y': [None,0], 'variables': ['x','y'],
                    'grid_x': json.dumps([x[0] for x in gen_grid(-1,14,-1,14,1,1)]),
                    'grid_y': json.dumps([x[1] for x in gen_grid(-1,14,-1,14,1,1)]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'equation': 'y=4+x',
                    'explanation': False,
                 },
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTableAndSetOfCoordinatePairsEquation',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': r'Graph $x=3$ by filling in the missing entries of the table and then graphing the points.', 'x': [None,None], 'y': [2,8], 'variables': ['x','y'],
                    'grid_x': json.dumps([x[0] for x in gen_grid(-1,14,-1,14,1,1)]),
                    'grid_y': json.dumps([x[1] for x in gen_grid(-1,14,-1,14,1,1)]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'equation': 'x=3',
                    'explanation': False,
                 },
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTableAndSetOfCoordinatePairsEquation',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': r'Graph $y=-2$ by filling in the missing entries of the table and then graphing the points.', 'x': [5,1], 'y': [None,None], 'variables': ['x','y'],
                    'grid_x': json.dumps([x[0] for x in gen_grid(-5,5,-5,5,1,1)]),
                    'grid_y': json.dumps([x[1] for x in gen_grid(-5,5,-5,5,1,1)]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'equation': 'y=-2',
                    'explanation': False,
                 },
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTableAndSetOfCoordinatePairsEquation',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': r'Graph $2x+4y=16$ by making a table and then graphing the points. (You can choose any value of $x$ between $-5$ and $5$.)', 'x': [None,None], 'y': [None,None], 'variables': ['x','y'],
                    'grid_x': json.dumps([x[0] for x in gen_grid(-5,5,-5,8,0.5,0.5)]),
                    'grid_y': json.dumps([x[1] for x in gen_grid(-5,5,-5,8,0.5,0.5)]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'equation': '2x+4y=16',
                    'explanation': False,
                 },
                ],
            'SpaceAfter': '4cm',
            },
        ]
    },
    'SeekingShelterB': {
        'ProvideImmediateFeedback': True,
        'Title': 'December 6: Seeking Shelter: How is the homeless population changing around the country?',
        'Questions': [
            {
            'Type': 'OpenResponse',
            'Template': 'OpenResponse.html',
            'ParameterSetVariants': [
                {'question': 'Bellringer: What do you think it would feel like not to have a permanent home?',
                    #'image': '/static/PerimeterLinearEquation.png',
                    'html': '<iframe id="vzvd-18185520" name="vzvd-18185520" title="video player" class="video-player d-block" type="text/html" width="918" height="516" frameborder="0" allowFullScreen="" allowTransparency="true" src="https://view.vzaar.com/18185520/player">',
                    'no_answer': json.dumps(True),
                },
                {'question': 'New York and Los Angeles are two of the largest cities in the United States. They’re also two of the most expensive. As more people move there, the cost of renting an apartment goes up...as does the number of people experiencing homelessness on any given night. Between 2011 and 2017, in which city would you say the homeless population grew by more? Explain.',
                    'image': '/static/HomelessnessQuestion1.png',
                    #'html': '<iframe class="interactive-iframe" frameborder="no" height="520" scrolling="no" src="https://mathalicious-production.s3.amazonaws.com/interactives/lessons/SeekingShelter/Q1.html?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIAIACU7RQ26H7DPBYQ%2F20191206%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20191206T124450Z&amp;X-Amz-Expires=900&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=215d0d51a3ab5ff26aaa1ec4fcfe4799e85d1e76a16c54eac7a86bf0a1ebae37" width="100%" id="iFrameResizer1" style="overflow: hidden; height: 639px;"></iframe>',
                    'no_answer': json.dumps(True),
                },
            ],
            'SpaceAfter': '6cm',
            },
            {
            'Type': 'SetOfCoordinatePairsEquationAndPrediction',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': 'Let’s assume the homeless population increases by a constant amount each year. If we round the data to the nearest thousand, the equation for the line in the NYC graph is $y = 50,000 + 4,000x$, where $y$ is the total number of homeless people and $x$ is the number of years since 2011. Project how many people you expect will be homeless in NYC in ten years.',
                    'image': '/static/HomelessnessQuestion1.png',
                    'equation': 'y = 50000 + 4000x',
                    'grid_x': json.dumps([x[0] for x in homelessness_grid]),
                    'grid_y': json.dumps([x[1] for x in homelessness_grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1000),
                    'variables': ['y','x'],
                    'x0': '18',
                    'explanation': True,
                    'no_answer': json.dumps(True),
                },
                {'question': 'Let’s assume the homeless population increases by a constant amount each year. If we round the data to the nearest thousand, the equation for the line in the LA graph is $y = 35,000 + 3,000x$, where $y$ is the total number of homeless people and $x$ is the number of years since 2011. Project how many people you expect will be homeless in LA in ten years.',
                    'image': '/static/HomelessnessQuestion1.png',
                    'equation': 'y =  35000 + 3000x',
                    'grid_x': json.dumps([x[0] for x in homelessness_grid]),
                    'grid_y': json.dumps([x[1] for x in homelessness_grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1000),
                    'variables': ['y','x'],
                    'x0': '18',
                    'explanation': True,
                    'no_answer': json.dumps(True),
                },
            ],
            'SpaceAfter': '6cm',
            },
            {
            'Type': 'OpenResponse',
            'Template': 'OpenResponse.html',
            'ParameterSetVariants': [
                {'question': 'According to the U.S. government, more than 500,000 people are experiencing homelessness at any given moment; this includes everyone from veterans to kids. Watch the videos about homelessness in cities around the country. Who do you think should be responsible for ensuring that people have safe and affordable places to live: governments, charities, employers, or individuals? Is there anything that you can do to help?',
                    #'image': '/static/HomelessnessQuestion3.png',
                    #'html': '<iframe class="interactive-iframe" frameborder="no" height="520" scrolling="auto" src="https://mathalicious-production.s3.amazonaws.com/interactives/lessons/SeekingShelter/Q0.html?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIAIACU7RQ26H7DPBYQ%2F20191206%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20191206T124110Z&amp;X-Amz-Expires=900&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=019ffdae23eb4aa635b2366475789f626515dc628e48ebfa54fc413508b70cf7" width="100%"></iframe>',
                    'no_answer': json.dumps(True),
                },
                #{'question': 'Bellringer: What do you think it would feel like not to have a permanent home?',
                #    'no_answer': json.dumps(True),
                #},
            ],
            'SpaceAfter': '6cm',
            },
        ]
    },
    'FindXAndYInterceptsAndPredict': {
        'ProvideImmediateFeedback': True,
        'Title': 'December 5: Graph a linear equation and predict an output for a given input',
        'Questions': [
#            {
#            'Type': 'OpenResponse',
#            'Template': 'OpenResponse.html',
#            'ParameterSetVariants': [
#                {'question': 'Bellringer: The graph shown has an x-intercept of 12 and a y-intercept of 6. Think of this graph as a function. Can you use the graph to predict the output $y$ when the input $x$ is 6? Can you predict the output when $x$ is greater than 12? Write any questions that you have, or give your answers and explain how you found them.',
#                    'grid_x': json.dumps([x[0] for x in grid]),
#                    'grid_y': json.dumps([x[1] for x in grid]),
#                    'N': json.dumps(2),
#                    'image': '/static/PredictBasedOnLineBellringer.png',
#                    'no_answer': json.dumps(True),
#                },
#            ],
#            'SpaceAfter': '6cm',
#            },
            {
            'Type': 'OpenResponse',
            'Template': 'OpenResponse.html',
            'ParameterSetVariants': [
                {'question': 'Bellringer: You want to build a swimming pool with stone slabs around the perimeter. The total length of your stone slabs is 72 feet. You choose variables $x$ and $y$ to represent the lengths of the sides of your pool. What are some possible values of $x$ and $y$?',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'image': '/static/PerimeterLinearEquation.png',
                    'no_answer': json.dumps(True),
                },
            ],
            'SpaceAfter': '6cm',
            },
            {
            'Type': 'SetOfCoordinatePairsEquationAndPrediction',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': 'You are building a swimming pool with a perimeter of 72 feet, and there are two sides with length $x$ and two sides with length $y$. You write the equation $2x+2y=72$. Graph this equation. If the length $x$ is 12, what must $y$ be?',
                    'image': '/static/PerimeterLinearEquation.png',
                    'grid_x': json.dumps([x[0] for x in grid36x36]),
                    'grid_y': json.dumps([x[1] for x in grid36x36]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': '2x+2y=72',
                    'x0': '12',
                    'explanation': True,
                },
                {'question': 'Graph the equation $x+y=4$. Then predict the output when $x=3$.',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': 'x+y=4',
                    'x0': '3',
                    'explanation': True,
                },
                {'question': 'Graph the equation $3x+6y=18$. Then predict the output when $x=3$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': '3x+6y=18',
                    'x0': '3',
                    'explanation': True,
                },
                {'question': 'Graph the equation $2x+4y=20$. Then predict the output when $x=5$.',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': '2x+4y=20',
                    'x0': '5',
                    'explanation': True,
                },
                {'question': 'Graph the equation $5x+3y=30$. Then predict the output when $x=2$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': '5x+3y=30',
                    'x0': '2',
                    'explanation': True,
                },
                {'question': 'Graph the equation $2x+y=10$. Then predict the output when $x=20$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': '2x+y=10',
                    'x0': '20',
                    'explanation': True,
                },
                {'question': 'Graph the equation $2x+4y=8$. Then predict the output when $x=15$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': '2x+4y=8',
                    'x0': '15',
                    'explanation': True,
                },
                {'question': 'Graph the equation $x+y=-2$. Then predict the output when $x=2$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': 'x+y=-2',
                    'x0': '2',
                    'explanation': True,
                },
                {'question': 'Graph the equation $5x-y=10$. Then predict the output when $x=1$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': '5-y=10',
                    'x0': '1',
                    'explanation': True,
                },
            ],
            'SpaceAfter': '6cm',
            },
        ]
    },
    'FindXAndYInterceptsAndPredictA': {
        'ProvideImmediateFeedback': True,
        'Title': 'December 5: Graph a linear equation and predict an output for a given input',
        'Questions': [
            {
            'Type': 'OpenResponse',
            'Template': 'OpenResponse.html',
            'ParameterSetVariants': [
                {'question': 'Bellringer: The graph shown has an x-intercept of 12 and a y-intercept of 6. Think of this graph as a function. Can you use the graph to predict the output $y$ when the input $x$ is 6? Can you predict the output when $x$ is greater than 12? Write any questions that you have, or give your answers and explain how you found them.',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'image': '/static/PredictBasedOnLineBellringer.png',
                    'no_answer': json.dumps(True),
                },
            ],
            'SpaceAfter': '6cm',
            },
            {
            'Type': 'SetOfCoordinatePairsEquationAndPrediction',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': 'Graph the equation $x+y=4$. Then predict the output when $x=3$.',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': 'x+y=4',
                    'x0': '3',
                    'explanation': True,
                },
                {'question': 'Graph the equation $4x+2y=12$. Then predict the output when $x=3$.',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': '4x+2y=12',
                    'x0': '3',
                    'explanation': True,
                },
                {'question': 'Graph the equation $3x+6y=18$. Then predict the output when $x=3$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': '3x+6y=18',
                    'x0': '3',
                    'explanation': True,
                },
                {'question': 'Graph the equation $2x+4y=20$. Then predict the output when $x=5$.',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': '2x+4y=20',
                    'x0': '5',
                    'explanation': True,
                },
                {'question': 'Graph the equation $5x+3y=30$. Then predict the output when $x=2$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': '5x+3y=30',
                    'x0': '2',
                    'explanation': True,
                },
                {'question': 'Graph the equation $2x+y=10$. Then predict the output when $x=20$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': '2x+y=10',
                    'x0': '20',
                    'explanation': True,
                },
                {'question': 'Graph the equation $2x+4y=8$. Then predict the output when $x=15$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': '2x+4y=8',
                    'x0': '15',
                    'explanation': True,
                },
                {'question': 'Graph the equation $x+y=-2$. Then predict the output when $x=2$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': 'x+y=-2',
                    'x0': '2',
                    'explanation': True,
                },
                {'question': 'Graph the equation $5x-y=10$. Then predict the output when $x=1$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': '5-y=10',
                    'x0': '1',
                    'explanation': True,
                },
            ],
            'SpaceAfter': '6cm',
            },
        ]
    },
    'StainedGlassGraphs': {
        'ProvideImmediateFeedback': True,
        'Title': "Stained Glass Graphs",
        'Questions': [
            {
            'Type': 'SetOfCoordinatePairs',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': '$x+2y=-8$',
                    'grid_x': json.dumps(numpy.linspace(-12,12,num=25).tolist()+[0]*25),
                    'grid_y': json.dumps([0]*25+numpy.linspace(-12,12,num=25).tolist()),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'set_of_coordinate_pairs': {(0,-4),(-8,0)},
                    'N': json.dumps(2),
                },
                {'question': '$x+y=12$',
                    'grid_x': json.dumps(numpy.linspace(-12,12,num=25).tolist()+[0]*25),
                    'grid_y': json.dumps([0]*25+numpy.linspace(-12,12,num=25).tolist()),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'set_of_coordinate_pairs': {(0,12),(12,0)},
                    'N': json.dumps(2),
                },
            ],
            'SpaceAfter': '3cm',
            },
            {
            'Type': 'SetOfCoordinatePairsEquation',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': '$y=12$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': 'y=12',
                },
                {'question': '$x=0$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': 'x=0',
                },
                {'question': '$-x+2y=8$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': '-x+2y=8',
                },
                {'question': '$-x+2y=-8$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': '-x+2y=-8',
                },
                {'question': '$x+2y=8$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': 'x+2y=8',
                },
                {'question': '$y=x+12$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': 'y=x+12',
                },
                {'question': '$y=-12$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': 'y=-12',
                },
                {'question': '$y=-x-12$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': 'y=-x-12',
                },
                {'question': '$y=x-12$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': 'y=x-12',
                },
            ],
            'SpaceAfter': '2.5cm',
            },
        ]
    },
    'XAndYInterceptsPractice': {
        'ProvideImmediateFeedback': True,
        'Title': 'December 4: x- and y-Intercepts',
        'Questions': [
            {
            'Type': 'OpenResponse',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': 'Bellringer: Can you draw a line that has only an x-intercept or only a y-intercept? Tap on the coordinate grid at two points to try to draw such a line. Then explain your answer in the box below.',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'no_answer': json.dumps(True),
                },
            ],
            'SpaceAfter': '6cm',
            },
            {
            'Type': 'SetOfCoordinatePairsEquation',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': '$y=5$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': 'y=5',
                },
                {'question': '$x=-2$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': 'x=-2',
                },
                {'question': '$2x+5=19$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': 'x=7',
                },
                {'question': '$5-y=10$',
                    'grid_x': json.dumps([x[0] for x in grid]),
                    'grid_y': json.dumps([x[1] for x in grid]),
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                    'variables': ['x','y'],
                    'equation': '5-y=10',
                },
            ],
            'SpaceAfter': '6cm',
            },
        ]
    },
#            {
#            'Type': 'SetOfCoordinatePairs',
#            'Template': 'PlotQuestion.html',
#            'ParameterSetVariants': [
#                {'question': 'Plot the linear equation $x=5$ using the x- and y-intercepts.',
#                    'grid_x': json.dumps(numpy.linspace(-1,5,num=13).tolist()+[0]*13),
#                    'grid_y': json.dumps([0]*13+numpy.linspace(-1,5,num=13).tolist()),
#                    'set_of_coordinate_pairs': {(0,3.0/2),(3,0)},
#                    'N': json.dumps(2),
#                },
#                {'question': 'Plot the linear equation $7x+14y=21$ using the x- and y-intercepts.',
#                    'grid_x': json.dumps(numpy.linspace(-1,5,num=13).tolist()+[0]*13),
#                    'grid_y': json.dumps([0]*13+numpy.linspace(-1,5,num=13).tolist()),
#                    'set_of_coordinate_pairs': {(0,3.0/2),(3,0)},
#                    'N': json.dumps(2),
#                },
#            ],
#            'SpaceAfter': '6cm',
#            },
#        ]
#    },
    'HomeworkDec3': {
        'ProvideImmediateFeedback': True,
        'Questions': [
            {
            'Type': 'SetOfCoordinatePairs',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': 'Plot the linear equation $y=4+2x$ using the x- and y-intercepts.',
                    'grid_x': json.dumps([-4,-3,-2,-1,1,2,3,4,5,6,7,8,0,0,0,0,0,0,0,0,0]),
                    'grid_y': json.dumps([0,0,0,0,0,0,0,0,0,0,0,0,-1,1,2,3,4,5,6,7,8]),
                    'set_of_coordinate_pairs': {(0,4),(-2,0)},
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                },
                {'question': 'Plot the linear equation $5-y=-3x$ using the x- and y-intercepts.',
                    'grid_x': json.dumps(numpy.linspace(-3,5,num=25).tolist()+[0]*25),
                    'grid_y': json.dumps([0]*25+numpy.linspace(-3,5,num=25).tolist()),
                    'set_of_coordinate_pairs': {(0,5),(-5.0/3,0)},
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                },
                {'question': 'Plot the linear equation $x=5y+5$ using the x- and y-intercepts.',
                    'grid_x': json.dumps(numpy.linspace(-2,6,num=9).tolist()+[0]*9),
                    'grid_y': json.dumps([0]*9+numpy.linspace(-2,6,num=9).tolist()),
                    'set_of_coordinate_pairs': {(0,-1),(5,0)},
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                },
                {'question': 'Plot the linear equation $x+y=4$ using the x- and y-intercepts.',
                    'grid_x': json.dumps(numpy.linspace(-2,6,num=9).tolist()+[0]*9),
                    'grid_y': json.dumps([0]*9+numpy.linspace(-2,6,num=9).tolist()),
                    'set_of_coordinate_pairs': {(0,4),(4,0)},
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                },
                {'question': 'Plot the linear equation $y=8-6x$ using the x- and y-intercepts.',
                    'grid_x': json.dumps(numpy.linspace(-1,10,num=45).tolist()+[0]*45),
                    'grid_y': json.dumps([0]*45+numpy.linspace(-1,10,num=45).tolist()),
                    'set_of_coordinate_pairs': {(0,8),(-4.0/3,0)},
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                },
                ],
            'SpaceAfter': '6cm',
            },
        ]
    },
    'LinearEquationsInStandardFormPart3': {
        'ProvideImmediateFeedback': True,
        'Questions': [
            {
            'Type': 'OpenResponse',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'What questions do you have about graphing linear equations?',}
                ],
            'SpaceAfter': '6cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': r'Each pair of socks in a store costs \$6, and each pair of gloves costs \$12. You have exactly \$48, and you want to spend all of it. Let $s$ be the number of pairs of socks and let $g$ be the number of pairs of gloves that you buy. Make a table with pairs of values of $s$ and $g$ that would work. Then graph the relationship.', 'equation': '6s+12g=48', 'variables': ['s','g'], 'n': 3},
                ],
            'SpaceAfter': '6cm',
            },
            {
            'Type': 'SetOfCoordinatePairs',
            'Template': 'PlotQuestion.html',
            'ParameterSetVariants': [
                {'question': 'Plot the linear equation $4x+2y=8$ using the x- and y-intercepts.',
                    'grid_x': json.dumps([-1,1,2,3,4,5,6,7,8,0,0,0,0,0,0,0,0,0]),
                    'grid_y': json.dumps([0,0,0,0,0,0,0,0,0,-1,1,2,3,4,5,6,7,8]),
                    'set_of_coordinate_pairs': {(0,4),(2,0)},
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                },
                {'question': 'What is the x-intercept of the linear equation $5x+2y=10$?',
                    'grid_x': json.dumps([1,2,3,4,5,6,7,8,0,0,0,0,0,0,0,0]),
                    'grid_y': json.dumps([0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8]),
                    'set_of_coordinate_pairs': {(2,0)},
                    'N': json.dumps(1),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                },
                {'question': 'What is the y-intercept of the linear equation $5x+2y=10$?',
                    'grid_x': json.dumps([1,2,3,4,5,6,7,8,0,0,0,0,0,0,0,0]),
                    'grid_y': json.dumps([0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8]),
                    'set_of_coordinate_pairs': {(0,5)},
                    'N': json.dumps(1),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                },
                {'question': 'Plot the linear equation $5x+10y=40$ using the x- and y-intercepts.',
                    'grid_x': json.dumps([-1,1,2,3,4,5,6,7,8,0,0,0,0,0,0,0,0,0]),
                    'grid_y': json.dumps([0,0,0,0,0,0,0,0,0,-1,1,2,3,4,5,6,7,8]),
                    'set_of_coordinate_pairs': {(0,4),(8,0)},
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                },
                {'question': 'What is the x-intercept of the linear equation $4x+3y=12$?',
                    'grid_x': json.dumps([1,2,3,4,5,6,7,8,0,0,0,0,0,0,0,0]),
                    'grid_y': json.dumps([0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8]),
                    'set_of_coordinate_pairs': {(3,0)},
                    'N': json.dumps(1),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                },
                {'question': 'What is the y-intercept of the linear equation $4x+3y=12$?',
                    'grid_x': json.dumps([1,2,3,4,5,6,7,8,0,0,0,0,0,0,0,0]),
                    'grid_y': json.dumps([0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8]),
                    'set_of_coordinate_pairs': {(0,4)},
                    'N': json.dumps(1),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                },
                {'question': 'Plot the linear equation $y=8-2x$ using the x- and y-intercepts.',
                    'grid_x': json.dumps([-1,1,2,3,4,5,6,7,8,0,0,0,0,0,0,0,0,0]),
                    'grid_y': json.dumps([0,0,0,0,0,0,0,0,0,-1,1,2,3,4,5,6,7,8]),
                    'set_of_coordinate_pairs': {(0,8),(4,0)},
                    'N': json.dumps(2),
                    'dtickx': json.dumps(1),
                    'dticky': json.dumps(1),
                },
            ],
            'SpaceAfter': '6cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'Make a table of numbers x and y that are solutions to the equation $y=8-2x$.', 'equation': 'y=8-2x', 'n': 3, 'variables': ['x','y']},
                ],
            'SpaceAfter': '6cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': r'Make a table to of values of $f$ and $s$ that are solutions to the equation $5f+s=36$.', 'equation': '5f+s=36', 'variables': ['f','s'], 'n': 3},
                ],
            'SpaceAfter': '6cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'Make a table of numbers x and y that are solutions to the equation $12x+3y=36$.', 'equation': '12x+3y=36', 'n': 3, 'variables': ['x','y']},
                {'question': 'Make a table of numbers x and y that are solutions to the equation $x=7y$.', 'equation': 'x=7y', 'n': 3, 'variables': ['x','y']},
                {'question': 'Make a table of numbers x and y that are solutions to the equation $x=5$.', 'equation': 'x=5', 'n': 3, 'variables': ['x','y']},
                ],
            'SpaceAfter': '6cm',
            },
        ]
    },
    'LinearEquationsInStandardFormPart2': {
        'ProvideImmediateFeedback': True,
        'Questions': [
            {
            'Type': 'OpenResponse',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'What is one thing that you will do to be successful in math class during the next three weeks?',}
                ],
            'SpaceAfter': '6cm',
            },
            {
            'Type': 'OpenResponse',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'One quantity that I care about and that can change is...',}
                ],
            'SpaceAfter': '6cm',
            },
            {
            'Type': 'GenericEquality',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'You want to save \$200 to buy a gift for a friend. Suppose you have \$80, and you earn \$10 every week for an allowance. How many weeks will it take to earn enough money?', 'CorrectAnswer': '12', 'explanation': True}
                ],
            'SpaceAfter': '6cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'Suppose you want to save \$300 to buy a gift in the next 12 weeks. Suppose your friend is also going to save money each week. How much money do you and your friend each need to save each week? Let $m$ be how much you need to save each week and let $f$ be how much your friend needs to save each week. Put your answers in the table.',
                    'equation': '12f+12m=300', 'n': 2, 'variables': ['f','m'], 'explanation': True}
                ],
            'SpaceAfter': '6cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'Find pairs of numbers x and y that are solutions to the equation $12x+12y=300$.', 'equation': '12x+12y=300', 'n': 4, 'variables': ['x','y']}
                ],
            'SpaceAfter': '6cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'Find pairs of numbers x and y that are solutions to the equation $6x+2y=24$.', 'equation': '6x+2y=24', 'n': 4, 'variables': ['x','y']}
                ],
            'SpaceAfter': '6cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': r'Each book in a store costs \$8, and each pen costs \$4. You want to spend exactly \$24. Let $b$ be the number of books and let $p$ be the number of pens that you buy. Make a table with 3 pairs of values that you could use.', 'equation': '8b+4p=24', 'variables': ['b','p'], 'n': 3},
                ],
            'SpaceAfter': '6cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'Make a table of numbers x and y that are solutions to the equation $5x+10y=75$.', 'equation': '5x+10y=75', 'n': 3, 'variables': ['x','y']}
                ],
            'SpaceAfter': '6cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': r'Each pair of socks in a store costs \$6, and each pair of gloves costs \$12. You have exactly \$48, and you want to spend all of it. Let $s$ be the number of pairs of socks and let $g$ be the number of pairs of gloves that you buy. Make a table with pairs of values of $s$ and $g$ that would work. Then graph the relationship.', 'equation': '6s+12g=48', 'variables': ['s','g'], 'n': 3},
                ],
            'SpaceAfter': '6cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': r'Louisa has \$36 in five-dollar bills and singles. Make a table to show how many of each type she could have. Let of $f$ stand for the number of five-dollar bills and let $s$ stand for the number of singles.', 'equation': '5f+s=36', 'variables': ['f','s'], 'n': 3},
                ],
            'SpaceAfter': '6cm',
            },
        ]
    },
    'LinearEquationsInStandardFormB': {
        'ProvideImmediateFeedback': True,
        'Questions': [
            {
            'Type': 'OpenResponse',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'You have 12 dollars to spend and plan on spending all of your money. You are going to spend all of your money on pop and candy. You can buy bottles of pop for \$2 each and a bag of candy for \$1 each. How many of each will you buy?',}
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': r'Let $p$ be the number of bottles of pop that you buy, and let $c$ stand for the number of bags of candy. Can you come up with more than one combination of $p$ and $c$ that you can buy and still spend all of your money?<br/> $\textbf{Original problem}$: You have 12 dollars to spend and plan on spending all of your money. You are going to spend all of your money on pop and candy. You can buy bottles of pop for \$2 each and a bag of candy for \$1 each. How many of each will you buy? <br/>', 'equation': '2p+c=12', 'variables': ['p','c'], 'n': 4},
                ],
            'SpaceAfter': '4cm',
            },
#            {
#            'Type': 'InputOutputTable',
#            'Template': 'Graph.html',
#            'ParameterSetVariants': [
#                {'question': r'You have 12 dollars to spend and plan on spending all of your money. You are going to spend all of your money on pop and candy. You can buy bottles of pop for \$2 each and a bag of candy for \$1 each. How many of each will you buy? The graph shows some possible combinations. Make a table of the values shown in the graph.', 'x': [6,4,2,0], 'y': [0,4,8,12], 'variables': ['x','y']},
#                ],
#            'SpaceAfter': '4cm',
#            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'Find pairs of numbers x and y that add up to 12, make a table, and plot the points in the coordinate plane.', 'equation': 'x+y=12', 'n': 4, 'variables': ['x','y']}
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'FindValues',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': r'A $\textbf{linear equation}$ is an equation that forms a line when graphed. A linear equation can be written in the form $Ax+By=C$. This is called the $\textbf{standard form}$ of a linear equation. How can you write an equation in standard for the problem: <br/><br/>$\textbf{Find pairs of numbers x and y that add up to 12.}$. Write your equation and then find the values of $A$, $B$, and $C$.', 'equation': 'x+y=12', 'variables': [('A', '1'),('B', '1'),('C', '12')]},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': r'Suppose you have 20 feet of fencing to enclose all four sides of a rectangular yard. Let $x$ and $y$ be the length and width of a yard in feet. Find four possible combinations of $x$ and $y$, the lengths and widths of yards that can be enclosed with 20 feet of fencing. <br/><br/>Suppose you have 20 feet of fencing.', 'equation': '2x+2y=20', 'variables': ['x','y'], 'n': 4},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'FindValues',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': r'Let $x$ and $y$ be the length and width of the yard in feet. Suppose you have 20 feet of fencing. Use the variables $x$ and $y$ to write an equation that you could use to find the lengths and widths of yards that can be enclose with 20 feet of fencing. <br/><br/>Write an equation, in standard form $Ax+By=C$ and determine the values of $A$, $B$, and $C$.', 'equation': '2x+2y=20', 'variables': [('A', '2'),('B', '2'),('C', '20')]},
                ],
            'SpaceAfter': '4cm',
            },
#            {
#            'Type': 'FindValues',
#            'Template': 'Question.html',
#            'ParameterSetVariants': [
#                {'question': r'Write the equation $y=-3x+18$ in standard form $Ax+By=C$.', 'equation': '3x+y=18', 'variables': [('A', '3'),('B', '1'),('C', '18')]},
#                ],
#            'SpaceAfter': '4cm',
#            },
#            {
#            'Type': 'FindValues',
#            'Template': 'Question.html',
#            'ParameterSetVariants': [
#                {'question': r'Write the equation $y+2x-6=0$ in standard form $Ax+By=C$.', 'equation': '2x+y=6', 'variables': [('A', '2'),('B', '1'),('C', '6')]},
#                ],
#            'SpaceAfter': '4cm',
#            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'Find pairs of numbers x and y that are solutions to the equation $4x+2y=24$.', 'equation': '4x+2y=24', 'n': 4, 'variables': ['x','y']}
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'Make a table of numbers x and y that are solutions to the equation $3x+6y=42$.', 'equation': '3x+6y=42', 'n': 3, 'variables': ['x','y']}
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'Make a table of pairs of numbers x and y that are solutions to the equation $x=-3y+27$.', 'equation': 'x+3y=27', 'n': 3, 'variables': ['x','y']}
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'Make a table of pairs of numbers x and y that are solutions to the equation $y=-8x$.', 'equation': 'y=-8x', 'n': 3, 'variables': ['x','y']},
                {'question': 'Make a table of pairs of numbers x and y that are solutions to the equation $3x=y$.', 'equation': '3x=y', 'n': 3, 'variables': ['x','y']},
                {'question': 'Make a table of pairs of numbers x and y that are solutions to the equation $y-8=-x$.', 'equation': 'y-8=-x', 'n': 3, 'variables': ['x','y']},
                {'question': 'Make a table of pairs of numbers x and y that are solutions to the equation $x=10-y$.', 'equation': 'x=10-y', 'n': 3, 'variables': ['x','y']}
                ],
            'SpaceAfter': '4cm',
            },
        ]
    },
    'LinearEquationsInStandardForm': {
        'ProvideImmediateFeedback': True,
        'Questions': [
            {
            'Type': 'OpenResponse',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'You have 12 dollars to spend and plan on spending all of your money. You are going to spend all of your money on pop and candy. You can buy bottles of pop for \$2 each and a bag of candy for \$1 each. How many of each will you buy?',}
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': r'Let $p$ be the number of bottle of pop that you buy, and let $c$ stand for the number of bags of candy. Can you come up with more than one combination of $p$ and $c$ that you can buy and still spend all of your money?<br/> $\textbf{Original problem}$: You have 12 dollars to spend and plan on spending all of your money. You are going to spend all of your money on pop and candy. You can buy bottles of pop for \$2 each and a bag of candy for \$1 each. How many of each will you buy? <br/>', 'equation': '2p+c=12', 'variables': ['p','c'], 'n': 4},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTable',
            'Template': 'Graph.html',
            'ParameterSetVariants': [
                {'question': r'You have 12 dollars to spend and plan on spending all of your money. You are going to spend all of your money on pop and candy. You can buy bottles of pop for \$2 each and a bag of candy for \$1 each. How many of each will you buy? The graph shows some possible combinations. Make a table of the values shown in the graph.', 'x': [6,4,2,0], 'y': [0,4,8,12], 'variables': ['x','y']},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'Find pairs of numbers x and y that add up to 12, make a table, and plot the points in the coordinate plane.', 'equation': 'x+y=12', 'n': 4, 'variables': ['x','y']}
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'FindValues',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': r'A $\textbf{linear equation}$ is an equation that forms a line when graphed. A linear equation can be written in the form $Ax+By=C$. This is called the $\textbf{standard form}$ of a linear equation. How can you write an equation in standard for the problem: <br/><br/>$\textbf{Find pairs of numbers x and y that add up to 12.}$. Write your equation and then find the values of $A$, $B$, and $C$.', 'equation': 'x+y=12', 'variables': [('A', '1'),('B', '1'),('C', '12')]},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'FindValues',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': r'A linear equation is an equation that forms a line when graphed. A linear equation can be written in the form $Ax+By=C$. This is called the $\textbf{standard form}$ of a linear equation. How can you write an equation in standard for the problem: $\textbf{Find pairs of numbers x and y that add up to 12.}$', 'equation': 'x+y=12', 'variables': [('A', '1'),('B', '1'),('C', '12')]},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'FindValues',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': r'Let $x$ and $y$ be the length and width of a yard in feet. Suppose you have 20 feet of fencing. How can you write an equation in standard form to represent the sizes of yards that you could enclose using all of the fencing? <br/><br/>Write an equation, in standard form $Ax+By=C$ and determine the values of $A$, $B$, and $C$.', 'equation': '2x+2y=20', 'variables': [('A', '2'),('B', '2'),('C', '20')]},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': r'Use your equation to find four possible combinations of $x$ and $y$, the lengths and widths of yards that can be enclosed with 20 feet of fencing. <br/><br/>$\textbf{Original Problem:}$ Let $x$ and $y$ be the length and width of a yard in feet. Suppose you have 20 feet of fencing. How can you write an equation in standard form to represent the sizes of yards that you could enclose using all of the fencing? ', 'equation': '2x+2y=20', 'variables': ['x','y'], 'n': 4},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'FindValues',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': r'Write the equation $y=-3x+18$ in standard form $Ax+By=C$.', 'equation': '3x+y=18', 'variables': [('A', '3'),('B', '1'),('C', '18')]},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'FindValues',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': r'Write the equation $y+2x-6=0$ in standard form $Ax+By=C$.', 'equation': '2x+y=6', 'variables': [('A', '2'),('B', '1'),('C', '6')]},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'Find pairs of numbers x and y that are solutions to the equation $4x+2y=24$.', 'equation': '4x+2y=24', 'n': 4, 'variables': ['x','y']}
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'Find pairs of numbers x and y that are solutions to the equation $3x+6y=42$.', 'equation': '3x+6y=42', 'n': 4, 'variables': ['x','y']}
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTableEquation',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'Find pairs of numbers x and y that are solutions to the equation $x=-3y+27$.', 'equation': 'x+3y=27', 'n': 4, 'variables': ['x','y']}
                ],
            'SpaceAfter': '4cm',
            },
        ]
    },
    'SolvingEquationsTestCorrections': {
        'ProvideImmediateFeedback': True,
        'Questions': [
        {
            #'Type': 'SolveEquation',
            'Type': 'SolveEquationGuided',
            'Template': 'SolveEquationGuided.html',
            'ParameterSetVariants': [
                {'equation': 'x+6=19', 'CorrectAnswer': '13', 'variables': ['x']},
                {'equation': '83+y=57','CorrectAnswer': '-26', 'variables': ['y']},
                {'equation': '6x+8=32','CorrectAnswer': '4', 'variables': ['x']},
                {'equation': '65=5x-10','CorrectAnswer': '15', 'variables': ['x']},
                {'equation': '2(y+7)=49','CorrectAnswer': '35/2', 'variables': ['y']},
                {'equation': '81=4h+5h-9','CorrectAnswer': '10', 'variables': ['h']},
                {'equation': '8n-9=2n+3','CorrectAnswer': '2', 'variables': ['h']},
                {'equation': 'x-42=98-9x','CorrectAnswer': '14', 'variables': ['x']},
                ],
            'SpaceAfter': '4.5cm',
            },
        {
            #'Type': 'SolveEquation',
            'Type': 'GenericEquality',
            'Template': 'SolveEquation.html',
            'ParameterSetVariants': [
                {'equation': '3(x+4)=3x+11','CorrectAnswer': '{}'},
                {'equation': '|x-8|=3','equation_latex': '|x-8|=3', 'CorrectAnswer': '{5,11}'},
                {'equation': '(n-10)/12 = 8/3', 'equation': r'\frac{n-10}{12} = \frac{8}{3}','CorrectAnswer': '42'},
                {'equation': '4/6=8/x', 'equation': r'\frac{4}{6} = \frac{8}{x}','CorrectAnswer': '12'},
                ],
            'SpaceAfter': '4cm',
            },
        ]
    },
    'UsingDistributiveProperty': {
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
    'UsingZeroPairsAndReciprocalPairs': {
        'ProvideImmediateFeedback': True,
        'Questions': [
        {
            #'Type': 'SolveEquation',
            'Type': 'Expression',
            'Template': 'ReciprocalPair.html',
            'ParameterSetVariants': [
                {'expression': r'\frac{4}{3}','CorrectAnswer': '3/4'},
                {'expression': r'3', 'CorrectAnswer': '1/3'}, 
                {'expression': r'-\frac{2}{3}','CorrectAnswer': '-3/2'},
                ],
            'SpaceAfter': '2cm',
            },
        {
            'Type': 'Expression',
            'Template': 'ZeroPair.html',
            'ParameterSetVariants': [
                {'expression': r'10', 'CorrectAnswer': '-10'}, 
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
    'FunctionsTest': {
        'Title': 'Functions Test',
        'Test': False, #10:00
        'ProvideImmediateFeedback': False,
        'Questions':
        [
        {
            #'Type': 'SolveEquation',
            'Type': 'Matching',
            'Template': 'Matching.html',
            'ParameterSetVariants': [
                {'prompts': [
                    '(x,y) is called a _______________',
                    'A relationship that has one output for each input',
                    'The first coordinate of an ordered pair',
                    'The second coordinate of an ordered pair',
                    'The set of input values or x coordinates of a function',
                    'The set of output values or y coordinates of a function',
                    #'<img src="/mapping_diagram?x=2&x=3&x=4&y=1&y=1&y=1"/>'
                    ], 
                    'answers': {
                        'A':'Function',
                        'B':'y-coordinate',
                        'C':'x-coordinate',
                        'D':'Range',
                        'E':'Domain',
                        'F':'Ordered pair',
                    #    'G':'mapping diagram'
                        },
                    'CorrectAnswers': ['F','A','C','B','E','D']}, 
                ],
            'SpaceAfter': '2cm',
            },
            {
            'Type': 'MCGraph',
            'Template': 'MappingDiagram.html',
            'ParameterSetVariants': [
                {'question': 'Choose the graph of the relation shown in the mapping diagram.', 'x': [-3,-1,0,1,3], 'y': [3,1,0,1,3],
                    'Choices': [('a', {'seed': 10, 'n': 5}), ('b', {'x': [-3,-1,0,1,3], 'y': [3,1,0,1,3]}), ('c', {'seed': 12, 'n': 5}), ('d', {'x': [-3,-1,0,1,3], 'y': [0,1,3,1,0]})],
                    'CorrectAnswer': 'b'
                    },
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'MCMappingDiagram',
            'Template': 'Graph.html',
            'ParameterSetVariants': [
                {'question': 'Choose the mapping diagram of the relation shown in the graph.', 'x': [-4,-2,0,2,4], 'y': [-3,-1,1,3,5],
                    'Choices': [('a', {'x': [-4,-2,0,2,4], 'y': [5,3,1,-1,-3]}), ('b', {'seed': 1, 'n': 5}), ('c', {'seed': 2, 'n': 5}), ('d', {'x': [-4,-2,0,2,4], 'y': [-3,-1,1,3,5]})],
                    'CorrectAnswer': 'd'
                    },
                ],
            'SpaceAfter': '4cm',
            },
#            {
#            'Type': 'SelectMultiple',
#            'Template': 'Empty.html',
#            'ParameterSetVariants': [
#                {'image': None,
#                    'choices': [
#                        ('a','<img src="/mapping_diagram?x=2&x=3&x=4&y=1&y=1&y=1"/>'),
#                        ('b','<img src="/mapping_diagram?x=2&x=3&x=4&y=1&y=2&y=3"/>'),
#                        ],
#                    'question': "The main learning goals that you need to work on are ",
#                    'CorrectAnswer': None,
#                    },
#                ]
#            },
            {
            'Type': 'MC',
            'Template': 'MappingDiagram.html',
            'ParameterSetVariants': [
                {'question': 'Choose the set of ordered pairs that represents the relation in the mapping diagram.', 'n': 5, 'seed': 6,
                    'x': (-4,-2,0,2,4),
                    'y': (4,2,0,2,4),
                    'Choices': [('A', '$\{(-4,-2),(0,2),(2,4),(4,2),(2,4)\}$'),('B', '$\{(-4,4),(-2,2),(0,0),(2,2),(4,4)\}$'),('C', '$\{(4,-4),(2,-2),(0,0),(2,2),(4,4)\}$'), ('D', '$\{(4,0),(-2,4),(2,-4),(0,2),(4,2)\}$')],
                    'CorrectAnswer': 'B'
                },
            ],
            'SpaceAfter': '2cm',
            },
            {
            'Type': 'SetOfCoordinatePairs',
            'Template': 'MappingDiagram.html',
            'ParameterSetVariants': [
                {'question': 'Write the relation in the mapping diagram as a set of ordered pairs.', 'n': 5, 'seed': 6,
                    'set_of_coordinate_pairs': {(0,1),(1,2),(2,3),(3,4),(4,5)},
                    'x': (0,1,2,3,4),
                    'y': (1,2,3,4,5),
                },
            ],
            'SpaceAfter': '2cm',
            },
            {
            'Type': 'InputOutputTable',
            'Template': 'Graph.html',
            'ParameterSetVariants': [
                {'question': 'Create the input/output table for the graph below', 'x': (-5,-3,-1,1), 'y': (4, 2, 0, -2), 'variables': ['x','y']},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTable',
            'Template': 'Graph.html',
            'ParameterSetVariants': [
                {'question': 'Create the input/output table for the graph below', 'n': 4, 'seed': 24, 'variables': ['x','y']},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTable',
            'Template': 'MappingDiagram.html',
            'ParameterSetVariants': [
                {'question': 'Create the input/output table for the mapping diagram below', 'n': 4, 'seed': 25, 'variables': ['x','y']},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'MC',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'Is the relation represented below a function?<br/><img src="/mapping_diagram?x=2&x=3&x=4&y=1&y=1&y=2"/>',
                    'Choices': [('a', 'Function'),('b','Not a function')],
                    'CorrectAnswer': 'a'
                    },
                {'question': 'Does the set of coordinate pairs represent a function?<br/>$\{(-1,-1),(0,0),(1,1),(2,4),(3,9)\}$',
                    'Choices': [('a', 'Function'),('b','Not a function')],
                    'CorrectAnswer': 'a'
                    },
                {'question': 'Does the set of coordinate pairs represent a function?<br/>$\{(-1,2),(0,0),(1,2),(1,3)\}$',
                    'Choices': [('a', 'Function'),('b','Not a function')],
                    'CorrectAnswer': 'b'
                    },
                {'question': 'Is the relation represented below a function?<br/><table class="iotable"><tr><th>x</th><th>y</th></tr><tr><td>-2</td><td>3</td></tr> <tr><td>-2</td><td>3</td></tr> <tr><td>-1</td><td>2</td></tr> <tr><td>0</td><td>1</td></tr></table>',
                    'Choices': [('a', 'Function'),('b','Not a function')],
                    'CorrectAnswer': 'a'
                    },
                {'question': 'Is the relation represented below a function?<br/><table class="iotable"><tr><th>x</th><th>y</th></tr><td>1</td><td>0</td></tr> <tr><td>1</td><td>2</td></tr> <tr><td>2</td><td>2</td></tr> <tr><td>3</td><td>2</td></tr></table>',
                    'Choices': [('a', 'Function'),('b','Not a function')],
                    'CorrectAnswer': 'b'
                    },
                {'question': 'Is the relation represented below a function?<br/><img src="/scatterplot?x=-2&x=0&x=1&x=3&x=4&y=2&y=-3&y=-1&y=1&y=2"/>',
                    'Choices': [('a', 'Function'),('b','Not a function')],
                    'CorrectAnswer': 'a'
                    },
                {'question': 'Is the relation represented below a function?<br/><img src="/scatterplot?x=-2&x=-2&x=0&x=0&x=1&x=3&y=4&y=2&y=2&y=0&y=-2&y=-4"/>',
                    'Choices': [('a', 'Function'),('b','Not a function')],
                    'CorrectAnswer': 'b'
                    },
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'GenericEquality',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'If $f(x) = x+10$, find $f(2)$.','CorrectAnswer': '12'},
                {'question': 'If $f(x) = 2x+3$, find $f(7)$.','CorrectAnswer': '17'},
                {'question': 'If $g(x) = 2x^2+1$, find $g(3)$.','CorrectAnswer': '19'},
                {'question': 'If $h(x) = (x-5)^2+1$, find $h(-3)$.','CorrectAnswer': '65'},
                ],
            'SpaceAfter': '4cm',
            },
        ]
    },
    'FunctionNotationTarsia': {
        'ProvideImmediateFeedback': True,
        'Questions':
        [
            {
            'Type': 'Tarsia',
            'Template': 'SortableTarsiaWithInput.html',
            'ParameterSetVariants': [
                {
                    #'CorrectAnswer': [0,1,2,3,4,5,6,7,8,9,10,11],
                    #'shuffle': [7,1,3,4,6,2,5,9,11,10,8,0],
                    #'cards': ['<img src="/static/deck1/card0.png"/>','<img src="/static/deck1/card1.png"/>', '<img src="/static/deck1/card2.png"/>', '<img src="/static/deck1/card3.png"/>', '<img src="/static/deck1/card4.png"/>', '<img src="/static/deck1/card5.png"/>', '<img src="/static/deck1/card6.png"/>', '<img src="/static/deck1/card7.png"/>', '<img src="/static/deck1/card8.png"/>', '<img src="/static/deck1/card9.png"/>', '<img src="/static/deck1/card10.png"/>', '<img src="/static/deck1/card11.png"/>']
                    'shuffle': [7,1,3,2,5,4,6,0],
                    'cards': ['<img src="/static/deck3/card0.png"/>','<img src="/static/deck3/card1.png"/>', '<img src="/static/deck3/card2.png"/>', '<img src="/static/deck3/card3.png"/>', '<img src="/static/deck3/card4.png"/>', '<img src="/static/deck3/card5.png"/>', '<img src="/static/deck3/card6.png"/>', '<img src="/static/deck3/card7.png"/>']
                    }
                ],
            'SpaceAfter': '4cm',
            },
        ]
    },
    'RepresentRelations': {
        'ProvideImmediateFeedback': True,
        'Questions':
        [
            {
            'Type': 'InputOutputTable',
            'Template': 'Graph.html',
            'ParameterSetVariants': [
                {'question': 'Create the input/output table for the graph below', 'n': 5, 'seed': 5, 'variables': ['x','y']},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTable',
            'Template': 'MappingDiagram.html',
            'ParameterSetVariants': [
                {'question': 'Create the input/output table for the mapping diagram below', 'n': 5, 'seed': 6, 'variables': ['x','y']},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'MCMappingDiagram',
            'Template': 'Graph.html',
            'ParameterSetVariants': [
                {'question': 'Choose the mapping diagram of the relation shown in the graph.'
                    ,'n': 5, 'seed': 0,
                    'Choices': [('a', {'seed': 0, 'n': 5}), ('b', {'seed': 1, 'n': 5}), ('c', {'seed': 2, 'n': 5}), ('d', {'seed': 3, 'n': 5})],
                    'CorrectAnswer': 'a'
                    },
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTable',
            'Template': 'Graph.html',
            'ParameterSetVariants': [
                {'question': 'Create the input/output table for the graph below', 'n': 5, 'seed': 7, 'variables': ['x','y']},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'InputOutputTable',
            'Template': 'MappingDiagram.html',
            'ParameterSetVariants': [
                {'question': 'Create the input/output table for the mapping diagram below', 'n': 5, 'seed': 8, 'variables': ['x','y']},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'MCGraph',
            'Template': 'MappingDiagram.html',
            'ParameterSetVariants': [
                {'question': 'Choose the graph of the relation shown in the mapping diagram.', 'n': 5, 'seed': 9,
                    'Choices': [('a', {'seed': 10, 'n': 5}), ('b', {'seed': 11, 'n': 5}), ('c', {'seed': 12, 'n': 5}), ('d', {'seed': 9, 'n': 5})],
                    'CorrectAnswer': 'd'
                    },
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'GenericEquality',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'If $f(x) = x+5$, find $f(-5)$.','CorrectAnswer': '0'},
                {'question': 'If $f(x) = x^2+5$, find $f(-5)$.','CorrectAnswer': '30'},
                {'question': 'If $f(x) = 2(x-5)$, find $f(-5)$.','CorrectAnswer': '-20'},
                {'question': 'If $f(x) = 2(x-5)^2-3$, find $f(-2)$.','CorrectAnswer': '95'},
                ],
            'SpaceAfter': '4cm',
            },
        ]
    },
    'EvaluateFunctions': {
        'ProvideImmediateFeedback': True,
        'Questions':
        [
            {
            'Type': 'GenericEquality',
            'Template': 'Question.html',
            'ParameterSetVariants': [
                {'question': 'Evaluate the function $f(x) = x+5$ for $x=3$.','CorrectAnswer': '8'},
                {'question': 'Evaluate the function $f(x) = 4x+2$ for $x=7$.','CorrectAnswer': '30'},
                {'question': 'Evaluate the function $f(x) = 5x-7$ for $x=0$.','CorrectAnswer': '-7'},
                {'question': 'Evaluate the function $f(x) = 5(x-7)$ for $x=10$.','CorrectAnswer': '15'},
                {'question': 'Evaluate the function $f(x) = 5(x-7)^2$ for $x=10$.','CorrectAnswer': '45'},
                {'question': 'Evaluate the function $f(x) = 5x^2-7$ for $x=10$.','CorrectAnswer': '493'},
                {'question': 'Evaluate the function $f(x) = x^2-2x+1$ for $x=3$.','CorrectAnswer': '4'},
                ],
            'SpaceAfter': '4cm',
            },
        ]
    },
    'WhatIsAFunction': {
        'ProvideImmediateFeedback': False,
        'Questions':
        [
            {
            'Type': 'OpenResponse',
            'Template': 'FunctionBuilder.html',
            'ParameterSetVariants': [
                {'image': '/static/WhatIsAFunction1.png',
                    'question': 'Explain how you labeled the parts below.',},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'OpenResponse',
            'Template': 'OpenResponse.html',
            'ParameterSetVariants': [
                {'image': '/static/WhatIsAFunction1.png',
                   'question': 'Share your labels with your partner. Describe the similarities below:',},
                {'image': '/static/WhatIsAFunction1.png',
                    'question': "The blue 'builder' in the middle is a function. Describe what a function is using the labels you've agreed on as a class:",},
                ],
            'SpaceAfter': '4cm',
            },
            {
            'Type': 'OpenResponse',
            'Template': 'FunctionBuilder.html',
            'ParameterSetVariants': [
                {'image': '/static/WhatIsAFunction4a.png',
                    'question': 'Draw your answers on a separate sheet of paper, or describe what each output will look like below.',},
                {'image': '/static/WhatIsAFunction4b.png',
                    'question': '',},
                ],
            'SpaceAfter': '4cm',
            }
        ]
    },
    'WODBFunctions': {
        'ProvideImmediateFeedback': False,
        'Questions':
        [
            {
            'Type': 'OpenResponse',
            'Template': 'OpenResponse.html',
            'ParameterSetVariants': [
                {'image': '/static/WODBFunctions1.png',
                    'question': 'Which one does not belong. Be sure to justify your answers using appropriate mathematical vocabulary.',},
                {'image': '/static/WODBFunctions2.png',
                    'question': 'Which one does not belong. Be sure to justify your answers using appropriate mathematical vocabulary.',}
                ],
            'SpaceAfter': '4cm',
            }
        ]
    },
    'CoordinatePairs': {
        'ProvideImmediateFeedback': True,
        'Questions': [
        {
            'Type': 'SetOfCoordinatePairs',
            'Template': 'SetOfCoordinatePairs.html',
            'ParameterSetVariants': [
                {'image': None,
                    #'objects': [('star', (-7,-8))],
                    'question': 'Enter the set of coordinate pairs: $\{(-2,3),(4,0),(5,5)\}$. (You are entering exactly what is written, including all braces, parentheses, and commas).',
                    'set_of_coordinate_pairs': {(-2,3),(4,0),(5,5)},
                    },
                {'image': '/static/GraphOfPoints.png',
                    #'objects': [('star', (-7,-8))],
                    'question': 'Enter the set of coordinate pairs a-e in the graph',
                    'set_of_coordinate_pairs': {(-6,4),(7,6),(-8,-2),(4,-7),(5,0)},
                    },
                {'image': '/static/MappingDiagram.png',
                    #'objects': [('star', (-7,-8))],
                    'question': 'Enter the set of coordinate pairs that represents in the mapping diagram.',
                    'set_of_coordinate_pairs': {(-4,4),(-2,2),(0,0),(2,2),(4,4)},
                    }
                 ],
#            'Choices': [('a', '![UpUp](/static/ArrowDiagrams/ArrowDiagram-1-1a.png)'),('b', '![UpDown](/static/ArrowDiagrams/ArrowDiagram-1-1b.png)'), ('c', '![DownUp](/static/ArrowDiagrams/ArrowDiagram-1-1c.png)'), ('d', '![DownDown](/static/ArrowDiagrams/ArrowDiagram-1-1d.png)')],
            'SpaceAfter': '2cm',
            },
        ]
        },
    'SolvingEquationsTest': {
        'ProvideImmediateFeedback': False,
        'Questions': [
        {
            #'Type': 'SolveEquation',
            'Type': 'Matching',
            'Template': 'Matching.html',
            'ParameterSetVariants': [
                {'prompts': ['Two quantities whose sum is 0', 'A statement that two quantities are the same.', 'A part of a sum that is separated from other parts by addition', 'A part of a product that is separated from other parts by multiplication', 'A letter that represents an unspecified quantity', 'Two quantities whose product is 1', 'A quantity that is represented by the number 1','','',''], 'answers': {'A': 'Equation', 'B': 'Factor', 'C': 'Term', 'D': 'Unit', 'E': 'Variable', 'F':'Reciprocal pair', 'G': 'Zero pair','H':'Constant','I':'Coefficient'}, 'CorrectAnswers': ['G','A','C','B','E','F','D','E','H','I']}, 
                ],
            'SpaceAfter': '2cm',
            },
        {
            #'Type': 'SolveEquation',
            'Type': 'GenericEquality',
            'Template': 'SolveEquation.html',
            'ParameterSetVariants': [
                {'equation': 'x+6=19', 'CorrectAnswer': '13'}, 
                {'equation': '83+y=57','CorrectAnswer': '-26'},
                {'equation': '6x+8=32','CorrectAnswer': '4'},
                {'equation': '65=5x-10','CorrectAnswer': '15'},
                {'equation': '2(y+7)=49','CorrectAnswer': '35/2'},
                {'equation': '81=4h+5h-9','CorrectAnswer': '10'},
                ],
            'SpaceAfter': '4.5cm',
            },
        {
            #'Type': 'SolveEquation',
            #'Type': 'Numerical',
            'Type': 'GenericEquality',
            'Template': 'SolveEquation.html',
            'ParameterSetVariants': [
                {'equation': '8n-9=2n+3','CorrectAnswer': '2'},
                {'equation': 'x-42=98-9x','CorrectAnswer': '14'},
                ],
            'SpaceAfter': '4.5cm',
            },
        {
            #'Type': 'SolveEquation',
            'Type': 'GenericEquality',
            'Template': 'SolveEquation.html',
            'ParameterSetVariants': [
                {'equation': '3(x+4)=3x+11','CorrectAnswer': '{}'},
                {'equation': '|x-8|=3','equation_latex': '|x-8|=3', 'CorrectAnswer': '{5,11}'},
                ],
            'SpaceAfter': '4.5cm',
            },
        {
            #'Type': 'SolveEquation',
            #'Type': 'Numerical',
            'Type': 'GenericEquality',
            'Template': 'SolveEquation.html',
            'ParameterSetVariants': [
                {'equation': '(n-10)/12 = 8/3', 'equation': r'\frac{n-10}{12} = \frac{8}{3}','CorrectAnswer': '42'},
                {'equation': '4/6=8/x', 'equation': r'\frac{4}{6} = \frac{8}{x}','CorrectAnswer': '12'},
                ],
            'SpaceAfter': '5cm',
            },
        {
            'Type': 'RubricScore',
            'Template': 'Empty.html',
            'ParameterSetVariants': [{}],
            'Choices': [('0', 'None of the following criteria are demonstrated.'), ('1','I recognized that the solution was not correct.'), ('2','I demonstrated a correct way to solve the equation.'), ('3','I described a correct way to solve the equation using mathematical vocabulary.')],
            'Question': 'Explaining concepts',
            },
        {
            'Type': 'RubricScore',
            'Template': 'Empty.html',
            'ParameterSetVariants': [{}],
            'Choices': [('0', 'I did not communicate my reasoning'), ('1','I presented my reasoning about half of the time'), ('2','I presented my reasoning for almost every problem, but some details were missing'), ('3','I presented a detailed argument, including all steps needed to reach all of my conclusions')],
            'Question': 'Communicating mathematical reasoning',
            },
        {
            'Type': 'RubricScore',
            'Template': 'Empty.html',
            'ParameterSetVariants': [{}],
            'Choices': [('0', 'I did not bring a note sheet containing solution strategies to the test'), ('1','I created a note sheet containing the basic solution strategies presented in class'), ('2','I created a note sheet containing the basic solution strategies presented in class, along with examples of each'), ('3','I created a note sheet containing the more advanced solution strategies presented in class'), ('4','I created a note sheet containing the more advanced solution strategies presented in class, along with examples'), ('5','I created a note sheet containing all of the solution strategies'), ('6','I created a note sheet containing all of the solution strategies, along with examples')],
            'Question': 'Creating a note sheet',
            },
        {
            'Type': 'OpenResponse',
            'Template': 'OpenResponse.html',
            'ParameterSetVariants': [
                {'image': None,
                    'question': "I demonstrated a full understanding of solution strategies on the following problems, but I made a computational error.",},
                ],
            'SpaceAfter': '4cm',
            },
        {
            'Type': 'OpenResponse',
            'Template': 'OpenResponse.html',
            'ParameterSetVariants': [
                {'image': None,
                    'question': "Notes about student work",},
                ],
            'SpaceAfter': '4cm',
            },
        {
            'Type': 'SelectMultiple',
            'Template': 'Empty.html',
            'ParameterSetVariants': [
                {'image': None,
                    'choices': [('a', 'Using zero pairs and reciprocal pairs to solve equations'), ('b', 'Eliminating variable terms when solving equations'), ('c', 'The distributive property'), ('d', 'Understanding like terms'), ('e', 'Solving equations involving absolute value'), ('f', 'Solving equations with variables on both sides'), ('g', 'Combining like terms when solving equations'), ('h', 'Solving proportions and other equations with quotients'), ('i', 'Combining like terms when solving equations and a term has no visible coefficient'), ('j', 'Distributing before trying to eliminate a term that is inside parentheses.'), ('k', 'Performing the same operation to both sides of an equation'), ('l', 'Eliminating a zero pair and bringing down the rest of the terms'), ('m', 'Communicating about the solution set when an equation has no solution.'), ('n', 'Writing clearly so that your equations are legible'), ('o', 'Knowing when an equation has a solution or no solution'), ('p', 'Consistently distinguishing between unlike terms when solve equations'), ('q', 'Understanding what variables are and what an equation means'), ('r', 'Correctly accounting for the signs of terms when using zero pairs to solving equations'), ('s', 'Understand what it means to solve an equation'), ('t','Figure out solutions to equations by refining an initial guess'),('u','Distributing when solving equations with variables in parentheses'),('v','Using a reciprocal pair when eliminating a coefficient'),('w','Forming zero pairs and reciprocal pairs')],
                    'question': "The main learning goals that you need to work on are ",
                    'CorrectAnswer': None,
                    },
                ],
            'SpaceAfter': '4cm',
            },
        ],
        },
    'BalancingCandiesRubric': {
        'ProvideImmediateFeedback': False,
        'Questions': [
        {
            'Type': 'MC',
            'Template': 'Empty.html',
            'ParameterSetVariants': [{}],
            'Choices': [('0', 'None of the following criteria are demonstrated.'), ('1','Some steps used to solve the equation are valid.'), ('2','The equation represents a balance. All steps of solution are shown in a logical order.'), ('3','The equation represents a balance. All steps needed to solve the equation are shown in a logical order, and the properties of algebra used are indicated.')],
            'Question': 'Communicating mathematical reasoning',
            },
        {
            'Type': 'MC',
            'Template': 'Empty.html',
            'ParameterSetVariants': [{}],
            'Choices': [('0', 'None of the following criteria are demonstrated.'), ('1','Examples are provided for some key concepts, or some of the key concepts are not accurately labeled.'), ('2','Examples are provided for 10 key concepts. All examples are accurately labeled.'), ('3','Examples are provided for all 13 key concepts. All examples of the key concepts are accurately labeled. A description of each concept is written in your own words.')],
            'Question': 'Explaining concepts',
            },
        {
            'Type': 'MC',
            'Template': 'Empty.html',
            'ParameterSetVariants': [{}],
            'Choices': [('0', 'None of the following criteria are demonstrated.'), ('1','Writing is partially organize, or markings and color leave uncertainty about examples and characteristics of key concepts.'), ('2','Writing is organized and easy to read. Markings and color clearly indicate examples and characteristics of key concepts.'), ('3','Writing is organized and easy to read. Markings and color clearly indicate examples and characteristics of key concepts. You produced an original video showing balanced weights.')],
            'Question': 'Presentation',
            },
        ]
    },
    'Nov8Examples': {
        'ProvideImmediateFeedback': True,
        'Questions':
        [
            {
            'Type': 'SolveEquationGuided',
            'Template': 'SolveEquationGuided.html',
            'ParameterSetVariants': [
                {'equation': '4-2x=16', 'variables': ['x']},
                # You and Review (2 min + 2 min)
                {'equation': '2(s-10)+s=13', 'variables': ['s']},
                {'equation': '7(n-1)=5-(n+8)', 'variables': ['n']},
                # We (2 min)
                ],
            'SpaceAfter': '4cm',
            }
        ]
    },
    'ClassworkNov8A': {
        'ProvideImmediateFeedback': True,
        'Questions':
        [
            {
            'Type': 'SolveEquationGuided',
            'Template': 'SolveEquationGuided.html',
            'ParameterSetVariants': [
                {'equation': '2x-4=6', 'variables': ['x']},
                # You and Review (2 min + 2 min)
                {'equation': '10-2s=18', 'variables': ['s']},
                {'equation': '7(n-1)=14', 'variables': ['n']},
                {'equation': '6-4t=30', 'variables': ['t']},
                {'equation': '6(5m-3)=42', 'variables': ['m']},
                {'equation': '2(6-2y)=-4', 'variables': ['y']},
                # We (2 min)
                ],
            'SpaceAfter': '4cm',
            }
        ]
    },
    'ClassworkNov8B': {
        'ProvideImmediateFeedback': True,
        'Questions':
        [
            {
            'Type': 'SolveEquationGuided',
            'Template': 'SolveEquationGuided.html',
            'ParameterSetVariants': [
                {'equation': '2(x-4)+5x=6', 'variables': ['x']},
                # You and Review (2 min + 2 min)
                {'equation': '10-2s+5s=38', 'variables': ['s']},
                {'equation': '7(n-1)-n=12', 'variables': ['n']},
                {'equation': '6(5m-3)-8m=4', 'variables': ['m']},
                {'equation': '6t-6+2t=30', 'variables': ['t']},
                {'equation': '-2y-2(6-2y)=4', 'variables': ['y']},
                # We (2 min)
                ],
            'SpaceAfter': '4cm',
            }
        ]
    },
    'ClassworkOct30B': {
        'ProvideImmediateFeedback': True,
        'Questions':
        [
            {
            'Type': 'SolveEquationGuided',
            'Template': 'SolveEquationGuided.html',
            'ParameterSetVariants': [
                {'equation': '1/2(4a-8)=-2(2+a)', 'equation_latex': r'\frac{1}{2}(4a-8)=-2(2+a)', 'variables': ['a']},
                {'equation': '4(2x-1)=4x+6', 'variables': ['x']},
                # You and Review (2 min + 2 min)
                {'equation': '8s-10=3(6-2s)', 'variables': ['s']},
                {'equation': '6(5m-3)=(1/3)*(24m+12)', 'equation_latex': r'6(5m-3)=\frac{1}{3}(24m+12)', 'variables': ['m']},
                {'equation': '-2y-4=2(6-2y)', 'equation_latex': r'-2y-4=2(6-2y)', 'variables': ['y']},
                {'equation': '3(2t-2)-26=2(2-t)', 'variables': ['t']},
                # We (2 min)
                {'equation': '7(n-1)=-2(3+n)', 'equation_latex': '7(n-1)=-2(3+n)', 'variables': ['n']},
                ],
            'SpaceAfter': '4cm',
            }
        ]
    },
    'ClassworkOct30': {
        'ProvideImmediateFeedback': True,
        'Questions':
        [
            {
            'Type': 'SolveEquationGuided',
            'Template': 'SolveEquationGuided.html',
            'ParameterSetVariants': [
                {'equation': '4(2x-1)=4x+6', 'variables': ['x']},
                # You and Review (2 min + 2 min)
                {'equation': '8s-10=3(6-2s)', 'variables': ['s']},
                {'equation': '1/2(4a-8)=-2(2+a)', 'equation_latex': r'\frac{1}{2}(4a-8)=-2(2+a)', 'variables': ['a']},
                {'equation': '6(5m-3)=(1/3)*(24m+12)', 'equation_latex': r'6(5m-3)=\frac{1}{3}(24m+12)', 'variables': ['m']},
                {'equation': '-2y-4=2(6-2y)', 'equation_latex': r'-2y-4=2(6-2y)', 'variables': ['y']},
                {'equation': '3(2t-2)-26=2(2-t)', 'variables': ['t']},
                # We (2 min)
                {'equation': '7(n-1)=-2(3+n)', 'equation_latex': '7(n-1)=-2(3+n)', 'variables': ['n']},
                ],
            'SpaceAfter': '4cm',
            }
        ]
    },
    'DifferenceBetweenZeroPairAndReciprocalPair': {
        'ProvideImmediateFeedback': False,
        'Questions':
        [
            {
            'Type': 'OpenResponse',
            'Template': 'DifferenceBetweenZeroPairAndReciprocalPair.html',
            'ParameterSetVariants': [{}],
            }
        ]
    },
    'BalancingCandy': {
        'ProvideImmediateFeedback': True,
        'Questions': [
        {
            'Type': 'SetUpAndSolveEquationGuided',
            'Template': 'SetUpAndSolveEquationGuided.html',
            'ParameterSetVariants': [
                {'question': 'How many skittles weight the same as one starburst?', 'quantities': ['weight of a starburst', 'weight of a skittle'], 'variables': ['t','k'], 'equation': r'6(t+2k)=40k', 'act1_youtube_video_id': 'hKbVTk2Z-kY'},
                {'question': 'How many skittles are in one bag?', 'quantities': ['weight of a bag of skittles', 'weight of one skittle'], 'variables': ['s','t'], 'equation': r'3s+2t=47t', 'act1_youtube_video_id': 'tAaSMnc7ovc'},
                {'question': 'How many skittles are in each of the silver bottles?', 'quantities': ['weight of an empty bottle', 'weight of a skittle', 'weight of a starburst', 'number of skittles in the silver bottle'], 'variables': ['b', 'k', 't', 'x'], 'equation': r'2b+x*k+3t=2b+21k', 'act1_youtube_video_id': 'ySPeCgh31qc'},
                ]
            }
        ]
    },
    'HomeworkOct29': {
        'ProvideImmediateFeedback': True,
        'Questions':
        [
            {
            'Type': 'SolveEquationGuided',
            'Template': 'SolveEquationGuided.html',
            'ParameterSetVariants': [
                # Homework
                # Page 100 #15-21
                #{'equation': '(5v-4)/10 = 4/5', 'variables': ['v']}, #15
                {'equation': '8=4(r+4)', 'variables': ['r']}, #16
                {'equation': '6(n+5)=66', 'variables': ['n']}, #17
                {'equation': '5(g+8)-7=103', 'variables': ['g']},
                {'equation': '12-4/5(x+15)=4', 'equation_latex': r'12-\frac{4}{5}(x+15)=4', 'variables': ['g']},
                {'equation': '3(3m-2)=2(3m+3)', 'variables': ['m']},
                {'equation': '6(3a+1)-30=3(2a-4)', 'variables': ['a']},
                ],
            'SpaceAfter': '4cm',
            }
        ]
    },
    'ClassworkOct29Advanced': {
        'ProvideImmediateFeedback': True,
        'Questions':
        [
            {
            'Type': 'SolveEquationGuided',
            'Template': 'SolveEquationGuided.html',
            'ParameterSetVariants': [
                # Review
                # You and Review (2 min + 2 min)
                #{'equation': '2(s+9)-s=30', 'variables': ['s']},
                # We (2 min)
                #{'equation': '3b-(b+18)=2', 'variables': ['b']},
                # Me (2 min) Follow along and enter into Schoology
                {'equation': '3m-1+2(m-2)=5', 'variables': ['m']},
                # Lesson (2 min)
                # Example on page 97 (2 min)
                {'equation': '2+5k=3k-6', 'variables': ['k']},
                # You and Review (2 min + 2 min)
                {'equation': '3w+2=7w', 'variables': ['w']},
                # We (2 min)
                {'equation': '5a+2=6-7a', 'variables': ['a']},
                {'equation': 'x/2+1=1/4x-6', 'variables': ['x']},
                #{'equation': '1.3c=3.3c+2.8', 'variables': ['c']},
                # Example on page 98 (Solve an equation with grouping symbols)
                {'equation': '6(5m-3)=(1/3)*(24m+12)', 'equation_latex': r'6(5m-3)=\frac{1}{3}(24m+12)', 'variables': ['m']},
                #{'equation': '3(2t-2)-26=2(2-t)', 'variables': ['t']},
                #{'equation': '4(2x-1)=4x+6', 'variables': ['x']},
                # You and Review (2 min + 2 min)
                {'equation': '8s-10=3(6-2s)', 'variables': ['s']},
                # We (2 min)
                {'equation': '7(n-1)=-2(3+n)', 'variables': ['n']},
                ],
            'SpaceAfter': '4cm',
            }
        ]
    },
    'ClassworkOct29': {
        'ProvideImmediateFeedback': True,
        'Questions':
        [
            {
            'Type': 'SolveEquationGuided',
            'Template': 'SolveEquationGuided.html',
            'ParameterSetVariants': [
                #{'equation': '5(2a+2)-3(3a+5)=10', 'equation_latex': r'5(2a+2)-3(3a+5)=10', 'variables': ['a']},
                {'equation': '2(s+9)-s=30', 'variables': ['s']},
                # We (2 min)
                {'equation': '3b-(b+18)=2', 'variables': ['b']},
                # Me (2 min) Follow along and enter into Schoology
                {'equation': '3m-1+2(m-2)=5', 'variables': ['m']},
                {'equation': '-3(2t-2)+2(2-t)=26', 'equation_latex': r'-3(2t-2)+2(2-t)=26', 'variables': ['t']},
                {'equation': '4(2x-1)-4x=6', 'variables': ['x']},
                # Homework
                # Page 100 #15-19
#                {'equation': '(5v-4)/10 = 4/5', 'variables': ['v']},
#                {'equation': '8=4(r+4)', 'variables': ['r']}, #16
#                {'equation': '6(n+5)=66', 'variables': ['n']}, #17
#                {'equation': '5(g+8)-7=103', 'variables': ['g']},
#                {'equation': '12-4/5(x+15)=4', 'equation': r'12-\frac{4}{5}(x+15)=4', 'variables': ['x']},
                ],
            'SpaceAfter': '4cm',
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


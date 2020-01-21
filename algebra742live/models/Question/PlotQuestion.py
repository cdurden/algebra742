from . import Question
class PlotQuestion(Question):
    def scripts(self):
        #return({'canvasjs': "https://canvasjs.com/assets/script/canvasjs.min.js", 'plot': '/static/js/plot.js', 'plotly': 'https://cdn.plot.ly/plotly-latest.min.js', 'plotly_ex1': '/static/js/plotly_ex1.js'})
        return(["https://canvasjs.com/assets/script/canvasjs.min.js", '/static/js/plot.js', 'https://cdn.plot.ly/plotly-latest.min.js', '/static/js/plotly_ex1.js'])


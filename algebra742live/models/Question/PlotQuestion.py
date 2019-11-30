class PlotQuestion(Question):
    def scripts(self):
        return({'canvasjs': "https://canvasjs.com/assets/script/canvasjs.min.js", 'plot': '/static/js/plot.js', 'plotly': 'https://cdn.plot.ly/plotly-latest.min.js'})


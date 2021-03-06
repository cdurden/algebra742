window.onload = function () {
var myPlot = document.getElementById('myDiv'),
    d3 = Plotly.d3,
    N = 16,
    x = d3.range(N),
    y = d3.range(N).map( d3.random.normal() ),
    data = [ { x:x, y:y, type:'scatter',
            mode:'markers', marker:{size:1} } ],
    layout = {
        hovermode:'closest',
        title:'Click on Points'
     };

Plotly.newPlot('myDiv', data, layout, {showSendToCloud: true});

myPlot.on('plotly_click', function(data){
    var pts = '';
    for(var i=0; i < data.points.length; i++){
        pts = 'x = '+data.points[i].x +'\ny = '+
            data.points[i].y.toPrecision(4) + '\n\n';
    }
    alert('Closest point clicked:\n\n'+pts);
});
}

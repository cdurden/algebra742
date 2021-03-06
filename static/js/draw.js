/* © 2009 ROBO Design
 * http://www.robodesign.ro
 */

// Keep everything in anonymous function, called on window load.
if(window.addEventListener) {
window.addEventListener('load', function () {
  var canvas, context, canvaso, contexto, canvas_container;

  // The active tool instance.
  var tool;
  var tool_default = 'pencil';
  var lastX, lastY;

  function init () {
    canvas_container = document.getElementById('canvas_container');
    new ResizeSensor(canvas_container, function(){ 
      //canvas.width  = canvaso.width;
      //canvas.height = canvaso.height;
      var rect = canvas_container.getBoundingClientRect();
		  context.drawImage(canvaso, 0, 0, canvaso.width, canvaso.height);
      canvaso.width  = rect.width-20;
      canvaso.height = rect.height-20;
      contexto = canvaso.getContext('2d');
		  contexto.drawImage(canvas, 0, 0, canvas.width, canvas.height);
      canvas.width  = rect.width-20;
      canvas.height = rect.height-20;
      context = canvas.getContext('2d');
		  context.clearRect(0, 0, canvas.width, canvas.height);
    });
    // Find the canvas element.
    canvaso = document.getElementById('imageView');
    if (!canvaso) {
      alert('Error: I cannot find the canvas element!');
      return;
    }
    var rect = canvas_container.getBoundingClientRect();
    canvaso.width  = rect.width-20;
    canvaso.height = rect.height-20;

    if (!canvaso.getContext) {
      alert('Error: no canvas.getContext!');
      return;
    }

    // Get the 2D canvas context.
    contexto = canvaso.getContext('2d');
    if (!contexto) {
      alert('Error: failed to getContext!');
      return;
    }

    // Add the temporary canvas.
    var container = canvaso.parentNode;
    canvas = document.createElement('canvas');
    if (!canvas) {
      alert('Error: I cannot create a new canvas element!');
      return;
    }

    canvas.id     = 'imageTemp';
    canvas.width  = canvaso.width;
    canvas.height = canvaso.height;
    //canvas.class = 'imageCanvas';
    container.appendChild(canvas);

    context = canvas.getContext('2d');

    // Get the tool select input.
    var tool_select = document.getElementById('dtool');
    if (!tool_select) {
      alert('Error: failed to get the dtool element!');
      return;
    }
    tool_select.addEventListener('change', ev_tool_change, false);

    // Activate the default tool.
    if (tools[tool_default]) {
      tool = new tools[tool_default]();
      tool_select.value = tool_default;
    }

    // Attach the mousedown, mousemove and mouseup event listeners.
    canvas.addEventListener('mousedown', ev_canvas, { passive: false});
    canvas.addEventListener('mousemove', ev_canvas, { passive: false });
    canvas.addEventListener('mouseup',   ev_canvas, { passive: false });
    canvas.addEventListener('touchstart', ev_canvas, { passive: false });
    canvas.addEventListener('touchmove', ev_canvas, { passive: false });
    canvas.addEventListener('touchend',   ev_canvas, { passive: false });
    canvaso.addEventListener('mousedown', function(ev) {ev.preventDefault()}, { passive: false });
    canvaso.addEventListener('mousemove', function(ev) {ev.preventDefault()}, { passive: false });
    canvaso.addEventListener('mouseup', function(ev) {ev.preventDefault()}, { passive: false });
    canvaso.addEventListener('touchstart', function(ev) {ev.preventDefault()}, { passive: false });
    canvaso.addEventListener('touchmove', function(ev) {ev.preventDefault()}, { passive: false });
    canvaso.addEventListener('touchend', function(ev) {ev.preventDefault()}, { passive: false });
    document.addEventListener("touchmove", function (ev) { if (ev.target == canvas) { ev_canvas(ev); return(false); } }, { passive: false });
    document.addEventListener("touchstart", function (ev) { if (ev.target == canvas) { ev_canvas(ev); return(false); } }, { passive: false });
    document.addEventListener("touchend", function (ev) { if (ev.target == canvas) { ev_canvas(ev); return(false); } }, { passive: false });

    updateImageData();
  }

  // The general-purpose event handler. This function just determines the mouse 
  // position relative to the canvas element.
  function ev_canvas (ev) {
    if (ev.layerX || ev.layerX == 0) { // Firefox
      ev._x = ev.layerX;
      ev._y = ev.layerY;
    } else if (ev.offsetX || ev.offsetX == 0) { // Opera
      ev._x = ev.offsetX;
      ev._y = ev.offsetY;
    } else if (ev.targetTouches && ev.targetTouches[0]) {
      ev.preventDefault();
      //var rect = ev.target.getBoundingClientRect();
      var rect = document.getElementById("imageView").getBoundingClientRect();
      ev._x = ev.targetTouches[0].clientX - rect.left;
      ev._y = ev.targetTouches[0].clientY - rect.top;
    } else if (ev.changedTouches && ev.changedTouches[0]) {
      ev.preventDefault();
      //var rect = ev.target.getBoundingClientRect();
      var rect = document.getElementById("imageView").getBoundingClientRect();
      ev._x = ev.changedTouches[0].clientX - rect.left;
      ev._y = ev.changedTouches[0].clientY - rect.top;
    }

    // Call the event handler of the tool.
    var func = tool[ev.type];
    if (func) {
      func(ev);
    }
    ev.preventDefault();
    return false;
  }

  // The event handler for any changes made to the tool selector.
  function ev_tool_change (ev) {
    if (tools[this.value]) {
      tool = new tools[this.value]();
    }
  }

  // This function draws the #imageTemp canvas on top of #imageView, after which 
  // #imageTemp is cleared. This function is called each time when the user 
  // completes a drawing operation.
  function img_update () {
		contexto.drawImage(canvas, 0, 0);
		context.clearRect(0, 0, canvas.width, canvas.height);
  }

  // This object holds the implementation of each drawing tool.
  var tools = {};

  // The drawing pencil.
  tools.pencil = function () {
    var tool = this;
    this.started = false;

    // This is called when you start holding down the mouse button.
    // This starts the pencil drawing.
    this.mousedown = function (ev) {
        context.strokeStyle = "#0000FF"; //rgba(0,0,0,1)";
        context.globalCompositeOperation="source-over";
        context.beginPath();
        context.moveTo(ev._x, ev._y);
        context.lineWidth = 1;
        tool.started = true;
    };

    // This function is called every time you move the mouse. Obviously, it only 
    // draws if the tool.started state is set to true (when you are holding down 
    // the mouse button).
    this.mousemove = function (ev) {
      if (tool.started) {
        context.lineTo(ev._x, ev._y);
        context.stroke();
      }
    };

    // This is called when you release the mouse button.
    this.mouseup = function (ev) {
      if (tool.started) {
        tool.mousemove(ev);
        tool.started = false;
        img_update();
      }
    };
    this.touchend = function (ev) {
      if (tool.started) {
        tool.touchmove(ev);
        tool.started = false;
        img_update();
      }
    };
    this.touchstart = this.mousedown;
    this.touchmove = this.mousemove;
  };
  // The eraser.
  tools.eraser = function () {
    var tool = this;
    this.started = false;

    // This is called when you start holding down the mouse button.
    // This starts the erasing.
    this.mousedown = function (ev) {
        context.strokeStyle = "#FFFFFF"; //rgba(0,0,0,1)";
        context.globalCompositeOperation="source-over";
        context.beginPath();
        context.moveTo(ev._x, ev._y);
        context.lineWidth = 10;
        /*context.beginPath();
        context.globalCompositeOperation="destination-out";
        context.lineWidth = 10;
        //context.strokeStyle = "rgba(0,0,0,1)";
        context.moveTo(ev._x, ev._y);
        */
        tool.started = true;
        lastX = ev._x;
        lastY = ev._y;
    };

    // This function is called every time you move the mouse. Obviously, it only 
    // draws if the tool.started state is set to true (when you are holding down 
    // the mouse button).
    this.mousemove = function (ev) {
      if (tool.started) {
        //context.globalCompositeOperation="destination-out";
        //context.strokeStyle = "rgba(1,1,1,1)";
        //context.moveTo(lastX, lastY);
        context.lineTo(ev._x, ev._y);
        //context.closePath();
        //context.lineJoin = context.lineCap = 'round';
        context.stroke();
        //lastX = ev._x;
        //lastY = ev._y;
        //context.arc(ev._x,ev._y,8,0,Math.PI*2,false);
        //context.fill();
      }
    };

    // This is called when you release the mouse button.
    this.mouseup = function (ev) {
      if (tool.started) {
        tool.mousemove(ev);
        tool.started = false;
        img_update();
      }
    };
    this.touchend = function (ev) {
      if (tool.started) {
        tool.touchmove(ev);
        tool.started = false;
        img_update();
      }
    };
    this.touchstart = this.mousedown;
    this.touchmove = this.mousemove;
  };


  // The rectangle tool.
  tools.rect = function () {
    var tool = this;
    this.started = false;

    this.mousedown = function (ev) {
      context.strokeStyle = "#0000FF"; //rgba(0,0,0,1)";
      tool.started = true;
      tool.x0 = ev._x;
      tool.y0 = ev._y;
    };

    this.mousemove = function (ev) {
      if (!tool.started) {
        return;
      }

      var x = Math.min(ev._x,  tool.x0),
          y = Math.min(ev._y,  tool.y0),
          w = Math.abs(ev._x - tool.x0),
          h = Math.abs(ev._y - tool.y0);

      context.clearRect(0, 0, canvas.width, canvas.height);

      if (!w || !h) {
        return;
      }

      context.strokeRect(x, y, w, h);
    };

    this.mouseup = function (ev) {
      if (tool.started) {
        tool.mousemove(ev);
        tool.started = false;
        img_update();
      }
    };
    this.touchend = function (ev) {
      if (tool.started) {
        tool.touchmove(ev);
        tool.started = false;
        img_update();
      }
    };
    this.touchstart = this.mousedown;
    this.touchmove = this.mousemove;
  };

  // The line tool.
  tools.line = function () {
    var tool = this;
    this.started = false;

    this.mousedown = function (ev) {
      context.strokeStyle = "#0000FF"; //rgba(0,0,0,1)";
      tool.started = true;
      tool.x0 = ev._x;
      tool.y0 = ev._y;
    };

    this.mousemove = function (ev) {
      if (!tool.started) {
        return;
      }

      context.clearRect(0, 0, canvas.width, canvas.height);
      context.beginPath();
      context.moveTo(tool.x0, tool.y0);
      context.lineTo(ev._x,   ev._y);
      context.stroke();
      context.closePath();
    };

    this.mouseup = function (ev) {
      if (tool.started) {
        tool.mousemove(ev);
        tool.started = false;
        img_update();
      }
    };
    this.touchend = function (ev) {
      if (tool.started) {
        tool.touchmove(ev);
        tool.started = false;
        img_update();
      }
    };
    this.touchstart = this.mousedown;
    this.touchmove = this.mousemove;
  };

  init();

}, false); }

// vim:set spell spl=en fo=wan1croql tw=80 ts=2 sw=2 sts=2 sta et ai cin fenc=utf-8 ff=unix:


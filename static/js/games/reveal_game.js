function injectLibFromStack(callback){
    if(libs.length > 0){
      
      //grab the next item on the stack
      var nextLib = libs.shift();
      var headTag = document.getElementsByTagName('head')[0];
      
      //create a script tag with this library
      var scriptTag = document.createElement('script');
      scriptTag.src = nextLib;
      
      //when successful, inject the next script
      scriptTag.onload = function(e){
        console.log("---> loaded: " + e.target.src);
        injectLibFromStack(callback);
      };    
      
      //append the script tag to the <head></head>
      headTag.appendChild(scriptTag);
      console.log("injecting: " + nextLib);
    }
    else return callback();
}

function loadScript(url, callback)
{
    // adding the script tag to the head as suggested before
   var head = document.getElementsByTagName('head')[0];
   var script = document.createElement('script');
   script.type = 'text/javascript';
   script.src = url;

   // then bind the event to the callback function 
   // there are several events for cross browser compatibility
   script.onreadystatechange = callback;
   script.onload = callback;

   // fire the loading
   head.appendChild(script);
}

function output(data) {
    //container = document.getElementById('question_'+data.graph+"_"+data.node);
    container = $('div.question[source="digraph_question:'+data.graph+":"+data.node+'"]');
    for (let field of data.question.marked_correct) {
      //$(container).find("input[name='"+field+"']").after('<i class="fas fa-check"></i>');
      $(container).find("input[name='"+field+"']").next("span.answer_marker").html('<i class="fas fa-check"></i>');
    }
    for (let field of data.question.marked_incorrect) {
      //$(container).find("input[name='"+field+"']").after('<i class="fas fa-times"></i>');
      $(container).find("input[name='"+field+"']").next("span.answer_marker").html('<i class="fas fa-times"></i>');
    }
    /*
    if (data.correct) {
      $(container).find('a.question_completed').attr('data-icon',"check");
      $(container).find('a.question_completed').html("Completed");
    } else {
      $(container).find('a.question_completed').attr('data-icon',"alert");
      $(container).find('a.question_completed').html("Incomplete");
    }
    */
}
function update_question_data(data) {
  //container = document.getElementById('digraph_question_'+data.graph+"_"+data.node);
  container = $('div.question[source="digraph_question:'+data.graph+":"+data.node+'"]');
  console.log(data);
  $(container).find('span[class="question_view"]').html(data.html); 
  form = $(container).find('form');
  $(form).append($(document.createElement('input')).attr('name','graph').attr('type','hidden').val(data.graph));
  $(form).append($(document.createElement('input')).attr('name','node').attr('type','hidden').val(data.node));
  //$(container).find('input[name="graph"]').val(data.graph);
  //$(container).find('input[name="node"]').val(data.node);
  $(container).find('input[type="text"]').after('<span class="answer_marker"></span>');
  $(form).submit(function (e) {
    socket.emit('form_submit', data=getFormData( $(this) ));
    e.preventDefault(); // block the traditional submission of the form.
  });
}
function update_snow_qm_task_data(data) {
  //container = document.getElementById('snow-qm_'+data.graph+"_"+data.task);
  container = $('div.snow-qm-task[source="snow-qm:'+data.collection+":"+data.task+'"]');
  console.log(data);
  console.log(container);
  $(container).find('span[class="question_view"]').html(data.html); 
  form = $(container).find('form');
  $(form).append($(document.createElement('input')).attr('name','collection').attr('type','hidden').val(data.collection));
  $(form).append($(document.createElement('input')).attr('name','task').attr('type','hidden').val(data.task));
  //$(container).find('input[name="collection"]').val(data.collection);
  //$(container).find('input[name="task"]').val(data.task);
  $(container).find('input[type="text"]').after('<span class="answer_marker"></span>');
  $(form).submit(function (e) {
    socket.emit('form_submit', data=getFormData( $(this) ));
    e.preventDefault(); // block the traditional submission of the form.
  });
}

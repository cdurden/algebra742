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
  $(container).find('input[name="graph"]').val(data.graph);
  $(container).find('input[name="node"]').val(data.node);
  $(container).find('input[type="text"]').after('<span class="answer_marker"></span>');
  $(container).find('form').submit(function (e) {
              socket.emit('form_submit', data=getFormData( $(this) ));
  });
}

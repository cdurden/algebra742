function output(data) {
    container = document.getElementById('question_'+data.graph+"_"+data.node);
    if (data.correct) {
      $(container).find('a[class="question_completed"]').attr('data-icon',"check");
      $(container).find('a[class="question_completed"]').html("Completed");
    } else {
      $(container).find('a[class="question_completed"]').attr('data-icon',"alert");
      $(container).find('a[class="question_completed"]').html("Incomplete");
    }
}
function update_game(data) {
    return
}

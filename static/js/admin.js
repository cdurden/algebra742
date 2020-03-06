function getFormData($form){
    var unindexed_array = $form.serializeArray();
    var indexed_array = {};

    $.map(unindexed_array, function(n, i){
        indexed_array[n['name']] = n['value'];
    });

    return indexed_array;
}
$(document).ready(function() {
    $('form').submit(function (e) {
        socket.emit('set_game', data=getFormData( $('form') ));
        e.preventDefault(); // block the traditional submission of the form.
    });
});

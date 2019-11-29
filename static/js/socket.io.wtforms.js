$(document).ready(function() {
    $('form').submit(function (e) {
        socket.emit('form_submit', data=JSON.stringify( $('form').serializeArray() ));
        e.preventDefault(); // block the traditional submission of the form.
    });
});

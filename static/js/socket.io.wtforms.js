$(document).ready(function() {
    $('form').submit(function (e) {
        socket.emit('form_submit', data=$('form').serialize());
        e.preventDefault(); // block the traditional submission of the form.
    });
});

$(function() {
    $('#button_doc').on('click', function(){
        if (document.getElementById('calendar').classList.contains('open')) {
            $('#calendar').toggleClass('open');
        }
        $('#documents').toggleClass('open');
    });
    $('#button_cal').on('click', function(){
        if (document.getElementById('documents').classList.contains('open')) {
            $('#documents').toggleClass('open');
        }
        $('#calendar').toggleClass('open');
    });
});
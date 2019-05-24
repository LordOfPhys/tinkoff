$(function() {
    $('#button_doc').on('click', function(){
        if (document.getElementById('calendar').classList.contains('open')) {
            $('#calendar').toggleClass('open');
        }
        if (document.getElementById('analys').classList.contains('open')) {
            $('#analys').toggleClass('open');
        }
        $('#documents').toggleClass('open');
    });
    $('#button_cal').on('click', function(){
        if (document.getElementById('documents').classList.contains('open')) {
            $('#documents').toggleClass('open');
        }
        if (document.getElementById('analys').classList.contains('open')) {
            $('#analys').toggleClass('open');
        }
        $('#calendar').toggleClass('open');
    });
    $('#button_analys').on('click', function(){
        if (document.getElementById('documents').classList.contains('open')) {
            $('#documents').toggleClass('open');
        }
        if (document.getElementById('calendar').classList.contains('open')) {
            $('#calendar').toggleClass('open');
        }
        $('#analys').toggleClass('open');
    });
});
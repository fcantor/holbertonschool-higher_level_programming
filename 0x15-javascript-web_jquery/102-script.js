// Script that fetches and prints how to say “Hello” depending of the language
$(document).ready(function () {
  let url = 'https://fourtonfish.com/hellosalut/?lang=';
  $('#btn_translate').click(function () {
    let language = $('#language_code').val();
    $.get(url + language, function (data) {
      $('#hello').append('<div>' + data.hello + '</div>');
    });
  });
});
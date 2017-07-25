/**
 * Created by vavadimir on 7/17/17.
 */
$(document).ready(function() {
    var form = $('#form_chat');
    var switcher = false;
    console.log(form);


    form.on('submit', function(e){
        e.preventDefault();
        var data = {};
        data.comm = $('#inputComment').val();
        var csrf_token = $('#form_chat [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        console.log('gggg');
        $.ajax({
             url: '../../chatbootstrap',
             type: 'POST',
             data: data,
             cache: true,
             success: function () {
                 console.log("OK");
                 $('#inputComment').val('');
                 getMessages();
             },
             error: function() {
                 console.log("ERROR");
             }
             });
    });
    function getMessages(){
        $.get('../../messages', function(messages) {
            $('#chatmsg').html(messages);
        });
    }

    setInterval(getMessages, 2000);

});
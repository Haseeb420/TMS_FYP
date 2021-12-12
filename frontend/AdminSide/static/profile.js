
$(document).on('click', '#id_user_save_btn', function() {
    $(".formBox").LoadingOverlay("show");
    var csrf_middleware_token = $('[name="csrfmiddlewaretoken"]').val();
    data = {
        'first_name': $("#id_first_name").val(),
        'last_name': $("#id_last_name").val(),
        'email': $("#id_email").val(),
        'phone_number': $("#id_phone_number").val(),
        'csrfmiddlewaretoken': csrf_middleware_token
    }
    
    $.ajax({
        type: 'POST',
        url: window.location.href,
        data: data,
    }).done(function(res) {
        $(".formBox").LoadingOverlay("hide");
        if (res['errors']) {
            $("#alert").html("")
            if (res['errors']['email']) {
                for (var i = 0; i < res['errors']['email'].length; i++) {
                    $("#alert").append('<div class="alert alert-danger" role="alert">' + res['errors']['email'][i] + '</div>')
                }
            }
            if (res['errors']['phone_number']) {
                for (var i = 0; i < res['errors']['phone_number'].length; i++) {
                    $("#alert").append('<div class="alert alert-danger" role="alert">' + res['errors']['phone_number'][i] + '</div>')
                }
            }                
        } else {
        }
    }).fail(function(err) {
        console.log(err)
    })
})

$(document).on('click', '.changePassword', function(){
    $(".userForm").css('display', 'none')
    $(".reset-password").css('display', 'block')
    
});

$(document).on('click', '.cancelBtn', function(){
    $(".reset-password").css('display', 'none')
    $(".userForm").css('display', 'block')
});

$(document).on('click', '#id_save_pass_btn', function() {
    $(".formBox").LoadingOverlay("show");
    var csrf_middleware_token = $('[name="csrfmiddlewaretoken"]').val();    
    data = {
        'old_password': $("#id_old_password").val(),
        'new_password': $("#id_new_password").val(),
        'confirm_password': $("#id_confirm_password").val(),
        'csrfmiddlewaretoken': csrf_middleware_token
    }

    $.ajax({
        type: 'POST',
        url: '/management/change-password',
        data: data,
    }).done(function(res) {
        $(".formBox").LoadingOverlay("hide");
        if (res['error']) {
            $("#alert").html("")
            $("#alert").append('<div class="alert alert-danger" role="alert">' + res['error'] + '</div>')                
        } else {
            window.location('/management/profile')
        }
    }).fail(function(err) {
        console.log(err)
    })
})

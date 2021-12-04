$(document).on("click", ".delete_btn", function(event) {
    event.preventDefault();
    var answer = confirm('Are you sure you want to delete?');
    if (answer)
    {
        var target_url = null;
        if( $(this).attr("url") != undefined)
            target_url = $(this).attr("url");
        var dic = {};
        dic['csrfmiddlewaretoken']= $('[name="csrfmiddlewaretoken"]').val();
        $.ajax({
                url: target_url,
                type: "POST",
                data: dic,
                success: function(data) {
                    if(data['success'])
                    {
                        $("#"+data['uuid']).remove();
                    }
                },
                error: function(request, error, status) {
                    alert(JSON.stringify(request))
                }
            });


    }

});

$(document).on("click", ".deactive_btn", function(event) {
    event.preventDefault();
    var answer = confirm('Are you sure you want to deactivate this user?');
    if (answer)
    {
        var target_url = null;
        if( $(this).attr("url") != undefined)
            target_url = $(this).attr("url");
        var dic = {};
        dic['csrfmiddlewaretoken']= $('[name="csrfmiddlewaretoken"]').val();
        $.ajax({
                url: target_url,
                type: "POST",
                data: dic,
                success: function(data) {
                    if(data['success'])
                    {
                        $("#"+data['uuid']).css('color', 'red')
                    }
                },
                error: function(request, error, status) {
                    alert(JSON.stringify(request))
                }
            });


    }

});
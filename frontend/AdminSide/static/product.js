$(document).keypress(
    function(event) {
        if (event.which == '13') {
            event.preventDefault();
        }
    });


$(document).on('change', '#id_logo', function() {
    var reader = new FileReader();
    reader.onload = function(e) {
        // get loaded data and render thumbnail.
        document.getElementById("id_selected_logo").src = e.target.result;
        $("#previous_image").remove();
    };
    // read the image file as a data URL.
    reader.readAsDataURL(this.files[0]);
});

function clear_fields() {
    $("#id_name").val("");
    $("#id_category").val("");
    $("#id_country").val("");
    $("#id_price").val("");
    $("#id_description").val("");
    $("#id_logo_image").val("");
    $("#id_quantity").val("");
    $("#id_subscription_price").val("");
    $("#id_Tags").val("");
    $('#id_selected').attr('src', ' ');
    amsifySuggestags = new AmsifySuggestags($('input[name="varcolor"]'));
    amsifySuggestags._init();
    amsifySuggestags.destroy();
    $('input[name="varcolor"]').amsifySuggestags({
        type: 'amsify',
        tagLimit: 5
    });
    tinyMCE.activeEditor.setContent('');
}


$(document).on("click", ".delete_product", function() {
    var uuid = $(this).data('uuid')
    var answer = confirm('Are you sure you want to delete?');
    if (answer) {
        var dic = {};
        dic['csrfmiddlewaretoken'] = $('[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url: '/management/delete-product/' + uuid,
            type: "POST",
            data: dic,
            success: function(data) {
                p_uuid = data['p_uuid']
                $('#id_' + p_uuid).remove();
                toastr.success('Product deleted successfully.', {
                    closeButton: true,
                    showMethod: 'show',
                    preventDuplicates: true,
                    hideMethod: 'fadeOut',
                    timeOut: 5000,
                    progressBar: true
                })
            },
            error: function(data) {}
        });
    }
})

$(document).ready(function() {
    $("#formCreateproduct").submit(function(e) {
        e.preventDefault()
        $(".product_update").LoadingOverlay("show");
        var uuid = $('#p_uuid').val();
        csrf_middleware_token = $('[name="csrfmiddlewaretoken"]').val();
        var formdata = new FormData();
        formdata.append('csrfmiddlewaretoken', csrf_middleware_token);
        formdata.append("name", $('#id_name').val())
        formdata.append("cat_code", $('#id_category').val())
        formdata.append("country_code", $('#id_country').val())
        formdata.append("description", $('#id_description').val())
        formdata.append('price', $("#id_price").val())
        formdata.append('quantity', $("#id_quantity").val())
        formdata.append('subscription_price', $("#id_subscription_price").val())
        formdata.append('tags', $("#id_Tags").val())
        formdata.append('selected_image', $("#id_selected_logo").attr("src"));
        $.ajax({
            type: 'POST',
            url: '/management/update-product/' + uuid,
            data: formdata,
            enctype: 'multipart/form-data',
            contentType: false,
            processData: false,
        }).done(function(res) {
            $(".product_update").LoadingOverlay("hide");
            toastr.success(res['success'], {
                closeButton: true,
                showMethod: 'show',
                preventDuplicates: true,
                hideMethod: 'fadeOut',
                timeOut: 5000,
                progressBar: true
            })
        }).fail(function(err) {
            $(".product_update").LoadingOverlay("hide");
            toastr.error(err.responseJSON.error, {
                closeButton: true,
                showMethod: 'show',
                preventDuplicates: true,
                hideMethod: 'fadeOut',
                timeOut: 5000,
                progressBar: true
            })
        })
    })
})

$(document).ready(function() {
    $("#Createproduct").submit(function(e) {
        e.preventDefault()
        $(".product_update").LoadingOverlay("show");
        csrf_middleware_token = $('[name="csrfmiddlewaretoken"]').val();
        var formdata = new FormData();
        formdata.append('csrfmiddlewaretoken', csrf_middleware_token);
        formdata.append("name", $('#id_name').val())
        formdata.append("cat_code", $('#id_category').val())
        formdata.append("country_code", $('#id_country').val())
        formdata.append("description", $('#id_description').val())
        formdata.append('price', $("#id_price").val())
        formdata.append('quantity', $("#id_quantity").val())
        formdata.append('subscription_price', $("#id_subscription_price").val())
        formdata.append('tags', $("#id_Tags").val())
        formdata.append('selected_image', $("#id_selected").attr("src"));
        $.ajax({
            type: 'POST',
            url: '/management/create-product/',
            data: formdata,
            enctype: 'multipart/form-data',
            contentType: false,
            processData: false,
        }).done(function(res) {
            toastr.success(res['success'], {
                closeButton: true,
                showMethod: 'show',
                preventDuplicates: true,
                hideMethod: 'fadeOut',
                timeOut: 5000,
                progressBar: true
            })

            $(".product_update").LoadingOverlay("hide");
            clear_fields()
        }).fail(function(err) {
            toastr.error(err.responseJSON.error, {
                closeButton: true,
                showMethod: 'show',
                preventDuplicates: true,
                hideMethod: 'fadeOut',
                timeOut: 5000,
                progressBar: true
            })
            $(".product_update").LoadingOverlay("hide");
        })
    })
})

$(document).on('change', '#id_logo_image', function() {
    var reader = new FileReader();
    reader.onload = function(e) {
        // get loaded data and render thumbnail.
        document.getElementById("id_selected").src = e.target.result;
        $("#previous_image").remove();
    };
    // read the image file as a data URL.
    reader.readAsDataURL(this.files[0]);
});

function ajax_search_list(ajax_payload) {
    var htmlstring = ''
    $.ajax({
        url: "/management/search-product/",
        type: "POST",
        data: ajax_payload,
        success: function(data) {
            // const tableOutput = document.querySelector("#table_company");
            //const id_table = document.querySelector("#id_table");
            const tbodyField = document.querySelector("#table_body");
            var search_value = $("#search_name_table").val();
            $("#id_table").LoadingOverlay("hide");
            //tableOutput.style.display = "none";

            if ((data['object_list']).length == 0) {
                $("#table_company").css('display', 'block');
                $("#id_table_ing").css('display', 'none');
                $(".pagination_trans").css('display', 'block');
                $("#table_company").removeAttr("style")
                if (search_value != '') {
                    toastr.error("No Data Exist", {
                        closeButton: true,
                        showMethod: 'show',
                        preventDuplicates: true,
                        hideMethod: 'fadeOut',
                        timeOut: 5000,
                        progressBar: true
                    })
                }
            } else {
                $(".pagination_trans").css('display', 'none');
                $("#table_company").css('display', 'none');
                $("#id_table_ing").css('display', 'block');
                $("#id_table_ing").removeAttr("style")
                var arr = data['object_list']
                for (var i = 0; i < arr.length; i++) {
                    //var datetime = new Date(arr[i].created_at);
                    htmlstring += `
                      <tr>
                      <td>${ arr[i].name }</td>
                      <td>${ arr[i].category__name }</td>
                      <td>${ arr[i].country__name }</td>
                      <td>${ arr[i].quantity }</td>
                      <td>${ arr[i].price }</td>
                      <td>${ arr[i].subscription_price }</td>
                      <td>${ moment(arr[i].created_at).format('YYYY-MM-DD HH:MM:ss') }</td>
                      <td><a class="button btn-sm btn-primary btnEditproduct" style="margin-left:8px"
                    href="../management/update-product/${ arr[i].uuid }">
                    <i class="fa fa-pencil"></i></a>
                    <a type="submit" class="button btn-sm btn-danger delete_product" 
                                                    data-uuid="${ arr[i].uuid }" style="margin-left:8px">
                                                    <i class="fa fa-trash-o"></i></a>
                      </td>
                    </tr>`
                }

                $(tbodyField).html(htmlstring)
            } //id_table.style.display = "block";

        },
        error: function(err) {
            $("#id_table_ing").LoadingOverlay("hide");
            $("#id_table_ing tbody").children().remove();
        }
    });
}

$(document).on("click", ".btn_code_table", function() {
    var input_ref = $(this).attr("input_id");
    var input = $("#" + input_ref).val();
    var dic = {
        "search_param": input,
        'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),
        "search_param_type": $(this).attr("search_param_type"),

    }
    $("#id_table").LoadingOverlay("show");
    ajax_search_list(dic);
})
$(document).on("click", ".btn_name_table", function() {
    var input = $("#search_name_table").val()
})
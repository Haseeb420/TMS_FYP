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

$(document).on('change', '#id_logo_images', function() {
    var reader = new FileReader();
    reader.onload = function(e) {
        // get loaded data and render thumbnail.
        document.getElementById("id_selecteds").src = e.target.result;
        $("#previous_image").remove();
    };
    // read the image file as a data URL.
    reader.readAsDataURL(this.files[0]);
});

function clear_fields() {
    $("#id_name").val("");
    $("#id_Code").val("");
    $("#id_category").val("");
    $("#id_logo_image").val("");
    $('#id_selected').attr('src', ' ');
}


$(document).ready(function() {
    $("#CreateCategory").submit(function(e) {   
        e.preventDefault()
        $(".cat_update").LoadingOverlay("show");
        var uuid = $('#p_uuid').val();
        csrf_middleware_token = $('[name="csrfmiddlewaretoken"]').val();
        var formdata = new FormData();
        formdata.append('csrfmiddlewaretoken', csrf_middleware_token);
        formdata.append("name", $('#id_name').val())
        formdata.append("category", $('#id_category').val())
        formdata.append("cat_code", $('#id_Code').val())
        formdata.append('selected_image', $("#id_selected").attr("src"));
        $.ajax({
            type: 'POST',
            url: '/management/categories',
            data: formdata,
            enctype: 'multipart/form-data',
            contentType: false,
            processData: false,
        }).done(function(data) {
            $('#table_company tr:first').after('<tr id="id_'+data['uuid']+'" ><td>'+data['name']+'</td><td>'+data['category']+'</td><td>'+data['code']+'</td><td>'+data['created_at']+'</td><td>'+
            '<a class="button btn-sm btn-primary btnEditcategory" style="margin-left:8px" data-toggle="modal" data-uuid="'+data['uuid']+'" data-target="#updatecat">'+
            '<i class="fa fa-pencil"></i></a>'+
            '<a type="submit" class="button btn-sm btn-danger delete_product" data-uuid="'+data['uuid']+'" style="margin-left:8px">'+
            '<i class="fa fa-trash-o"></i></a>'+
            '</td></tr>');
            toastr.success(data['success'], {
                closeButton: true,
                showMethod:'show',
                preventDuplicates: true,
                hideMethod:'fadeOut',
                timeOut: 5000,
                progressBar:true
            })
            $(".cat_update").LoadingOverlay("hide");
            $("#exampleModal").hide();
            $(".modal-backdrop").hide();
            clear_fields()
        }).fail(function(err) {
            toastr.error(err.responseJSON.error, {
                closeButton: true,
                showMethod:'show',
                preventDuplicates: true,
                hideMethod:'fadeOut',
                timeOut: 5000,
                progressBar:true
            })
            $(".cat_update").LoadingOverlay("hide");
        })
    })
})

$(document).on("click", ".delete_product", function() {    
    var uuid = $(this).data('uuid')
    var answer = confirm('Are you sure you want to delete?');
    if (answer)
    {
        var dic = {};
        dic['csrfmiddlewaretoken']= $('[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url: '/management/delete-category/'+uuid,
            type: "POST",
            data: dic,
            success: function(data) {     
                p_uuid = data['p_uuid']
                $('#id_'+p_uuid).remove();
                toastr.success(data['success'], {
                    closeButton: true,
                    showMethod:'show',
                    preventDuplicates: true,
                    hideMethod:'fadeOut',
                    timeOut: 5000,
                    progressBar:true
                })
            },
            error: function(data) {                            
            }
        });
    }
})

$(document).on("click", ".btnEditcategory", function() {    
    var uuid = $(this).data('uuid')
    var dic = {};
    dic['csrfmiddlewaretoken']= $('[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/management/fetch-category/'+uuid,
        type: "POST",
        data: dic,
        success: function(data) {  
            $('#id_names').val(data['name']);
            $('#id_Codes').val(data['code']);
            $('#id_categorys').val(data['category']);
            $('#id_selecteds').attr("src", data['image'])
            $('#p_uuid').val(data['uuid'])
            $('.catgory_update').attr('data-uuid', data['uuid'])
        },
        error: function(data) {                            
        }
    });
})

$(document).ready(function() {
    $("#UpdateCategory").submit(function(e) {   
        e.preventDefault()
        $(".catgory_update").LoadingOverlay("show");
        var uuid = $('#p_uuid').val();
        csrf_middleware_token = $('[name="csrfmiddlewaretoken"]').val();
        var formdata = new FormData();
        formdata.append('csrfmiddlewaretoken', csrf_middleware_token);
        formdata.append("name", $('#id_names').val())
        formdata.append("cat_code", $('#id_Codes').val())
        formdata.append("category", $('#id_categorys').val())
        formdata.append('selected_image', $("#id_selecteds").attr("src"));
        $.ajax({
            type: 'POST',
            url: '/management/update-category/'+uuid,
            data: formdata,
            enctype: 'multipart/form-data',
            contentType: false,
            processData: false,
        }).done(function(data) {
            $('#id_'+data['uuid']).remove()
            $('#table_company tr:first').after('<tr id="id_'+data['uuid']+'" ><td>'+data['name']+'</td><td>'+data['category']+'</td><td>'+data['code']+'</td><td>'+data['created_at']+'</td><td>'+
            '<a class="button btn-sm btn-primary btnEditcategory" style="margin-left:8px" data-toggle="modal" data-uuid="'+data['uuid']+'" data-target="#updatecat">'+
            '<i class="fa fa-pencil"></i></a>'+
            '<a type="submit" class="button btn-sm btn-danger delete_product" data-uuid="'+data['uuid']+'" style="margin-left:8px">'+
            '<i class="fa fa-trash-o"></i></a>'+
            '</td></tr>');
            toastr.success(data['success'], {
                closeButton: true,
                showMethod:'show',
                preventDuplicates: true,
                hideMethod:'fadeOut',
                timeOut: 5000,
                progressBar:true
            })
            $(".catgory_update").LoadingOverlay("hide");
            $("#updatecat").hide();
            $(".modal-backdrop").hide();
            clear_fields()
        }).fail(function(err) {
            $(".catgory_update").LoadingOverlay("hide");
            toastr.error(err.responseJSON.error, {
                closeButton: true,
                showMethod:'show',
                preventDuplicates: true,
                hideMethod:'fadeOut',
                timeOut: 5000,
                progressBar:true
            })
        })
    })
})

function ajax_search_list(ajax_payload) {
    var htmlstring = ''
    $.ajax({
        url: "/management/search-category/",
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
                      <td>${ arr[i].cat_type }</td>
                      <td>${ arr[i].code }</td>
                      <td>${ moment(arr[i].created_at).format('YYYY-MM-DD HH:MM:ss') }</td>
                      <td>
                      <a class="button btn-sm btn-primary btnEditcategory" style="margin-left:8px"
                      data-toggle="modal" data-uuid="${ arr[i].uuid }"
                      data-target="#updatecat">
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
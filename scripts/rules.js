
$(document).ready(function () {

    
    $('input[type="text"]').focus(function () {
        $(this).siblings('.l_move').css({ 'top': '0%' })
    });
    

    



    $("#rules_submit").on("click", function (e) {
        e.preventDefault();


        $.ajax({
            method: 'post',
            url: 'pythonfile/user.py',
            data: {
                what:"rules_insertion",
                userid: $("#id").val(),
                rules_area: $("#rules_area").val(),
            },
            success: function (data) {
                console.log(data)
                // alert(data)
                if (data.includes("rules inserted successfully")) {
                    swal({
                        title: "Yeah!",
                        text: "Rules Inserted Successfully!",
                        icon: "success",
                    });
                } else if (data.includes("one of the field is empty")) {
                    swal({
                        title: "Failed!",
                        text: "One of the field is empty!",
                        icon: "error",
                    });
                } else {
                    swal({
                        title: "Failed!",
                        text: "Sorry for inconvenience!",
                        icon: "error",
                    });
                }
            }
        });


    });



});

$(document).ready(function () {

    $("#search_user").on("click",function(e){
        e.preventDefault();
        window.location.href = "fee_search.html";
    })

    
    $(".add_btn").on("click",function(e){
        e.preventDefault();
        window.location.href="Feedetails.html";
    })


    $('input[type="text"]').focus(function () {
        $(this).siblings('.l_move').css({ 'top': '0%' })
    });

  // fetching userid for searching operation here
  $.ajax({
    method: 'post',
    url: 'pythonfile/user.py',
    data: {
        what: "fetchuserid",
    },
    success: function (data) {
        console.log(data)
        $("#userid").append(data)
    }
});



    $("#fee_submit").on("click", function (e) {
        e.preventDefault();
        $.ajax({
            method: 'post',
            url: 'pythonfile/user.py',
            data: {
                what: "fee_details_insertion",
                user_id: $("#id").val(),
                fee_amount: $("#fee_amt").val(),
                paydate: $("#paydate").val(),
                paymode: $('input[name="pay_mode"]:checked').val(),
                month_name: $("#month_name").val(),
                status: $("#status").val(),
            },
            success: function (data) {
                console.log(data)
                // alert(data)
                if (data.includes("fee inserted successfully")) {
                    swal({
                        title: "Yeah!",
                        text: "Fee Inserted Successfully!",
                        icon: "success",
                    });
                    $("#id").val("")
                    $("#fee_amt").val("")
                    $("#paydate").val("")
                    $('input[name="pay_mode"]:checked').val("")
                    $("#month_name").val("")
                    $("#status").val("")
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





    // performing search operation
    // doing searching opration here
    // code for display incoming data after executing query
    $('#user_search_btn').on('click', function () {

        $.ajax({
            method: 'post',
            url: 'pythonfile/user.py',
            data: {
                what: "fee_details_condtions",
                userid: $('#userid').val(),
                fee_amt: $('#fee_amt').val(),
                paydate: $('#paydate').val(),
                pay_mode: $('input[name="pay_mode"]:checked').val(),
                month_name: $('#month_name').val(),
                status: $('#status').val(),
            },
            success: function (data) {
                console.log(data);

                if (data.includes("please select one field")) {
                    $('.below_card').css({ "display": "none" })
                    swal({
                        title: "Failed!",
                        text: "please select atleast one field",
                        icon: "error",
                    });
                } else if (data.includes("fee details fetched successfully")) {
                    $('.below_card').css({ "display": "block" })
                    $('.table_container').html(data)

                } else if (data.includes("no data available")) {
                    $('.below_card').css({ "display": "none" })
                    swal({
                        title: "Failed!",
                        text: "no data available",
                        icon: "error",
                    });
                }


                // if user click on delete button
                $(".del").on("click", function () {
                    let uid = $(this).closest('tr').children('td:first-child').text();
                    // console.log(fid);

                    swal({
                        title: "Are you sure?",
                        text: "Once deleted, you will not be able to recover this data!",
                        icon: "warning",
                        buttons: true,
                        dangerMode: true,
                    })
                        .then((willDelete) => {
                            if (willDelete) {
                                $.ajax({
                                    method: 'post',
                                    url: 'pythonfile/user.py',
                                    data: {
                                        what: "deletefee",
                                        userid: uid
                                    },
                                    success: function (data) {
                                        console.log(data);

                                        if (data.includes("room allocation deleted successfully")) {

                                            swal("Yeah! Your data has been deleted!", {
                                                icon: "success",
                                            });

                                        } else {
                                            swal({
                                                title: "Failed!",
                                                text: "unable to delete somethings error!",
                                                icon: "error",
                                            });
                                        }
                                    },
                                });
                                $(this).closest('tr').remove();
                            } else {
                                swal("Your data is safe!", { icon: "success" });
                            }
                        });
                });

                $("#edit").on("click", function () {
                    let uid = $(this).closest('tr').children('td:first-child').text();
                    // console.log(pid);
                    $.ajax({
                        method: 'post',
                        url: 'pythonfile/user.py',
                        data: {
                            what: "fetchFeeUpdate",
                            userid: uid
                        },
                        success: function (data) {
                            console.log(data);
                            if (data.includes("data fetching successfully")) {
                                $(".form_placeholder").css({ "display": "block" })
                                $(".form_placeholder").html(data)






                                // code for saving the updated the data when use click on update button
                                $("#save").on("click", function (e) {
                                    e.preventDefault();
                                    d = "savetheFeeUpdate"


                                    $.ajax({
                                        method: 'post',
                                        url: 'pythonfile/user.py',
                                        data: {
                                            what: d,
                                            userid1: $("#userid1").val(),
                                            fee_amt1: $("#fee_amt1").val(),
                                            paydate1: $("#paydate1").val(),
                                            paymode1: $('input[name="pay_mode"]:checked').val(),
                                            month_name1: $("#month_name1").val(),
                                            status1: $("#status1").val(),
                                        },
                                        success: function (data) {
                                            // window.location.href = 'showData.html'
                                            console.log(data);

                                            if (data.includes("fee details successfully updated")) {
                                                swal({
                                                    title: "Success!",
                                                    text: "Fee Details Updated Successfully",
                                                    icon: "success",
                                                });
                                                $('.form_placeholder').css({ "display": "none" })
                                            } else {
                                                swal({
                                                    title: "Failed!",
                                                    text: "somethings error",
                                                    icon: "error",
                                                });
                                            }
                                        },
                                    });
                                })


                            }

                            // on click of cross icon
                            $(".form_placeholder .fa-xmark").on("click", function () {
                                $(".form_placeholder").css({ "display": "none" });
                            })


                        },
                    });
                });




            },
        });
    });


});
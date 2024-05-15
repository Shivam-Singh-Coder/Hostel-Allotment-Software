
$(document).ready(function () {

    $("#search_user").on("click",function(e){
        e.preventDefault();
        window.location.href = "room_search.html";
    })

    
    $(".add_btn").on("click",function(e){
        e.preventDefault();
        window.location.href="Roomdetail.html";
    })
    
    $('input[type="text"]').focus(function () {
        $(this).siblings('.l_move').css({ 'top': '0%' })
    });




    $("#room_submit").on("click", function (e) {
        e.preventDefault();


        $.ajax({
            method: 'post',
            url: 'pythonfile/user.py',
            data: {
                what: "room_details_insertion",
                room_no: $("#room_no").val(),
                room_type: $("#room_type").val(),
                total_bed: $("#t_bed").val(),
                status: $("#status").val(),
            },
            success: function (data) {
                console.log(data)
                // alert(data)
                if (data.includes("room details inserted successfully")) {
                    swal({
                        title: "Yeah!",
                        text: "Data Inserted Successfully!",
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



    // fetching roomid for searching operation here
    $.ajax({
        method: 'post',
        url: 'pythonfile/user.py',
        data: {
            what: "fetchroomid",
        },
        success: function (data) {
            console.log(data)
            $("#roomno").append(data)
        }
    });


    // doing searching opration here
    // code for display incoming data after executing query
    $('#user_search_btn').on('click', function () {

        $.ajax({
            method: 'post',
            url: 'pythonfile/user.py',
            data: {
                what: "fetch_room_conditions",
                room_no: $('#roomno').val(),
                roomtype: $('#roomtype').val(),
                total_bed: $('#t_bed').val(),
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
                } else if (data.includes("room details fetched successfully")) {
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
                    let rid = $(this).closest('tr').children('td:first-child').text();
                    console.log(rid);

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
                                        what: "deleteroom",
                                        roomno: rid
                                    },
                                    success: function (data) {
                                        console.log(data);

                                        if (data.includes("room deleted successfully")) {

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
                    let rid = $(this).closest('tr').children('td:first-child').text();
                    // console.log(pid);
                    $.ajax({
                        method: 'post',
                        url: 'pythonfile/user.py',
                        data: {
                            what: "fetchForRoomUpdate",
                            roomid: rid
                        },
                        success: function (data) {
                            console.log(data);
                            if (data.includes("data fetching successfully")) {
                                $(".form_placeholder").css({ "display": "block" })
                                $(".form_placeholder").html(data)














                                // code for saving the updated the data when use click on update button
                                $("#save").on("click", function (e) {
                                    e.preventDefault();
                                    d = "savetheRoomupdate"


                                    $.ajax({
                                        method: 'post',
                                        url: 'pythonfile/user.py',
                                        data: {
                                            what: d,
                                            room_no: $("#room_no").val(),
                                            room_type: $("#room_type").val(),
                                            t_bed1: $("#t_bed1").val(),
                                            status1: $("#status1").val(),
                                        },
                                        success: function (data) {
                                            // window.location.href = 'showData.html'
                                            console.log(data);

                                            if (data.includes("room details successfully updated")) {
                                                swal({
                                                    title: "Success!",
                                                    text: "Room Details updated successfully",
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


    // docu


});
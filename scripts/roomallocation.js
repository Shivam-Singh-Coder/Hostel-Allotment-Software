
$(document).ready(function () {

    $("#search_user").on("click",function(e){
        e.preventDefault();
        window.location.href = "room_alloc_search.html";
    })

    
    $(".add_btn").on("click",function(e){
        e.preventDefault();
        window.location.href="Roomallocation.html";
    })


    $('input[type="text"]').focus(function () {
        $(this).siblings('.l_move').css({ 'top': '0%' })
    });


    // fetching room id
    $.ajax({
        method: 'post',
        url: 'pythonfile/user.py',
        data: {
            what: "fetchroomid",
        },
        success: function (data) {
            console.log(data)
            $("#roomid").append(data)
        }
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



    // $("#userid").change(function () {
    //     // e.preventDefault();

    //     $.ajax({
    //         method: 'post',
    //         url: 'pythonfile/user.py',
    //         data: {
    //             what: "checkuserid",
    //             userid: $("#userid").val()
    //         },
    //         success: function (data) {
    //             console.log(data)
    //             if (data.includes("Userid doesnot exist"))
    //                 swal({
    //                     title: "Failed!",
    //                     text: "Userid doesnot exit",
    //                     icon: "error",
    //                 });
    //         }
    //     });

    // });



    $("#room_alloc_submit").on("click", function (e) {
        e.preventDefault();


        $.ajax({
            method: 'post',
            url: 'pythonfile/user.py',
            data: {
                what: "room_allocation",
                room_no: $("#roomid").val(),
                userid: $('#userid').val(),
                checkin: $("#checkin").val(),
                checkout: $("#checkout").val(),
                status: $("#status").val(),
            },
            success: function (data) {
                console.log(data)
                // alert(data)
                if (data.includes("room allocated successfully")) {
                    swal({
                        title: "Yeah!",
                        text: "Room allocated Successfully!",
                        icon: "success",
                    });

                    $("#roomid").val("");
                    $('#userid').val("");
                    $("#checkin").val("");
                    $("#checkout").val("");
                    $("#status").val("");

                } else if (data.includes("one of the field is empty")) {
                    swal({
                        title: "Failed!",
                        text: "One of the field is empty!",
                        icon: "error",
                    });
                }
                else if (data.includes("userid doesnot exists")) {
                    swal({
                        title: "Failed!",
                        text: "User Id doesn't exists!",
                        icon: "error",
                    });
                }else {
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
                what: "fetch_room_allocation_conditions",
                roomid: $('#roomid').val(),
                userid: $('#userid').val(),
                checkin: $('#checkin').val(),
                checkout: $('#checkout').val(),
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
                } else if (data.includes("room allocation fetched successfully")) {
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
                    let raid = $(this).closest('tr').children('td:first-child').text();
                    console.log(raid);

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
                                        what: "deleteroomalloc",
                                        roomid: raid
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
                    let rid = $(this).closest('tr').children('td:first-child').text();
                    // console.log(pid);
                    $.ajax({
                        method: 'post',
                        url: 'pythonfile/user.py',
                        data: {
                            what: "fetchForRoomAllocUpdate",
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
                                    d = "savetheRoomAllocupdate"


                                    $.ajax({
                                        method: 'post',
                                        url: 'pythonfile/user.py',
                                        data: {
                                            what: d,
                                            roomid1: $("#roomid1").val(),
                                            userid1: $("#userid1").val(),
                                            checkin1: $("#checkin1").val(),
                                            checkout1: $("#checkout1").val(),
                                            status1: $("#status1").val(),
                                        },
                                        success: function (data) {
                                            // window.location.href = 'showData.html'
                                            console.log(data);

                                            if (data.includes("room allocation details successfully updated")) {
                                                swal({
                                                    title: "Success!",
                                                    text: "Room Allocation Updated Successfully",
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
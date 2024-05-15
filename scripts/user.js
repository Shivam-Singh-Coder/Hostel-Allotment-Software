
$(document).ready(function () {

$("#search_user").on("click",function(e){
    e.preventDefault();
    window.location.href= "user_search.html";
})

    $('input[type="text"]').focus(function () {
        $(this).siblings('.l_move').css({ 'top': '0%' })
    });

    $(".add_btn").on("click",function(e){
        e.preventDefault();
        window.location.href="user.html";
    })

    let imageDataUrl1 = "";


    // image data url for image 1
    $("#pic").on("change", function (event) {
        var file = event.target.files[0];
        var reader = new FileReader();

        reader.onload = function (event) {
            imageDataUrl1 = event.target.result;
        };

        if (file) {
            reader.readAsDataURL(file);
        } else {
            console.error("No file selected.");
        }
    });



    $("#submit_btn").on("click", function (e) {
        e.preventDefault();

        // alert($("#id").val())
        // alert(imageDataUrl1)
        // alert($('input[name="gender"]:checked').val())

        $.ajax({
            method: 'post',
            url: 'pythonfile/user.py',
            data: {
                what: "user_details_insertion",
                emp_id: $("#id").val(),
                emp_name: $("#name").val(),
                emp_contact: $("#contact").val(),
                emp_gender: $('input[name="gender"]:checked').val(),
                emp_dob: $("#dob").val(),
                emp_blood: $("#bloodgrp").val(),
                emp_father: $("#f_name").val(),
                emp_mother: $("#m_name").val(),
                emp_par_contact: $("#p_contact").val(),
                emp_photo: imageDataUrl1,
                emp_aadhar: $("#aadhar").val(),
                emp_street: $("#street").val(),
                emp_dist_state: $("#dit").val(),
                emp_pincode: $("#pin").val(),
                emp_local_guard: $("#local_guard").val(),
                emp_local_guard_cont: $("#local_guard_contact").val(),
                emp_local_guard_addr: $("#local_guard_addr").val()
            },
            success: function (data) {
                console.log(data)
                // alert(data)
                if (data.includes("user inserted successfully")) {
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


    // doing searching opration here
    // code for display incoming data after executing query
    $('#user_search_btn').on('click', function () {

        $.ajax({
            method: 'post',
            url: 'pythonfile/user.py',
            data: {
                what: "fetch_user_conditions",
                userid: $('#userid').val(),
                username: $('#username').val(),
                mob_no: $('#mob_no').val(),
                fname: $('#fname').val(),
                mname: $('#mname').val(),
                aadharno: $('#aadharno').val(),
                bloodgrp: $('#bloodgrp').val(),
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
                } else if (data.includes("product details fetched successfully")) {
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
                    console.log(uid);

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
                                        what: "deleteuser",
                                        userid: uid
                                    },
                                    success: function (data) {
                                        console.log(data);

                                        if (data.includes("user deleted successfully")) {

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
                    // alert(uid)
                    $.ajax({
                        method: 'post',
                        url: 'pythonfile/user.py',
                        data: {
                            what: "fetchUserUpdate",
                            userid: uid
                        },
                        success: function (data) {
                            console.log(data);
                            if (data.includes("data fetching successfully")) {
                                $(".form_placeholder").css({ "display": "block" })
                                $(".form_placeholder").html(data)




                                // image data url for image 1
                                $("#pic1").on("change", function (event) {
                                    var file = event.target.files[0];
                                    var reader = new FileReader();

                                    reader.onload = function (event) {
                                        imageDataUrl1 = event.target.result;
                                    };

                                    if (file) {
                                        reader.readAsDataURL(file);
                                    } else {
                                        console.error("No file selected.");
                                    }
                                });



                                // code for saving the updated the data when use click on update button
                                $("#save").on("click", function (e) {
                                    e.preventDefault();


                                    $.ajax({
                                        method: 'post',
                                        url: 'pythonfile/user.py',
                                        data: {
                                            what: "savetheUserUpdate",
                                            // what: "user_details_insertion",
                                            emp_id1: $("#id1").val(),
                                            emp_name1: $("#name1").val(),
                                            emp_contact1: $("#contact1").val(),
                                            emp_gender1: $('input[name="gender"]:checked').val(),
                                            emp_dob1: $("#dob1").val(),
                                            emp_blood1: $("#bloodgrp1").val(),
                                            emp_father1: $("#f_name1").val(),
                                            emp_mother1: $("#m_name1").val(),
                                            emp_par_contact1: $("#p_contact1").val(),
                                            emp_photo1: imageDataUrl1,
                                            emp_aadhar1: $("#aadhar1").val(),
                                            emp_street1: $("#street1").val(),
                                            emp_dist_state1: $("#dit1").val(),
                                            emp_pincode1: $("#pin1").val(),
                                            emp_local_guard1: $("#local_guard1").val(),
                                            emp_local_guard_cont1: $("#local_guard_contact1").val(),
                                            emp_local_guard_addr1: $("#local_guard_addr1").val()
                                        },
                                        success: function (data) {
                                            // window.location.href = 'showData.html'
                                            console.log(data);

                                            if (data.includes("user details successfully updated")) {
                                                swal({
                                                    title: "Success!",
                                                    text: "User Details Updated Successfully",
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
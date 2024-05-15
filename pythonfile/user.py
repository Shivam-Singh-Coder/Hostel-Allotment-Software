#! C:\Users\ASUS\AppData\Local\Programs\Python\Python312\python.exe
print ("Content-Type: text/html\r\n\r\n")
# print()
import cgi
# import cgitb
import mysql.connector


con = mysql.connector.connect(host='localhost', user='hostel', passwd='data73063',database='hostel')
# print(con)
cur=con.cursor()
# print(cur)
f=cgi.FieldStorage()
flaguser = False
# print("jhj")
what = f.getvalue("what")
if(what == "user_details_insertion"):
    try:
        user_id = f.getvalue("emp_id")
        user_name = f.getvalue("emp_name")
        user_contact = f.getvalue("emp_contact")
        user_gender = f.getvalue("emp_gender")
        user_dob = f.getvalue("emp_dob")
        user_blood = f.getvalue("emp_blood")
        user_father = f.getvalue("emp_father")
        user_mother = f.getvalue("emp_mother")
        user_par_contact = f.getvalue("emp_par_contact")
        user_photo = f.getvalue("emp_photo")
        user_aadhar = f.getvalue("emp_aadhar")
        user_street = f.getvalue("emp_street")
        user_dist_state = f.getvalue("emp_dist_state")
        user_pincode = f.getvalue("emp_pincode")
        user_local_guard = f.getvalue("emp_local_guard")
        user_local_guard_cont = f.getvalue("emp_local_guard_cont")
        user_local_guard_addr = f.getvalue("emp_local_guard_addr")

        if( user_name != None and user_contact != None and user_dob != None
        and user_gender != None and user_dob != None and user_blood != None
        and user_father != None and user_mother != None and user_par_contact != None
        and user_photo != None and user_aadhar != None and user_street != None 
        and user_dist_state != None and user_pincode != None and user_local_guard != None and
        user_local_guard_cont != None and user_local_guard_addr != None):
            
            user_insert_query = f"insert into user_info (userid,username,user_cont,user_gender,user_dob,user_blood_grp,user_f_name,user_m_name,user_p_contact,user_pic,user_addhar,user_street,user_dstate,user_pin, user_local_guard,user_local_guard_cont, user_local_guard_add) values('{user_id}','{user_name}','{user_contact}','{user_gender}','{user_dob}','{user_blood}','{user_father}','{user_mother}','{user_par_contact}','{user_photo}','{user_aadhar}','{user_street}','{user_dist_state}','{user_pincode}','{user_local_guard}','{user_local_guard_cont}','{user_local_guard_addr}')"
            print(user_insert_query)
            cur.execute(user_insert_query)
            print("yaha")
            con.commit()
            print("user inserted successfully")
        else:
            print("one of the field is empty")


    except Exception as e:
        print(e)

elif(what == "room_details_insertion"):
    try:
        room_no = f.getvalue("room_no")
        room_type = f.getvalue("room_type")
        total_bed = f.getvalue("total_bed")
        status = f.getvalue("status")

        if(room_no != None and room_type != None and total_bed != None and status != None):
            room_details_insert = f"insert into room_details (room_no, room_type, total_bed, status) values('{room_no}','{room_type}','{total_bed}','{status}')"
            cur.execute(room_details_insert)
            con.commit()
            print("room details inserted successfully")
        else:
            print("one of the field is empty")

    except Exception as e:
        print(e)

elif(what=="fetchroomid"):
    try:
        cur.execute("select distinct room_no from room_details")
        res = cur.fetchall()
        if res != []:
            for row in res:
                print(f"<option value='{row[0]}'>{row[0]}</option>")
        else:
            print()
    except Exception as e:
        print(e)



elif(what=="checkuserid"):
    userid = f.getvalue("userid")
    checkUsername = cur.execute(f"SELECT userid FROM user_info WHERE userid='{userid}'")
    res = cur.fetchall()
    if res == []:
        print('Userid doesnot exist')
        flaguser=False
    else:
        flaguser=True


elif(what == "room_allocation"):
    try:
        room_no = f.getvalue("room_no")
        userid = f.getvalue("userid")
        checkin = f.getvalue("checkin")
        checkout = f.getvalue("checkout")
        status = f.getvalue("status")

        if(room_no != None and userid != None  and checkin != None and checkout != None and status != None):
            room_allocation_insert = f"insert into room_allocation(roomid, userid,checkin,checkout,status) values('{room_no}','{userid}','{checkin}','{checkout}','{status}')"
            cur.execute(room_allocation_insert)
            con.commit()
            print("room allocated successfully")
        else:
            print("one of the field is empty")

    except Exception as e:
        print(e)

elif(what == "fee_details_insertion"):
    try:
        user_id = f.getvalue("user_id")
        fee_amount = f.getvalue("fee_amount")
        paydate = f.getvalue("paydate")
        paymode = f.getvalue("paymode")
        month_name = f.getvalue("month_name")
        status = f.getvalue("status")

        if(user_id != None and fee_amount != None and paydate != None and paymode != None and month_name != None and status != None):
            fee_insertion = f"insert into fee_details(userid,fee_amount,pay_date,pay_mode,month_name,f_status) values('{user_id}','{fee_amount}','{paydate}','{paymode}','{month_name}','{status}')"
            cur.execute(fee_insertion)
            con.commit()
            print("fee inserted successfully")
        else:
            print("one of the field is empty")

    except Exception as e:
        print(e)


elif(what == "rules_insertion"):
    try:
        user_id = f.getvalue("userid")
        rules_area = f.getvalue("rules_area")

        if(user_id != None and rules_area != None):
            rules_insertion = f"insert into rules(userid,rules) values('{user_id}','{rules_area}')"
            cur.execute(rules_insertion)
            con.commit()
            print("rules inserted successfully")
        else:
            print("one of the field is empty")

    except Exception as e:
        print(e)


elif(what=="fetchuserid"):
    try:
        cur.execute("select distinct userid from user_info")
        res = cur.fetchall()
        if res != []:
            for row in res:
                print(f"<option value='{row[0]}'>{row[0]}</option>")
        else:
            print()
    except Exception as e:
        print(e)


# fetching data on click of search button or searching data
elif(what == "fetch_user_conditions"):
    # print(d)
    try:
        userid = f.getvalue("userid")
        username = f.getvalue("username")
        mob_no = f.getvalue("mob_no")
        fname = f.getvalue("fname")
        mname = f.getvalue("mname")
        aadharno = f.getvalue("aadharno")
        bloodgrp = f.getvalue("bloodgrp")
        

        # Construct conditions for the SQL query
        conditions = []
        if userid != None:
            conditions.append(f"userid = '{userid}'")
        if username is not None:
            conditions.append(f"username = '{username}'")
        if mob_no is not None:
            conditions.append(f"user_cont = '{mob_no}'")
        if fname is not None:
            conditions.append(f"user_f_name >= '{fname}'")
        if mname is not None:
            conditions.append(f"user_m_name < '{mname}'")
        if aadharno != None:
            conditions.append(f"user_addhar = '{aadharno}'")
        if bloodgrp is not None:
            conditions.append(f"user_blood_grp >= '{bloodgrp}'")

        # Construct the SQL query
        fetch_user_query = "SELECT * FROM user_info"
        if conditions:
            fetch_user_query += " WHERE " + " AND ".join(conditions)
       
        # print(fetch_user_query)


        cur.execute(fetch_user_query)
        srr = cur.fetchall()
        if srr != []:
            # print("<br>yes")
            print("<table class='tab'>")
            print("<tr>")
            print("<th>User Id</th>")
            print("<th>User Name</th>")
            print("<th>User Contact</th>")
            print("<th>User Gender</th>")
            print("<th>User DOB</th>")
            print("<th>User Blood Group</th>")
            print("<th>F's Name</th>")
            print("<th>M's Name</th>")
            print("<th>Parent Contact</th>")
            print("<th>Aadhar No</th>")
            print("<th>Street No</th>")
            print("<th>District State</th>")
            print("<th>PinCode No</th>")
            print("<th>Local Guardian</th>")
            print("<th>Local Guardian Contact</th>")
            print("<th>Local Guardian Address</th>")
            print("<th>images</th>")
            # print("<th>Size</th>")
            print("<th colspan='2' style='text-align:center;'>action</th>")
            print("</tr>")
            for row in srr:
                # print(row)
                print("<tr>")
                print(f'<td>{row[0]}</td>')
                print(f'<td>{row[1]}</td>')
                print(f'<td>{row[2]}</td>')
                print(f'<td>{row[3]}</td>')
                print(f'<td>{row[4]}</td>')
                print(f'<td>{row[5]}</td>')
                print(f'<td>{row[6]}</td>')
                print(f'<td>{row[7]}</td>')
                print(f'<td>{row[8]}</td>')
                print(f'<td>{row[10]}</td>')
                print(f'<td>{row[11]}</td>')
                print(f'<td>{row[12]}</td>')
                print(f'<td>{row[13]}</td>')
                print(f'<td>{row[15]}</td>')
                print(f'<td>{row[16]}</td>')
                print(f'<td>{row[14]}</td>')
                
                print(f'<td><a href=''>view</a></td>')
                print(f"<td><i class='fa-solid fa-pen-to-square fa-xl edit'  id=\"edit\" ></i></td>")
                print(f"<td><i class='fa-solid fa-trash-can fa-xl del'></i></td>")
                print("</tr>")
            print("</table>")
            print("<p style='display:none;'>product details fetched successfully</p>")
        else:
            # print("no")
            print("no data available")
    except Exception as e:
        print(e)

# deleting product category on click of delete button
elif(what == "deleteuser"):
    try:
        user_id = f.getvalue("userid")
        # print(prod_id + " have gotten")
        delete_user_query = f"delete from user_info where userid = '{user_id}'"
        print(delete_user_query)
        cur.execute(delete_user_query)
        con.commit()
        print("user deleted successfully")
    except Exception as e:
        print(e)

elif(what=="fetchroomid"):
    try:
        cur.execute("select distinct room_no from room_details")
        res = cur.fetchall()
        if res != []:
            for row in res:
                print(f"<option value='{row[0]}'>{row[0]}</option>")
        else:
            print()
    except Exception as e:
        print(e)

# fetching data on click of search button or searching data
elif(what == "fetch_room_conditions"):
    # print(d)
    try:
        room_no = f.getvalue("room_no")
        roomtype = f.getvalue("roomtype")
        total_bed = f.getvalue("total_bed")
        status = f.getvalue("status")
        

        # Construct conditions for the SQL query
        conditions = []
        if room_no != None:
            conditions.append(f"room_no = '{room_no}'")
        if roomtype is not None:
            conditions.append(f"room_type = '{roomtype}'")
        if total_bed is not None:
            conditions.append(f"total_bed <= '{total_bed}'")
        if status is not None:
            conditions.append(f"status = '{status}'")
        

        # Construct the SQL query
        fetch_room_query = "SELECT * FROM room_details"
        if conditions:
            fetch_room_query += " WHERE " + " AND ".join(conditions)
       
        # print(fetch_user_query)


        cur.execute(fetch_room_query)
        srr = cur.fetchall()
        if srr != []:
            # print("<br>yes")
            print("<table class='tab'>")
            print("<tr>")
            print("<th>Room No</th>")
            print("<th>Room Type</th>")
            print("<th>Total Bed</th>")
            print("<th>Status Gender</th>")
            print("<th colspan='2' style='text-align:center;'>action</th>")
            print("</tr>")
            for row in srr:
                # print(row)
                print("<tr>")
                print(f'<td>{row[0]}</td>')
                print(f'<td>{row[1]}</td>')
                print(f'<td>{row[2]}</td>')
                print(f'<td>{row[3]}</td>')
                
                print(f"<td><i class='fa-solid fa-pen-to-square fa-xl edit'  id=\"edit\" ></i></td>")
                print(f"<td><i class='fa-solid fa-trash-can fa-xl del'></i></td>")
                print("</tr>")
            print("</table>")
            print("<p style='display:none;'>room details fetched successfully</p>")
        else:
            # print("no")
            print("no data available")
    except Exception as e:
        print(e)

# deleting product category on click of delete button
elif(what == "deleteroom"):
    try:
        roomid = f.getvalue("roomno")
        delete_room_query = f"delete from room_details where room_no = '{roomid}'"
        print(delete_room_query)
        cur.execute(delete_room_query)
        con.commit()
        print("room deleted successfully")
    except Exception as e:
        print(e)

# fetching data on click of search button or searching data
elif(what == "fetch_room_allocation_conditions"):
    # print(d)
    try:
        roomid = f.getvalue("roomid")
        userid = f.getvalue("userid")
        checkin = f.getvalue("checkin")
        checkout = f.getvalue("checkout")
        status = f.getvalue("status")
        

        # Construct conditions for the SQL query
        conditions = []
        if roomid != None:
            conditions.append(f"roomid = '{roomid}'")
        if userid is not None:
            conditions.append(f"userid = '{userid}'")
        if checkin is not None:
            conditions.append(f"checkin = '{checkin}'")
        if checkout is not None:
            conditions.append(f"checkout = '{checkout}'")
        if status is not None:
            conditions.append(f"status = '{status}'")
        

        # Construct the SQL query
        fetch_room_alloc_query = "SELECT * FROM room_allocation"
        if conditions:
            fetch_room_alloc_query += " WHERE " + " AND ".join(conditions)
       
        # print(fetch_user_query)


        cur.execute(fetch_room_alloc_query)
        srr = cur.fetchall()
        if srr != []:
            # print("<br>yes")
            print("<table class='tab'>")
            print("<tr>")
            print("<th>Room No</th>")
            print("<th>User Id</th>")
            print("<th>Checkin</th>")
            print("<th>Checkout</th>")
            print("<th>Status</th>")
            print("<th colspan='2' style='text-align:center;'>action</th>")
            print("</tr>")
            for row in srr:
                # print(row)
                print("<tr>")
                print(f'<td>{row[0]}</td>')
                print(f'<td>{row[1]}</td>')
                print(f'<td>{row[2]}</td>')
                print(f'<td>{row[3]}</td>')
                print(f'<td>{row[4]}</td>')
                
                print(f"<td><i class='fa-solid fa-pen-to-square fa-xl edit'  id=\"edit\" ></i></td>")
                print(f"<td><i class='fa-solid fa-trash-can fa-xl del'></i></td>")
                print("</tr>")
            print("</table>")
            print("<p style='display:none;'>room allocation fetched successfully</p>")
        else:
            # print("no")
            print("no data available")
    except Exception as e:
        print(e)

# deleting product category on click of delete button
elif(what == "deleteroomalloc"):
    try:
        roomid = f.getvalue("roomid")
        delete_room_alloc_query = f"delete from room_allocation where roomid = '{roomid}'"
        print(delete_room_alloc_query)
        cur.execute(delete_room_alloc_query)
        con.commit()
        print("room allocation deleted successfully")
    except Exception as e:
        print(e)


# fetching data on click of search button or searching data
elif(what == "fee_details_condtions"):
    # print(d)
    try:
        userid = f.getvalue("userid")
        fee_amt = f.getvalue("fee_amt")
        paydate = f.getvalue("paydate")
        pay_mode = f.getvalue("pay_mode")
        month_name = f.getvalue("month_name")
        status = f.getvalue("status")
        

        # Construct conditions for the SQL query
        conditions = []
        if userid != None:
            conditions.append(f"userid = '{userid}'")
        if fee_amt is not None:
            conditions.append(f"fee_amount = '{fee_amt}'")
        if paydate is not None:
            conditions.append(f"pay_date = '{paydate}'")
        if pay_mode is not None:
            conditions.append(f"pay_mode = '{pay_mode}'")
        if month_name is not None:
            conditions.append(f"month_name = '{month_name}'")
        if status is not None:
            conditions.append(f"f_status = '{status}'")
        

        # Construct the SQL query
        fetch_feedetails_query = "SELECT * FROM fee_details"
        if conditions:
            fetch_feedetails_query += " WHERE " + " AND ".join(conditions)
       
        # print(fetch_feedetails_query)


        cur.execute(fetch_feedetails_query)
        srr = cur.fetchall()
        if srr != []:
            # print("<br>yes")
            print("<table class='tab'>")
            print("<tr>")
            print("<th>User Id</th>")
            print("<th>Fee Amount</th>")
            print("<th>Pay Date</th>")
            print("<th>Pay Mode</th>")
            print("<th>Month Name</th>")
            print("<th>Payment Status</th>")
            print("<th colspan='2' style='text-align:center;'>action</th>")
            print("</tr>")
            for row in srr:
                # print(row)
                print("<tr>")
                print(f'<td>{row[0]}</td>')
                print(f'<td>{row[1]}</td>')
                print(f'<td>{row[2]}</td>')
                print(f'<td>{row[3]}</td>')
                print(f'<td>{row[4]}</td>')
                print(f'<td>{row[5]}</td>')
                
                print(f"<td><i class='fa-solid fa-pen-to-square fa-xl edit'  id=\"edit\" ></i></td>")
                print(f"<td><i class='fa-solid fa-trash-can fa-xl del'></i></td>")
                print("</tr>")
            print("</table>")
            print("<p style='display:none;'>fee details fetched successfully</p>")
        else:
            # print("no")
            print("no data available")
    except Exception as e:
        print(e)

# deleting product category on click of delete button
elif(what == "deletefee"):
    try:
        userid = f.getvalue("userid")
        delete_fee_query = f"delete from fee_details where userid = '{userid}'"
        print(delete_fee_query)
        cur.execute(delete_fee_query)
        con.commit()
        print("room allocation deleted successfully")
    except Exception as e:
        print(e)

elif(what == "fetchForRoomUpdate"):
    # print(what)
    try:
        roomid = f.getvalue("roomid")
        # print(userid + " have gotten")
        if(roomid != None):
            fetch_for_upd_room = f"select * from room_details where room_no='{roomid}'"
            # print(fetch_for_upd_room)
            cur.execute(fetch_for_upd_room)
            res = cur.fetchall()
            if res != []:
                print("<div style='display:none;'>data fetching successfully</div>")
                # print(res)
                print("<span><i class='fa-solid fa-xmark fa-2xl'></i></span>")
                print("<form class='catupform'>")
                for row in res:
                    print(f'''<div class="parent">
      <h2>
        
         Room Details Form
      </h2>
      <form enctype="multipart/form-data" method="post">
        <table>
          <tr><td>
              <label class="l_move" for="room_no">Room No</label>
              <i class="fa-solid fa-people-roof i1"></i>
              <input
                required
                type="text"
                id="room_no"
                name="room_no"
                value='{row[0]}'
                readonly
              />
              <span> </span>
            </td>
            <td>
              <select name="" id="room_type">
                <option value="{row[1]}" selected>{row[1]}</option>
                <option value="ac">ac</option>
                <option value="non ac">non ac</option>
              </select>
              <span></span>
            </td>
            <td>
                <label class="l_move" for="t_bed1">Total Bed</label>
                <i class="fa-solid fa-bed i1"></i>
                <input required type="text" value='{row[2]}' id="t_bed1"
                />
                <span></span>
              </td>
          </tr>
       

          <tr>
            <td>
                <!-- <label class="l_move" for="status">Status</label> -->
                <select name="" id="status1">
                  <option value='{row[3]}'>{row[3]}</option>
                  <option value="active">Active</option>
                  <option value="inactive">Inactive</option>
                </select>
                <!-- <span></span> -->
                <span></span>
            </td>
            <td colspan="2">
              <div class="button">
                <button
                  type="submit"
                  value="Save"
                  style="background-color: rgb(0, 255, 0); color: black"
                  id="save"
                >
                  <i class="fa-solid fa-arrow-up-from-bracket"></i> &nbsp;
                  Submit
                </button>
                <button
                  type="reset"
                  value="Reset"
                  style="background-color: rgb(0, 208, 255); color: black"
                >
                  <i class="fa-solid fa-rotate-left"></i> Reset
                </button>
              </div>
            </td>
          </tr>
        </table>
      </form>
    </div>

''')
              
                print("</form>")
            else:
                print("no data available")
    except Exception as e:
        print(e)

elif(what == "savetheRoomupdate"):
    try:
        room_no = f.getvalue("room_no")
        room_type = f.getvalue("room_type")
        t_bed = f.getvalue("t_bed1")
        status = f.getvalue("status1")

        print(room_no,room_type,t_bed,status)
        
        if( room_type != None and t_bed != None and status != None):
            saveRoomUpdate_query = f"update room_details SET room_type = '{room_type}', total_bed = '{t_bed}',status = '{status}' where room_no = '{room_no}'"
            cur.execute(saveRoomUpdate_query)
            con.commit()
            print("room details successfully updated")
        else:
            print("no field should be empty")
    except Exception as e:
        print(e)

elif(what == "fetchForRoomAllocUpdate"):
    # print(what)
    try:
        roomid = f.getvalue("roomid")
        # print(userid + " have gotten")
        if(roomid != None):
            fetch_for_upd_room_alloc = f"select * from room_allocation where roomid='{roomid}'"
            # print(fetch_for_upd_room)
            cur.execute(fetch_for_upd_room_alloc)
            res = cur.fetchall()
            if res != []:
                print("<div style='display:none;'>data fetching successfully</div>")
                # print(res)
                print("<span><i class='fa-solid fa-xmark fa-2xl'></i></span>")
                print("<form class='catupform'>")
                for row in res:
                    print(f'''<div class="parent">
        <h2> Room Allocation</h2>
        <form enctype="multipart/form-data" method="post">
            
            <table>
                <tr>
                    
                    <td>
                        <!-- <label class="l_fixed" for="Id">Room ID </label> -->
                        <i class="fa-solid fa-id-card i1"></i>
                        <!-- <input required type="text" name="emp_id" id="id" value="" readonly> -->
                        <select name="" id="roomid1" readonly>
                            <option value="{row[0]}">{row[0]}</option>
                        </select>
                        <span> </span>
                    </td>
                    <td>
                        <label class="l_fixed" for="userid">User Id </label>
                        <i class="fa-solid fa-id-card i1"></i>
                        <input required type="text" name="emp_id" id="userid1" value="{row[1]}" >
                        <span> </span>
                    </td>
                    
                    <td>
                        <label class="l_fixed" for="dob">Check In</label>
                        <i class="fa-solid fa-calendar i1"></i>
                        <input required type="date" name="dob" id="checkin1" value="{row[2]}">
                        <span> </span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label class="l_fixed" for="dob">Check Out</label>
                        <i class="fa-solid fa-calendar i1"></i>
                        <input required type="date" name="dob" id="checkout1" value="{row[3]}">
                        <span> </span>
                    </td>
                    
                    <td>
                        <!-- <label class="l_move" for="f_name">Status</label> -->
                        <i class="fa-solid fa-chart-line i1"></i>
                        <select name="" id="status1">
                            <option value="{row[4]}">{row[4]}</option>
                            <option value="active">Active</option>
                            <option value="inactive">Inactive</option>
                        </select>
                        <span></span>
                    </td>
                    <td>
                        <div class="button">
                            <button id="save" type="submit" value="Save" style="background-color: rgb(0, 255, 0); color: black;"> <i
                                    class="fa-solid fa-arrow-up-from-bracket"></i> &nbsp; Submit </button>
                            <button type="reset" value="Reset" style="background-color: rgb(0, 208, 255); color: black;"><i
                                    class="fa-solid fa-rotate-left"></i> Reset </button>
                        </div>
                    </td>
                </tr>
            </table>
        </form>
    </div>''')
              
                print("</form>")
            else:
                print("no data available")
    except Exception as e:
        print(e)

elif(what == "savetheRoomAllocupdate"):
    try:
        roomid1 = f.getvalue("roomid1")
        userid1 = f.getvalue("userid1")
        checkin1 = f.getvalue("checkin1")
        checkout1 = f.getvalue("checkout1")
        status1 = f.getvalue("status1")

        print(roomid1,userid1,checkin1,checkout1,status1)
        
        if( roomid1 != None and userid1 != None and checkin1 != None and checkout1 != None and status1 != None):
            saveRoomAllocUpdate_query = f"update room_allocation SET userid = '{userid1}', checkin = '{checkin1}',checkout = '{checkout1}', status='{status1}' where roomid = '{roomid1}'"
            cur.execute(saveRoomAllocUpdate_query)
            con.commit()
            print("room allocation details successfully updated")
        else:
            print("no field should be empty")
    except Exception as e:
        print(e)

elif(what == "fetchFeeUpdate"):
    # print(what)
    try:
        userid = f.getvalue("userid")
        # print(userid + " have gotten")
        if(userid != None):
            fetch_fee_upd = f"select * from fee_details where userid='{userid}'"
            cur.execute(fetch_fee_upd)
            res = cur.fetchall()
            if res != []:
                print("<div style='display:none;'>data fetching successfully</div>")
                # print(res)
                print("<span><i class='fa-solid fa-xmark fa-2xl'></i></span>")
                for row in res:
                    print(f''' <div class="parent">
        <h2>Fee Details</h2>
        <form enctype="multipart/form-data" method="post">
            
            <table>
                <tr>
                    
                   
                    <td>
                        <label class="l_fixed" for="Id">User Id </label>
                        <i class="fa-solid fa-id-card i1"></i>
                        <input type="text" name="emp_id" id="userid1" value="{row[0]}" readonly>
                        <span> </span>
                    </td>
                    <td>
                        <label class="l_fixed" for="Id">Fee Amount</label>
                        <input required type="text" name="fee_amount" id="fee_amt1" value="{row[1]}" readonly>
                    </td>
                    
                    <td>
                        <label class="l_fixed" for="dob">Pay Date</label>
                        <i class="fa-solid fa-calendar i1"></i>
                        <input type="date" name="dob" id="paydate1" value="{row[2]}"> 
                        <span> </span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label class="l_fixed" >Pay Mode</label><br>
                        &nbsp; &nbsp; &nbsp;<input type="radio" name="pay_mode" value="CASH" id="Cash" checked> <label for="Cash">Cash</label> &nbsp; &nbsp;
                        &nbsp;<input type="radio" name="pay_mode" value="UPI" id="UPI" > <label for="UPI">UPI</label> &nbsp; &nbsp;
                        &nbsp;<input type="radio" name="pay_mode" value="NEFT" id="NEFT"> <label for="NEFT">NEFT</label>
                        <span> </span>
                    </td>
                    <td>
                        <label class="l_fixed" for="f_name">Month Name</label>
                        <i class="fa-solid fa-chart-line i1"></i>
                      
                        <select name="" id="month_name1">
                            <option value="{row[4]}">{row[4]}</option>
                            <option value="January">January</option>
                            <option value="February">February</option>
                            <option value="March">March</option>
                            <option value="April">April</option>
                            <option value="May">May</option>
                            <option value="June">June</option>
                            <option value="July">July</option>
                            <option value="August">August</option>
                            <option value="September">September</option>
                            <option value="October">October</option>
                            <option value="November">November</option>
                            <option value="December">December</option>
                        </select>
                        <span></span>
                    </td>
                    <td>
                        <label class="l_move" for="f_name">Status</label>
                        <i class="fa-solid fa-chart-line i1"></i>
                        <select id="status1">
                            <option value="{row[5]}">{row[5]}</option>
                            <option value="active">Success</option>
                            <option value="inactive">Failure</option>
                        </select>
                        <span></span>
                    </td>
                   
                </tr>
                <tr>
                    <td colspan="3">
                        <div class="button">
                            <button id="save" type="submit" value="Submit" style="background-color: rgb(0, 255, 0); color: black;"> <i
                                    class="fa-solid fa-arrow-up-from-bracket"></i> &nbsp; Submit </button>
                            <button type="reset" value="Reset" style="background-color: rgb(0, 208, 255); color: black;"><i
                                    class="fa-solid fa-rotate-left"></i> Reset </button>
                        </div>
                    </td>
                </tr>
            </table>
        </form>
    </div>''')
              
            else:
                print("no data available")
    except Exception as e:
        print(e)

elif(what == "savetheFeeUpdate"):
    try:
        userid1 = f.getvalue("userid1")
        fee_amt1 = f.getvalue("fee_amt1")
        paydate1 = f.getvalue("paydate1")
        paymode1 = f.getvalue("paymode1")
        month_name1 = f.getvalue("month_name1")
        status1 = f.getvalue("status1")

        print(userid1,fee_amt1,paydate1,paymode1,month_name1,status1)
        
        if( userid1 != None and fee_amt1 != None and paydate1 != None and paymode1 != None and month_name1 and status1 != None):
            saveFeeUpd_query = f"update fee_details SET pay_date = '{paydate1}', pay_mode = '{paymode1}',month_name = '{month_name1}', f_status='{status1}' where userid = '{userid1}'"
            cur.execute(saveFeeUpd_query)
            con.commit()
            print("fee details successfully updated")
        else:
            print("no field should be empty")
    except Exception as e:
        print(e)


elif(what == "fetchUserUpdate"):
    # print(what)
    try:
        userid = f.getvalue("userid")
        # print(userid + " have gotten")
        if(userid != None):
            fetch_user_upd = f"select * from user_info where userid='{userid}'"
            cur.execute(fetch_user_upd)
            res = cur.fetchall()
            if res != []:
                print("<div style='display:none;'>data fetching successfully</div>")
                # print(res)
                print("<span><i class='fa-solid fa-xmark fa-2xl'></i></span>")
                for row in res:
                    print(f'''<div class="parent">
        <h2>Update User Details Form </h2>
        <form enctype="multipart/form-data" method="post">

            <table>
                <tr>
                    <td>
                        <label class="l_fixed" for="id">User Id </label>
                        <i class="fa-solid fa-id-card i1"></i>
                        <input type="text" name="emp_id" id="id1" value="{row[0]}" readonly >
                        <span> </span>
                    </td>
                    <td>
                        <label class="l_move" for="name">Name</label>
                        <i class="fa-solid fa-user i1"></i>
                        <input type="text" id="name1" name="emp_name" value="{row[1]}">
                        <span> </span>
                    </td>
                    <td>
                        <label class="l_move" for="contact">Contact Number</label>
                        <i class="fa-solid fa-phone i1"></i>
                        <input type="text" name="contact" id="contact1" value="{row[2]}">
                        <span></span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label for="" class="l_fixed" style="left: 1rem;">Gender : </label> <br>
                        &nbsp; &nbsp; &nbsp;<input type="radio" name="gender" value="male" id="male" checked> <label
                            for="male">Male</label> &nbsp; &nbsp;
                        &nbsp;<input type="radio" name="gender" value="female" id="female"> <label
                            for="female">Female</label> &nbsp; &nbsp;
                        &nbsp;<input type="radio" name="gender" value="other" id="other"> <label
                            for="other">Other</label>
                    </td>
                    <td>
                        <label class="l_fixed" for="dob">Date Of Birth</label>
                        <i class="fa-solid fa-calendar i1"></i>
                        <input type="date" name="dob" id="dob1" value="{row[4]}">
                        <span> </span>
                    </td>
                    <td>
                        <select name="" id="bloodgrp1">
                            <option value="{row[5]}">{row[5]}</option>
                            <option value="0">O+</option>
                            <option value="0">O-</option>
                            <option value="0">A+</option>
                            <option value="0">A-</option>
                            <option value="0">B+</option>
                            <option value="0">B-</option>
                            <option value="0">AB+</option>
                            <option value="0">AB-</option>
                        </select>
                    </td>

                </tr>
                <tr>
                    <td>
                        <label class="l_move" for="f_name">Father's Name</label>
                        <i class="fa-solid fa-user i1"></i>
                        <input type="text" name="father_name" id="f_name1" value="{row[6]}">
                        <span></span>
                    </td>
                    <td>
                        <label class="l_move" for="m_name">Mother's Name</label>
                        <i class="fa-solid fa-user i1"></i>
                        <input type="text" name="father_name" id="m_name1" value="{row[7]}">
                        <span></span>
                    </td>
                    <td>
                        <label class="l_move" for="p_contact">Parent Contact Number</label>
                        <i class="fa-solid fa-phone i1"></i>
                        <input type="text" name="father_name" id="p_contact1" value="{row[8]}">
                        <span></span>
                    </td>

                </tr>
                <tr>

                    <td>
                        <label for="pic" class="l_fixed">Photo</label>
                        <input type="file" id="pic1"  name="emp_pic" style="padding-top: 0.8rem; padding-left: 1.5rem;" accept="image/*" readonly>
                    </td>
                    <td>
                        <label class="l_move" for="aadhar">Aadhar Number</label>
                        <i class="fa-solid fa-id-card i1"></i>
                        <input type="text" name="aadhar" maxlength="12" minlength="12" id="aadhar1" value="{row[10]}">
                        <span> </span>
                    </td>
                    <td>
                        <label class="l_move" for="street">Street</label>
                        <i class="fa-solid fa-street-view i1"></i>
                        <input type="text" name="street" id="street1" value="{row[11]}">
                        <span> </span>
                    </td>

                </tr>
                <tr>




                    <td>
                        <label class="l_move" for="dit">District, State</label>
                        <i class="fa-solid fa-building i1"></i>
                        <input type="text" name="dict" id="dit1" value="{row[12]}">
                        <span> </span>
                    </td>
                    <td>
                        <label class="l_move" for="pin">Pincode</label>
                        <i class="fa-solid fa-location-pin i1"></i>
                        <input type="text" name="pin" maxlength="6" minlength="6" id="pin1" value="{row[13]}">
                        <span> </span>
                    </td>


                    <td>
                        <label class="l_move" for="local_guard">Local Guardian </label>
                        <i class="fa-solid fa-user i1"></i>
                        <input type="text" name="father_name" id="local_guard1" value="{row[14]}">
                        <span></span>
                    </td>
                </tr>
                <tr>

                </tr>
                <td>
                    <label class="l_move" for="local_guard_contact">Local Guardian Number</label>
                    <i class="fa-solid fa-phone i1"></i>
                    <input type="text" name="father_name" id="local_guard_contact1" value="{row[15]}">
                    <span></span>
                </td>
                <td colspan="2">
                    <label class="l_move" for="local_guard_addr">Local Guardian Address</label>
                    <i class="fa-solid fa-map-location-dot i1"></i>
                    <input type="text" name="father_name" id="local_guard_addr1" value="{row[16]}">
                    <span></span>
                </td>



                <tr>
                    <td colspan="3">
                        <div class="button">
                            <button id="save" type="submit" value="Submit"
                                style="background-color: rgb(0, 255, 0); color: black;"> <i
                                    class="fa-solid fa-arrow-up-from-bracket"></i> &nbsp; Save </button>
                            <button type="reset" value="Reset"
                                style="background-color: rgb(0, 208, 255); color: black;"><i
                                    class="fa-solid fa-rotate-left"></i> Reset </button>
                        </div>
                    </td>
                </tr>
            </table>
        </form>
    </div>''')
              
            else:
                print("no data available")
    except Exception as e:
        print(e)

elif(what == "savetheUserUpdate"):
    try:
        user_id1 = f.getvalue("emp_id1")
        user_name1 = f.getvalue("emp_name1")
        user_contact1 = f.getvalue("emp_contact1")
        user_gender1 = f.getvalue("emp_gender1")
        user_dob1 = f.getvalue("emp_dob1")
        user_blood1 = f.getvalue("emp_blood1")
        user_father1 = f.getvalue("emp_father1")
        user_mother1 = f.getvalue("emp_mother1")
        user_par_contact1 = f.getvalue("emp_par_contact1")
        user_photo1 = f.getvalue("emp_photo1")
        user_aadhar1 = f.getvalue("emp_aadhar1")
        user_street1 = f.getvalue("emp_street1")
        user_dist_state1 = f.getvalue("emp_dist_state1")
        user_pincode1 = f.getvalue("emp_pincode1")
        user_local_guard1 = f.getvalue("emp_local_guard1")
        user_local_guard_cont1 = f.getvalue("emp_local_guard_cont1")
        user_local_guard_addr1 = f.getvalue("emp_local_guard_addr1")

        # print(user_id1,user_name1,user_contact1,user_dob1,user_gender1)
        # print(user_father1,user_blood1,user_mother1,user_par_contact1,user_aadhar1)
        # print(user_photo1)
        # print(user_street1,user_dist_state1,user_pincode1,user_local_guard1,user_local_guard_cont1,user_local_guard_addr1 )
        
        if( user_name1 != None and user_contact1 != None and user_dob1 != None
        and user_gender1 != None and user_dob1 != None and user_blood1 != None
        and user_father1 != None and user_mother1 != None and user_par_contact1 != None
        and user_aadhar1 != None and user_street1 != None 
        and user_dist_state1 != None and user_pincode1 != None and user_local_guard1 != None and
        user_local_guard_cont1 != None and user_local_guard_addr1 != None):
            
            saveUserUpd_query = f"update user_info SET username = '{user_name1}', user_cont = '{user_contact1}',user_gender = '{user_gender1}', user_dob='{user_dob1}', user_blood_grp='{user_blood1}', user_f_name='{user_father1}', user_m_name='{user_mother1}', user_p_contact='{user_par_contact1}', user_pic='{user_photo1}' , user_addhar='{user_aadhar1}', user_street='{user_street1}', user_dstate='{user_dist_state1}', user_pin='{user_pincode1}', user_local_guard='{user_local_guard1}' , user_local_guard_cont='{user_local_guard_cont1}', user_local_guard_add='{user_local_guard_addr1}' where userid = '{user_id1}'"
            cur.execute(saveUserUpd_query)
            con.commit()
            print("user details successfully updated")
        else:
            print("no field should be empty")
    except Exception as e:
        print(e)

# fetching data on click of search button or searching data
elif(what == "fetch_room_conditions"):
    # print(d)
    try:
        room_no = f.getvalue("room_no")
        roomtype = f.getvalue("roomtype")
        total_bed = f.getvalue("total_bed")
        status = f.getvalue("status")
        

        # Construct conditions for the SQL query
        conditions = []
        if room_no != None:
            conditions.append(f"room_no = '{room_no}'")
        if roomtype is not None:
            conditions.append(f"room_type = '{roomtype}'")
        if total_bed is not None:
            conditions.append(f"total_bed <= '{total_bed}'")
        if status is not None:
            conditions.append(f"status = '{status}'")
        

        # Construct the SQL query
        fetch_room_query = "SELECT * FROM room_details"
        if conditions:
            fetch_room_query += " WHERE " + " AND ".join(conditions)
       
        # print(fetch_user_query)


        cur.execute(fetch_room_query)
        srr = cur.fetchall()
        if srr != []:
            # print("<br>yes")
            print("<table class='tab'>")
            print("<tr>")
            print("<th>Room No</th>")
            print("<th>Room Type</th>")
            print("<th>Total Bed</th>")
            print("<th>Status Gender</th>")
            print("<th colspan='2' style='text-align:center;'>action</th>")
            print("</tr>")
            for row in srr:
                # print(row)
                print("<tr>")
                print(f'<td>{row[0]}</td>')
                print(f'<td>{row[1]}</td>')
                print(f'<td>{row[2]}</td>')
                print(f'<td>{row[3]}</td>')
                
                print(f"<td><i class='fa-solid fa-pen-to-square fa-xl edit'  id=\"edit\" ></i></td>")
                print(f"<td><i class='fa-solid fa-trash-can fa-xl del'></i></td>")
                print("</tr>")
            print("</table>")
            print("<p style='display:none;'>room details fetched successfully</p>")
        else:
            # print("no")
            print("no data available")
    except Exception as e:
        print(e)

# deleting product category on click of delete button
elif(what == "deleteroom"):
    try:
        roomid = f.getvalue("roomno")
        delete_room_query = f"delete from room_details where room_no = '{roomid}'"
        print(delete_room_query)
        cur.execute(delete_room_query)
        con.commit()
        print("room deleted successfully")
    except Exception as e:
        print(e)


elif(what == "fetchForRoomUpdate"):
    # print(what)
    try:
        roomid = f.getvalue("roomid")
        # print(userid + " have gotten")
        if(roomid != None):
            fetch_for_upd_room = f"select * from room_details where room_no='{roomid}'"
            # print(fetch_for_upd_room)
            cur.execute(fetch_for_upd_room)
            res = cur.fetchall()
            if res != []:
                print("<div style='display:none;'>data fetching successfully</div>")
                # print(res)
                print("<span><i class='fa-solid fa-xmark fa-2xl'></i></span>")
                for row in res:
                    print(f''' ''')
              
            else:
                print("no data available")
    except Exception as e:
        print(e)

elif(what == "savetheRoomupdate"):
    try:
        room_no = f.getvalue("room_no")
        room_type = f.getvalue("room_type")
        t_bed = f.getvalue("t_bed1")
        status = f.getvalue("status1")

        print(room_no,room_type,t_bed,status)
        
        if( room_type != None and t_bed != None and status != None):
            saveRoomUpdate_query = f"update room_details SET room_type = '{room_type}', total_bed = '{t_bed}',status = '{status}' where room_no = '{room_no}'"
            cur.execute(saveRoomUpdate_query)
            con.commit()
            print("room details successfully updated")
        else:
            print("no field should be empty")
    except Exception as e:
        print(e)

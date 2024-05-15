#! C:\Users\ASUS\AppData\Local\Programs\Python\Python312\python.exe

print("Content-Type: text/html\r\n\r\n")
import cgi
import mysql.connector
con=mysql.connector.connect(host='localhost', user='hostel', passwd='data73063',database='hostel')
t=con.cursor()
try:
    f=cgi.FieldStorage()
    cond=f.getvalue('cond')
    if(cond=='entry'):
        t.execute('select * from signup where email="'+str(f.getvalue('t2'))+'"')
        if(t.fetchall()==[]):
                t.execute("insert into signup(name,email,sec_q,ans,pass) values(%s,%s,%s,%s,%s)",(f.getvalue('t1'),f.getvalue('t2'),f.getvalue('t3'),f.getvalue('t4'),f.getvalue('t5')))
                con.commit()
                print("Successfully Created!!&&0")
        else:
            print('Already Email Exists!!')
    elif(cond=='login'):
        t.execute('select name,email from signup where email="'+str(f.getvalue('t1'))+'" and pass="'+str(f.getvalue('t2'))+'"')
        rs=t.fetchall()
        if(rs!=[]):
            print(rs[0][0],rs[0][1],sep="&&")
        else:
            print(0)
    elif(cond=='forgot'):
        t.execute('select * from signup where email="'+str(f.getvalue('t1'))+'" and sec_q="'+str(f.getvalue('t4'))+'" and ans="'+str(f.getvalue('t3'))+'"')
        if(t.fetchall()!=[]):
            t.execute('update signup set pass="'+str(f.getvalue('t2'))+'" where email="'+str(f.getvalue('t1'))+'"')
            con.commit()
            print('Password Updated Succesfully!!&&0')
        else:
            print('Please Enter Correct Cerenditals!!')
    elif(cond=='profile_run'):
        t.execute('select * from profile where email="'+str(f.getvalue('t1'))+'"')
        rs=t.fetchall()
        if(rs!=[]):
            for a in rs:
                for i in a:
                    print(str(i)+'&&')
    elif(cond=='update'):
        t.execute('select * from profile where email="'+str(f.getvalue('t2'))+'"')
        if(t.fetchall()==[]):
            t.execute("insert into profile(name,email,cont,dob,gender,stat,dist,pin,loaction,about) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(f.getvalue('t1'),f.getvalue('t2'),f.getvalue('t3'),f.getvalue('t4'),f.getvalue('t5'),f.getvalue('t6'),f.getvalue('t7'),f.getvalue('t8'),f.getvalue('t9'),f.getvalue('t10')))
        else:
            t.execute('update profile set name="'+str(f.getvalue('t1'))+'",cont="'+str(f.getvalue('t3'))+'",dob="'+str(f.getvalue('t4'))+'",gender="'+str(f.getvalue('t5'))+'",stat="'+str(f.getvalue('t6'))+'",dist="'+str(f.getvalue('t7'))+'",pin="'+str(f.getvalue('t8'))+'",loaction="'+str(f.getvalue('t9'))+'",about="'+str(f.getvalue('t10'))+'" where email="'+f.getvalue('t2')+'"')
        con.commit()
        print('Profile Updated Succesfully!!&&0')
except Exception as e:
    print("Unsuccesss",e)
finally:
    if con.is_connected:
        con.close()
        t.close()
import streamlit as st
import mysql.connector 
mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="", 
    database="vvvv"
)
c = mydb.cursor()

def create_table1(): 
    c.execute('create table if not exists Report (regno text,bookno text,issuedate text,staffid text)')
def create_table2(): 
    c.execute('create table if not exists Staff (staffid text,staffname text,loginid text)')
def create_table3(): 
    c.execute('create table if not exists Reader (userid text,email text,readername text,staffid text)')
def create_table4(): 
    c.execute('create table if not exists Book (ISBN text,title text,category text,price text,staffid text,publisherid text,userid text)')
def create_table5(): 
    c.execute('create table if not exists Publisher (publisherid text,publishername text,yearofpublication text)')
def create_table6(): 
    c.execute('create table if not exists Authentication (loginid text,password text)')
def create_table7(): 
    c.execute('create table if not exists Readerphone (userid text,phoneno text)')

def add_data1(regno,bookno,issuedate,staffid): 
    c.execute('insert into Report values (%s,%s,%s,%s)',(regno,bookno,issuedate,staffid)) 
    mydb.commit()
def add_data2(staffid,staffname,loginid): 
    c.execute('insert into Staff values (%s,%s,%s)',(staffid,staffname,loginid)) 
    mydb.commit()
def add_data3(userid,email,readername,staffid): 
    c.execute('insert into Reader values (%s,%s,%s,%s)',(userid,email,readername,staffid)) 
    mydb.commit()
def add_data4(ISBN,title,category,price,staffid,publisherid,userid): 
    c.execute('insert into Book values (%s,%s,%s,%s,%s,%s,%s)',(ISBN,title,category,price,staffid,publisherid,userid)) 
    mydb.commit()
def add_data5(publisherid,publishername,yearofpublication): 
    c.execute('insert into Publisher values (%s,%s,%s)',(publisherid,publishername,yearofpublication)) 
    mydb.commit()
def add_data6(loginid,password): 
    c.execute('insert into Authentication values (%s,%s)',(loginid,password)) 
    mydb.commit()
def add_data7(userid,phoneno): 
    c.execute('insert into Readerphone values (%s,%s)',(userid,phoneno)) 
    mydb.commit()

def view_all_data1(): 
    c.execute('select * from Report') 
    data = c.fetchall()
    return data
def view_all_data2(): 
    c.execute('select * from Staff') 
    data = c.fetchall()
    return data
def view_all_data3(): 
    c.execute('select * from Reader') 
    data = c.fetchall()
    return data
def view_all_data4(): 
    c.execute('select * from Book') 
    data = c.fetchall()
    return data
def view_all_data5(): 
    c.execute('SELECT * FROM Publisher') 
    data = c.fetchall()
    return data
def view_all_data6(): 
    c.execute('SELECT * FROM Authentication') 
    data = c.fetchall()
    return data
def view_all_data7(): 
    c.execute('SELECT * FROM Readerphone') 
    data = c.fetchall()
    return data

def view_only_regno(): 
    c.execute('select regno from Report') 
    data = c.fetchall()
    return data
def view_only_staffid(): 
    c.execute('select staffid from Staff') 
    data = c.fetchall()
    return data
def view_only_userid1(): 
    c.execute('select userid from Reader') 
    data = c.fetchall()
    return data
def view_only_ISBN(): 
    c.execute('select ISBN from Book') 
    data = c.fetchall()
    return data
def view_only_publisherid(): 
    c.execute('select publisherid from Publisher') 
    data = c.fetchall()
    return data
def view_only_loginid(): 
    c.execute('select loginid from Authentication') 
    data = c.fetchall()
    return data
def view_only_userid2(): 
    c.execute('select userid from Readerphone') 
    data = c.fetchall()
    return data

def get_report(regno): 
    c.execute('select * from Report where regno = "{}"'.format(regno)) 
    data = c.fetchall()
    return data
def get_staff(staffid): 
    c.execute('select * from Staff where staffid = "{}"'.format(staffid)) 
    data = c.fetchall()
    return data
def get_reader(userid): 
    c.execute('select * from Reader where userid = "{}"'.format(userid)) 
    data = c.fetchall()
    return data
def get_book(ISBN): 
    c.execute('select * from Book where ISBN = "{}"'.format(ISBN))  
    data = c.fetchall()
    return data
def get_publisher(publisherid): 
    c.execute('select * from Publisher where publisherid = "{}"'.format(publisherid)) 
    data = c.fetchall()
    return data
def get_authentication(loginid): 
    c.execute('select * from Authentication where loginid = "{}"'.format(loginid)) 
    data = c.fetchall()
    return data
def get_readerphone(userid): 
    c.execute('select * from Readerphone where userid = "{}"'.format(userid)) 
    data = c.fetchall()
    return data

def edit_report_data(new_regno,new_bookno,new_issuedate,new_staffid,regno,bookno,issuedate,staffid): 
    c.execute("update Report set regno = %s,bookno = %s,issuedate = %s,staffid = %s where regno = %s and bookno = %s and issuedate = %s and staffid = %s",(new_regno,new_bookno,new_issuedate,new_staffid,regno,bookno,issuedate,staffid))
    mydb.commit()
    data = c.fetchall()
    return data
def edit_staff_data(new_staffid,new_staffname,new_loginid,staffid,staffname,loginid): 
    c.execute("update Staff set staffid = %s,staffname = %s,loginid = %s where staffid = %s and staffname = %s and loginid = %s",(new_staffid,new_staffname,new_loginid,staffid,staffname,loginid))
    mydb.commit()
    data = c.fetchall()
    return data
def edit_reader_data(new_userid,new_email,new_readername,new_staffid,userid,email,readername,staffid): 
    c.execute("update Reader set userid = %s,email = %s,readername = %s,staffid = %s where userid = %s and email = %s and readername = %s and staffid = %s",(new_userid,new_email,new_readername,new_staffid,userid,email,readername,staffid))
    mydb.commit()
    data = c.fetchall()
    return data
def edit_book_data(new_ISBN,new_title,new_category,new_price,new_staffid,new_publisherid,new_userid,ISBN,title,category,price,staffid,publisherid,userid): 
    c.execute("update Book set ISBN = %s,title = %s,category = %s,price = %s,staffid = %s,publisherid = %s,userid = %s where ISBN = %s and title = %s and category = %s and price = %s and staffid = %s and publisherid = %s and userid = %s",(new_ISBN,new_title,new_category,new_price,new_staffid,new_publisherid,new_userid,ISBN,title,category,price,staffid,publisherid,userid))
    mydb.commit()
    data = c.fetchall()
    return data
def edit_publisher_data(new_publisherid,new_publishername,new_yearofpublication,publisherid,publishername,yearofpublication): 
    c.execute("update Publisher set publisherid = %s,publishername = %s,yearofpublication = %s where publisherid = %s and publishername = %s and yearofpublication = %s",(new_publisherid,new_publishername,new_yearofpublication,publisherid,publishername,yearofpublication))
    mydb.commit()
    data = c.fetchall()
    return data
def edit_authentication_data(new_loginid,new_password,loginid,password): 
    c.execute("update Authentication set loginid = %s,password = %s where loginid = %s and password = %s",(new_loginid,new_password,loginid,password))
    mydb.commit()
    data = c.fetchall()
    return data
def edit_readerphone_data(new_userid,new_phoneno,userid,phoneno): 
    c.execute("update Readerphone set userid = %s,phoneno = %s where userid = %s and phoneno = %s",(new_userid,new_phoneno,userid,phoneno))
    mydb.commit()
    data = c.fetchall()
    return data

def delete_data1(regno): 
    c.execute('delete from Report where regno = "{}"'.format(regno)) 
    mydb.commit()
def delete_data2(staffid): 
    c.execute('delete from Staff where staffid = "{}"'.format(staffid)) 
    mydb.commit()
def delete_data3(userid): 
    c.execute('delete from Reader where userid = "{}"'.format(userid)) 
    mydb.commit()
def delete_data4(ISBN): 
    c.execute('delete from Book where ISBN = "{}"'.format(ISBN)) 
    mydb.commit()
def delete_data5(publisherid): 
    c.execute('delete from Publisher where publisherid = "{}"'.format(publisherid)) 
    mydb.commit()
def delete_data6(loginid): 
    c.execute('delete from Authentication where loginid = "{}"'.format(loginid)) 
    mydb.commit()
def delete_data7(userid): 
    c.execute('delete from Readerphone where userid = "{}"'.format(userid)) 
    mydb.commit()

def run_sql(query):
    c.execute(query)
    data = c.fetchall()
    return data



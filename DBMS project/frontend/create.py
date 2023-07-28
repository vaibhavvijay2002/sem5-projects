import streamlit as st
from database import add_data1,add_data2,add_data3,add_data4,add_data5,add_data6,add_data7
def create1():
    col1,col2 = st.columns(2)
    with col1:
        regno = st.text_input("regno:")
        bookno = st.text_input("bookno:")
    with col2:
        issuedate = st.text_input("issuedate:")
        staffid = st.text_input("staffid:")
    if st.button("add Report"):
        add_data1(regno,bookno,issuedate,staffid)
        st.success("successfully added Report with regno: {}".format(regno))

def create2():
    staffid = st.text_input("staffid:")
    staffname = st.text_input("staffname:")
    loginid = st.text_input("loginid:")
    if st.button("add Staff"):
        add_data2(staffid,staffname,loginid)
        st.success("successfully added Staff with staffid: {}".format(staffid))

def create3():
    col1,col2 = st.columns(2)
    with col1:
        userid = st.text_input("userid:")
        email = st.text_input("email:")
    with col2:
        readername = st.text_input("readername:")
        staffid = st.text_input("staffid:")
    if st.button("add Reader"):
        add_data3(userid,email,readername,staffid)
        st.success("successfully added Reader with userid: {}".format(userid))

def create4():
    col1,col2,col3 = st.columns(3)
    with col1:
        ISBN = st.text_input("ISBN:")
        title = st.text_input("title:")
    with col2:
        category = st.text_input("category:")
        price = st.text_input("price:")
    with col3:
        staffid = st.text_input("staffid")
        publisherid = st.text_input("publisherid:")
        userid = st.text_input("userid:")
    if st.button("add Book"):
        add_data4(ISBN,title,category,price,staffid,publisherid,userid)
        st.success("successfully added Book with ISBN: {}".format(ISBN))

def create5():
    publisherid = st.text_input("publisherid:")
    publishername = st.text_input("publishername:")
    yearofpublication = st.text_input("yearofpublication:")
    if st.button("add Publisher"):
        add_data5(publisherid,publishername,yearofpublication)
        st.success("successfully added Publisher with publisherid: {}".format(publisherid))

def create6():
    loginid = st.text_input("loginid:")
    password = st.text_input("password:")
    if st.button("add Authentication"):
        add_data6(loginid,password)
        st.success("successfully added Authentication with loginid: {}".format(loginid))

def create7():
    userid = st.text_input("userid:")
    phoneno = st.text_input("phoneno:")
    if st.button("add Readerphone"):
        add_data7(userid,phoneno)
        st.success("successfully added Readerphone with userid: {}".format(userid))
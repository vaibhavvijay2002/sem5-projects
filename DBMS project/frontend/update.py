import pandas as pd
import streamlit as st
from database import view_all_data1,view_all_data2,view_all_data3,view_all_data4,view_all_data5,view_all_data6,view_all_data7,view_only_regno,view_only_staffid,view_only_userid1,view_only_ISBN,view_only_publisherid,view_only_loginid,view_only_userid2,get_report,get_staff,get_reader,get_book,get_publisher,get_authentication,get_readerphone,edit_report_data,edit_staff_data,edit_reader_data,edit_book_data,edit_publisher_data,edit_authentication_data,edit_readerphone_data
def update1():
    result = view_all_data1()
    df = pd.DataFrame(result,columns = ['regno','bookno','issuedate','staffid']) 
    with st.expander("current data"):
        st.dataframe(df)
    list_of_reports = [i[0] for i in view_only_regno()] 
    selected_report = st.selectbox("select regno to edit",list_of_reports) 
    selected_result = get_report(selected_report)
    if selected_result:
        regno = selected_result[0][0]
        bookno = selected_result[0][1]
        issuedate = selected_result[0][2]
        staffid = selected_result[0][3]
        col1,col2 = st.columns(2)
        with col1:
            new_regno = st.text_input("regno:")
            new_bookno = st.text_input("bookno:")
        with col2:
            new_issuedate = st.text_input("issuedate:")
            new_staffid = st.text_input("staffid:")
        if st.button("update Report data"):
            edit_report_data(new_regno,new_bookno,new_issuedate,new_staffid,regno,bookno,issuedate,staffid)
            st.success("successfully updated Report with regno: {}".format(regno))
    new_result = view_all_data1()
    df2 = pd.DataFrame(new_result,columns = ['regno','bookno','issuedate','staffid']) 
    with st.expander("updated data"):
        st.dataframe(df2)

def update2():
    result = view_all_data2()
    df = pd.DataFrame(result,columns = ['staffid','staffname','loginid']) 
    with st.expander("current data"):
        st.dataframe(df)
    list_of_staffs = [i[0] for i in view_only_staffid()] 
    selected_staff = st.selectbox("select staffid to edit",list_of_staffs)  
    selected_result = get_staff(selected_staff)
    if selected_result:
        staffid = selected_result[0][0]
        staffname = selected_result[0][1]
        loginid = selected_result[0][2]
        new_staffid = st.text_input("staffid:")
        new_staffname = st.text_input("staffname:")
        new_loginid = st.text_input("loginid:")
        if st.button("update Staff data"):
            edit_staff_data(new_staffid,new_staffname,new_loginid,staffid,staffname,loginid)
            st.success("successfully updated Staff with staffid: {}".format(staffid))
    new_result = view_all_data2()
    df2 = pd.DataFrame(new_result,columns = ['staffid','staffname','loginid']) 
    with st.expander("updated data"):
        st.dataframe(df2)

def update3():
    result = view_all_data3()
    df = pd.DataFrame(result,columns = ['userid','email','readername','staffid']) 
    with st.expander("current data"):
        st.dataframe(df)
    list_of_readers = [i[0] for i in view_only_userid1()] 
    selected_reader = st.selectbox("select userid to edit",list_of_readers)
    selected_result = get_reader(selected_reader)
    if selected_result:
        userid = selected_result[0][0]
        email = selected_result[0][1]
        readername = selected_result[0][2]
        staffid = selected_result[0][3]
        col1,col2 = st.columns(2)
        with col1:
            new_userid = st.text_input("userid:")
            new_email = st.text_input("email:")
        with col2:
            new_readername = st.text_input("readername:")
            new_staffid = st.text_input("staffid:")
        if st.button("update Reader data"):
            edit_reader_data(new_userid,new_email,new_readername,new_staffid,userid,email,readername,staffid)
            st.success("successfully updated Reader with userid: {}".format(userid))
    new_result = view_all_data3()
    df2 = pd.DataFrame(new_result,columns = ['userid','email','readername','staffid']) 
    with st.expander("updated data"):
        st.dataframe(df2)

def update4():
    result = view_all_data4()
    df = pd.DataFrame(result,columns = ['ISBN','title','category','price','staffid','publisherid','userid']) 
    with st.expander("current data"):
        st.dataframe(df)
    list_of_books = [i[0] for i in view_only_ISBN()] 
    selected_book = st.selectbox("select ISBN to edit",list_of_books) 
    selected_result = get_book(selected_book)
    if selected_result:
        ISBN = selected_result[0][0]
        title = selected_result[0][1]
        category = selected_result[0][2]
        price = selected_result[0][3]
        staffid = selected_result[0][4]
        publisherid = selected_result[0][5]
        userid = selected_result[0][6]
        col1,col2,col3 = st.columns(3)
        with col1:
            new_ISBN = st.text_input("ISBN:")
            new_title = st.text_input("title:")
        with col2:
            new_category = st.text_input("category:")
            new_price = st.text_input("price:")
        with col3:
            new_staffid = st.text_input("staffid")
            new_publisherid = st.text_input("publisherid:")
            new_userid = st.text_input("userid:")
        if st.button("update Book data"):
            edit_book_data(new_ISBN,new_title,new_category,new_price,new_staffid,new_publisherid,new_userid,ISBN,title,category,price,staffid,publisherid,userid)
            st.success("successfully updated Book with ISBN: {}".format(ISBN))
    new_result = view_all_data4()
    df2 = pd.DataFrame(new_result,columns = ['ISBN','title','category','price','staffid','publisherid','userid']) 
    with st.expander("updated data"):
        st.dataframe(df2)

def update5():
    result = view_all_data5()
    df = pd.DataFrame(result,columns = ['publisherid','publishername','yearofpublication']) 
    with st.expander("current data"):
        st.dataframe(df)
    list_of_publishers = [i[0] for i in view_only_publisherid()] 
    selected_publisher = st.selectbox("select publisherid to edit",list_of_publishers)  
    selected_result = get_publisher(selected_publisher)
    if selected_result:
        publisherid = selected_result[0][0]
        publishername = selected_result[0][1]
        yearofpublication = selected_result[0][2]
        new_publisherid = st.text_input("publisherid:")
        new_publishername = st.text_input("publishername:")
        new_yearofpublication = st.text_input("yearofpublication:")
        if st.button("update Publisher data"):
            edit_publisher_data(new_publisherid,new_publishername,new_yearofpublication,publisherid,publishername,yearofpublication)
            st.success("successfully updated Publisher with publisherid: {}".format(publisherid))
    new_result = view_all_data5()
    df2 = pd.DataFrame(new_result,columns = ['publisherid','publishername','yearofpublication']) 
    with st.expander("updated data"):
        st.dataframe(df2)

def update6():
    result = view_all_data6()
    df = pd.DataFrame(result,columns = ['loginid','password']) 
    with st.expander("current data"):
        st.dataframe(df)
    list_of_authentications = [i[0] for i in view_only_loginid()] 
    selected_authentication = st.selectbox("select loginid to edit",list_of_authentications) 
    selected_result = get_authentication(selected_authentication)
    if selected_result:
        loginid = selected_result[0][0]
        password = selected_result[0][1]
        new_loginid = st.text_input("loginid:")
        new_password = st.text_input("password:")
        if st.button("update Authentication data"):
            edit_authentication_data(new_loginid,new_password,loginid,password)
            st.success("successfully updated Authentication with loginid: {}".format(loginid))
    new_result = view_all_data6()
    df2 = pd.DataFrame(new_result,columns = ['loginid','password']) 
    with st.expander("updated data"):
        st.dataframe(df2)

def update7():
    result = view_all_data7()
    df = pd.DataFrame(result,columns = ['userid','phoneno']) 
    with st.expander("current data"):
        st.dataframe(df)
    list_of_readerphones = [i[0] for i in view_only_userid2()] 
    selected_readerphone = st.selectbox("select userid to edit",list_of_readerphones) 
    selected_result = get_readerphone(selected_readerphone)
    if selected_result:
        userid = selected_result[0][0]
        phoneno = selected_result[0][1]
        new_userid = st.text_input("userid:")
        new_phoneno = st.text_input("phoneno:")
        if st.button("update Readerphone data"):
            edit_readerphone_data(new_userid,new_phoneno,userid,phoneno)
            st.success("successfully updated Readerphone with userid: {}".format(userid))
    new_result = view_all_data7()
    df2 = pd.DataFrame(new_result,columns = ['userid','phoneno']) 
    with st.expander("updated data"):
        st.dataframe(df2)
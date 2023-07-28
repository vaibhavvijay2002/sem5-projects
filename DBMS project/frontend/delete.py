import pandas as pd 
import streamlit as st
from database import view_all_data1,view_all_data2,view_all_data3,view_all_data4,view_all_data5,view_all_data6,view_all_data7,view_only_regno,view_only_staffid,view_only_userid1,view_only_ISBN,view_only_publisherid,view_only_loginid,view_only_userid2,delete_data1,delete_data2,delete_data3,delete_data4,delete_data5,delete_data6,delete_data7
def delete1():
    result = view_all_data1()
    df = pd.DataFrame(result,columns = ['regno','bookno','issuedate','staffid']) 
    with st.expander("current data"):
        st.dataframe(df)
    list_of_reports = [i[0] for i in view_only_regno()] 
    selected_report = st.selectbox("select regno to delete",list_of_reports) 
    st.warning("confirm to delete Report with regno: {}".format(selected_report)) 
    if st.button("delete Report"):
        delete_data1(selected_report)
        st.success("Report has been deleted successfully")
    new_result = view_all_data1()
    df2 = pd.DataFrame(new_result,columns = ['regno','bookno','issuedate','staffid']) 
    with st.expander("updated data"):
        st.dataframe(df2)

def delete2():
    result = view_all_data2()
    df = pd.DataFrame(result,columns = ['staffid','staffname','loginid']) 
    with st.expander("current data"):
        st.dataframe(df)
    list_of_staffs = [i[0] for i in view_only_staffid()] 
    selected_staff = st.selectbox("select staffid to delete",list_of_staffs) 
    st.warning("confirm to delete Staff with staffid: {}".format(selected_staff)) 
    if st.button("delete Staff"):
        delete_data2(selected_staff)
        st.success("Staff has been deleted successfully")
    new_result = view_all_data2()
    df2 = pd.DataFrame(new_result,columns = ['staffid','staffname','loginid']) 
    with st.expander("updated data"):
        st.dataframe(df2)

def delete3():
    result = view_all_data3()
    df = pd.DataFrame(result,columns = ['userid','email','readername','staffid']) 
    with st.expander("current data"):
        st.dataframe(df)
    list_of_readers = [i[0] for i in view_only_userid1()] 
    selected_reader = st.selectbox("select userid to delete",list_of_readers) 
    st.warning("confirm to delete Reader with userid: {}".format(selected_reader)) 
    if st.button("delete Reader"):
        delete_data3(selected_reader)
        st.success("Reader has been deleted successfully")
    new_result = view_all_data3()
    df2 = pd.DataFrame(new_result,columns = ['userid','email','readername','staffid']) 
    with st.expander("updated data"):
        st.dataframe(df2)

def delete4():
    result = view_all_data4()
    df = pd.DataFrame(result,columns = ['ISBN','title','category','price','staffid','publisherid','userid']) 
    with st.expander("current data"):
        st.dataframe(df)
    list_of_books = [i[0] for i in view_only_ISBN()] 
    selected_book = st.selectbox("select ISBN to delete",list_of_books) 
    st.warning("confirm to delete Book with ISBN: {}".format(selected_book)) 
    if st.button("delete Book"):
        delete_data4(selected_book)
        st.success("Book has been deleted successfully")
    new_result = view_all_data4()
    df2 = pd.DataFrame(new_result,columns = ['ISBN','title','category','price','staffid','publisherid','userid']) 
    with st.expander("updated data"):
        st.dataframe(df2)

def delete5():
    result = view_all_data5()
    df = pd.DataFrame(result,columns = ['publisherid','publishername','yearofpublication']) 
    with st.expander("current data"):
        st.dataframe(df)
    list_of_publishers = [i[0] for i in view_only_publisherid()] 
    selected_publisher = st.selectbox("select publisherid to delete",list_of_publishers) 
    st.warning("confirm to delete Publisher with publisherid: {}".format(selected_publisher)) 
    if st.button("delete Publisher"):
        delete_data5(selected_publisher)
        st.success("Publisher has been deleted successfully")
    new_result = view_all_data5()
    df2 = pd.DataFrame(new_result,columns = ['publisherid','publishername','yearofpublication']) 
    with st.expander("updated data"):
        st.dataframe(df2)

def delete6():
    result = view_all_data6()
    df = pd.DataFrame(result,columns = ['loginid','password']) 
    with st.expander("current data"):
        st.dataframe(df)
    list_of_authentications = [i[0] for i in view_only_loginid()] 
    selected_authentication = st.selectbox("select loginid to delete",list_of_authentications) 
    st.warning("confirm to delete Authentication with loginid: {}".format(selected_authentication)) 
    if st.button("delete Authentication"):
        delete_data6(selected_authentication)
        st.success("Authentication has been deleted successfully")
    new_result = view_all_data6()
    df2 = pd.DataFrame(new_result,columns = ['loginid','password']) 
    with st.expander("updated data"):
        st.dataframe(df2)

def delete7():
    result = view_all_data7()
    df = pd.DataFrame(result,columns = ['userid','phoneno']) 
    with st.expander("current data"):
        st.dataframe(df)
    list_of_readerphones = [i[0] for i in view_only_userid2()] 
    selected_readerphone = st.selectbox("select userid to delete",list_of_readerphones) 
    st.warning("confirm to delete Readerphone with userid: {}".format(selected_readerphone)) 
    if st.button("delete Readerphone"):
        delete_data7(selected_readerphone)
        st.success("Readerphone has been deleted successfully")
    new_result = view_all_data7()
    df2 = pd.DataFrame(new_result,columns = ['userid','phoneno']) 
    with st.expander("updated data"):
        st.dataframe(df2)

import streamlit as st
from create import create1,create2,create3,create4,create5,create6,create7
from database import create_table1,create_table2,create_table3,create_table4,create_table5,create_table6,create_table7
from delete import delete1,delete2,delete3,delete4,delete5,delete6,delete7
from read import read1,read2,read3,read4,read5,read6,read7
from update import update1,update2,update3,update4,update5,update6,update7
from query import custom_run

def main():
   st.title("Library Management System")
   st.subheader("By Vaibhav Vijay (PES1UG20CS479)")
   tables = ["Report","Staff","Reader","Book","Publisher","Authentication","Readerphone","Custom Run Query"]
   operations = ["Add","View","Edit","Remove"]
   choice1 = st.sidebar.selectbox("Table",tables)
   if choice1 != "Custom Run Query":
      choice2 = st.sidebar.selectbox(choice1,operations)
   create_table1()
   create_table2()
   create_table3()
   create_table4()
   create_table5()
   create_table6()
   create_table7()
   if choice1 == "Report" and choice2 == "Add":
      st.subheader("enter Report details")
      create1()
   elif choice1 == "Report" and choice2 == "View":
      st.subheader("view Report details")
      read1()
   elif choice1 == "Report" and choice2 == "Edit":
      st.subheader("update Report details")
      update1()
   elif choice1 == "Report" and choice2 == "Remove":
      st.subheader("delete Report details")
      delete1()
   elif choice1 == "Staff" and choice2 == "Add":
      st.subheader("enter Staff details:")
      create2()
   elif choice1 == "Staff" and choice2 == "View":
      st.subheader("view Staff details")
      read2()
   elif choice1 == "Staff" and choice2 == "Edit":
      st.subheader("update Staff details")
      update2()
   elif choice1 == "Staff" and choice2 == "Remove":
      st.subheader("delete Staff details")
      delete2()
   elif choice1 == "Reader" and choice2 == "Add":
      st.subheader("enter Reader details:")
      create3()
   elif choice1 == "Reader" and choice2 == "View":
      st.subheader("view Reader details")
      read3()
   elif choice1 == "Reader" and choice2 == "Edit":
      st.subheader("update Reader details")
      update3()
   elif choice1 == "Reader" and choice2 == "Remove":
      st.subheader("delete Reader details")
      delete3()
   elif choice1 == "Book" and choice2 == "Add":
      st.subheader("enter Book details:")
      create4()
   elif choice1 == "Book" and choice2 == "View":
      st.subheader("view Book details")
      read4()
   elif choice1 == "Book" and choice2 == "Edit":
      st.subheader("update Book details")
      update4()
   elif choice1 == "Book" and choice2 == "Remove":
      st.subheader("delete Book details")
      delete4()
   elif choice1 == "Publisher" and choice2 == "Add":
      st.subheader("enter Publisher details:")
      create5()
   elif choice1 == "Publisher" and choice2 == "View":
      st.subheader("view Publisher details")
      read5()
   elif choice1 == "Publisher" and choice2 == "Edit":
      st.subheader("update Publisher details")
      update5()
   elif choice1 == "Publisher" and choice2 == "Remove":
      st.subheader("delete Publisher details")
      delete5()
   elif choice1 == "Authentication" and choice2 == "Add":
      st.subheader("enter Authentication details:")
      create6()
   elif choice1 == "Authentication" and choice2 == "View":
      st.subheader("view Authentication details")
      read6()
   elif choice1 == "Authentication" and choice2 == "Edit":
      st.subheader("update Authentication details")
      update6()
   elif choice1 == "Authentication" and choice2 == "Remove":
      st.subheader("delete Authentication details")
      delete6()
   elif choice1 == "Readerphone" and choice2 == "Add":
      st.subheader("enter Readerphone details:")
      create7()
   elif choice1 == "Readerphone" and choice2 == "View":
      st.subheader("view Readerphone details")
      read7()
   elif choice1 == "Readerphone" and choice2 == "Edit":
      st.subheader("update Readerphone details")
      update7()
   elif choice1 == "Readerphone" and choice2 == "Remove":
      st.subheader("delete Readerphone details")
      delete7()
   elif choice1 == "Custom Run Query":
      st.subheader("run sql queries")
      custom_run()
      
if __name__ == '__main__':
   main()
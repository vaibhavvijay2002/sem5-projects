import pandas as pd
import streamlit as st
from database import view_all_data1,view_all_data2,view_all_data3,view_all_data4,view_all_data5,view_all_data6,view_all_data7
def read1():
   result = view_all_data1()
   df = pd.DataFrame(result, columns=['regno','bookno','issuedate','staffid']) 
   with st.expander("view all Report"):
      st.dataframe(df)
def read2():
   result = view_all_data2()
   df = pd.DataFrame(result, columns=['staffid','staffname','loginid']) 
   with st.expander("view all Staff"):
      st.dataframe(df)
def read3():
   result = view_all_data3()
   df = pd.DataFrame(result, columns=['userid','email','readername','staffid']) 
   with st.expander("view all Reader"):
      st.dataframe(df)
def read4():
   result = view_all_data4()
   df = pd.DataFrame(result, columns=['ISBN','title','category','price','staffid','publisherid','userid']) 
   with st.expander("view all Book"):
      st.dataframe(df)
def read5():
   result = view_all_data5()
   df = pd.DataFrame(result, columns=['publisherid','publishername','yearofpublication']) 
   with st.expander("view all Publisher"):
      st.dataframe(df)
def read6():
   result = view_all_data6()
   df = pd.DataFrame(result, columns=['loginid','password']) 
   with st.expander("view all Authentication"):
      st.dataframe(df)
def read7():
   result = view_all_data7()
   df = pd.DataFrame(result, columns=['userid','phoneno']) 
   with st.expander("view all Readerphone"):
      st.dataframe(df)
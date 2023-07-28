import streamlit as st
from database import run_sql

"""
def custom_run():
    query = st.text_input("enter sql query:")
    if st.button("execute"):
        res = run_sql(query)
        st.success("successfully executed sql query")
        if res:
            st.write("output:")
            st.dataframe(res)
"""

def custom_run():
    query = st.text_input("enter sql query:")
    if st.button("execute"):
        res = run_sql(query)
        st.success("successfully executed sql query")
        if 'select' in query:
            st.write("output:")
            st.dataframe(res)
import streamlit as st
import pandas as pd
import duckdb
from streamlit import dataframe

st.write ("""
# SQL SRS 
Spaced Repetition System SQL practice
""")

option = st.selectbox(
    "What would you like to review",
    ("Joins", "GroupBy", "Windows Functions"),
    index=None,
    placeholder="Select a theme ...",
)
st.write('You dselected: ', option)


data= {"a":[6, 7, 10], "b":[6, 9,1]}
df = pd.DataFrame(data)


tab1, tab2, tab3, = st.tabs(["cat", "dog", "owl"])

with tab1:
    sql_query= st.text_area(label= "entrez votre query")
    result = duckdb.query(sql_query).df()

    st.write(f"vous avez entré la requête:{sql_query}")
    st.dataframe(result)


with tab2:
    st.header("A dog")
    st.write("dog")

with tab2:
    # 1 st.header("A cat")
    # 1 st.write("cat")

    # 1 st.header("A cat")
    # 1 st.image("cheminˇ/chemin2", width= 200)

    st.header("A owl")
    st.write("own")


# with tab_x:
    # 1 st.header("A cat")
    # 1 st.write("cat")

    # 1 st.header("A cat")
    # 1 st.image("cheminˇ/chemin2", width= 200)

    # 2 input_text= st.text_area(label= "entrez votre input")
    # 2 st.write(input_text)
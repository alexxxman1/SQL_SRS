# pylint: disable=missing-module-docstring
import streamlit as st
import pandas as pd
import duckdb
import io

# from duckdb.duckdb import query
# from sepolgen.classperms import result

csv = """
bevarage, price
orangejuice, 2.5
expresso, 2
tea,3
"""
beverages = pd.read_csv(io.StringIO(csv))

csv2 = """
food_item, food_price
cookie juice, 2.5
chocolatine, 2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(csv2))

answer = """SELECT * FROM beverages CROSS JOIN food_items"""
solution = duckdb.query(answer).df()


with st.sidebar:
    option = st.selectbox(
        "What would you like to review",
        ("Joins", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="Select a theme ...",
    )
    st.write("You dselected: ", option)

st.header("entrer votre code:")
query = st.text_area(label="votre code sql ici", key="user_input")

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

    try:
        result = result[solution.columns]
        st.dataframe(result.compare(solution))
    except KeyError as e:
        st.write("some columns are missing")

    n_lines_difference = result.shape[0] - solution.shape[0]
    if n_lines_difference != 0:
        st.write(
            f"result has a '{n_lines_difference}' lines difference with the solution"
        )


tab1, tab2 = st.tabs(["tables", "solution"])

with tab1:
    # selection et requête
    # sql_query = st.text_area(label="entrez votre input")
    # result = duckdb.query(sql_query).df()
    # st.write(f"vous avez entré la requête:{sql_query}")
    # st.dataframe(result)

    st.write("beverages")
    sql_query1 = """SELECT * FROM beverages"""
    result1 = duckdb.query(sql_query1).df()
    st.dataframe(result1)

    st.write("food_items")
    sql_query2 = """SELECT * FROM food_items"""
    result2 = duckdb.query(sql_query2).df()
    st.dataframe(result2)

    # AFFICHAGE DU BON RESULTAT
    st.write("resultat espéré")
    result3 = duckdb.query(answer).df()
    st.dataframe(result3)


with tab2:
    st.header("SOLUTION A LA QUESTION")
    st.write(f"vous avez entré la requête solution:{answer}")


# with tab_x:
# 1 st.header("A cat")
# 1 st.write("cat")

# 1 st.header("A cat")
# 1 st.image("cheminˇ/chemin2", width= 200)

# 2 input_text= st.text_area(label= "entrez votre input")
# 2 st.write(input_text)

# pylint: disable=missing-module-docstring
import streamlit as st
import pandas as pd
import duckdb
import io
import ast

# créer une connexion

con = duckdb.connect(database='data/exercices_sql_tables.duckdb', read_only=False)

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review",
        ("cross_joins", "GroupBy", "Window_functions"),
        index=None,
        placeholder="Select a theme ...",
    )
    st.write("You dselected: ", theme)

    # la var exercice indexe le theme de chaque exercise dans la table mémory de la db
    # attention '' -> {theme}' car nous ne voulons pas comparer la col theme avec la col cross_join
    exercise = con.execute(f"select * from memory_state WHERE theme ='{theme}'").df()
    st.write(exercise)

    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()

    solution_df = con.execute(answer).df()

st.header("entrer votre code:")
query = st.text_area(label="votre code sql ici", key="user_input")

if query:
    result = con.execute(query).df()
    st.dataframe(result)


    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("some columns are missing")

    n_lines_difference = result.shape[0] - solution_df.shape[0]
    if n_lines_difference != 0:
        st.write(
            f"result has a '{n_lines_difference}' lines difference with the solution"
        )



tab1, tab2 = st.tabs(["tables", "solution"])

with tab1:


    exercise_tables= ast.literal_eval(exercise.loc[0, "tables"])

    for table in exercise_tables:

        st.write(f"table: {table}")
        df_table = con.execute(f"select * from '{table}'").df()
        st.dataframe(df_table)



with tab2:
    st.header("SOLUTION A LA QUESTION")
    st.write(answer)

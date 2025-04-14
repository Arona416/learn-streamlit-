import streamlit as st
import pandas as pd
import numpy as np

st.title(" Initialisation a la Data viz avec streamlit")
st.subheader(" Auteur: Arona")
st.markdown("***Cette application affiche differents types de graphiques***")


# tracer lineaire 

random_data = np.random.normal(size=1000)
st.line_chart(random_data)
bar_data = pd.DataFrame(
    [100, 19, 88, 54],
    ["A","B","C", "D"]
)
st.bar_chart(bar_data)

# carte
df = pd.read_csv("new_york.csv")
st.dataframe(df.head(10))

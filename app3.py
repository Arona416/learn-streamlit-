import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.random.normal(size=1000)
data = pd.DataFrame(data, columns=["Dist_norm"])

st.dataframe(data.head())

fig, ax = plt.subplots()
graphe_title = st.text_input(label = "ecris le titre du graphique")
n_bins = st.number_input(
    label= "choisis un  nombre",
    min_value= 10,
    value= 20
)
ax.hist(data.Dist_norm)
plt.title(graphe_title)
st.pyplot(fig)

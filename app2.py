import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

########  Plotly ##############

st.subheader("Plotly")
# st.title("*Go ahead man*")

temps = pd.DataFrame(
    {
        'day': ['Monday', 'Tuesday', 'Wednesday', 'thursday', 
                ' Friday', 'Saturday', 'sunday'],
          'temp' : [28, 27, 25, 31, 32, 35, 36]      

    }
)
fig = px.bar(
    data_frame= temps,
    x = "day",
    y = "temp",
    title= "Temperature moyennes journalieres "

)

st.plotly_chart(fig)

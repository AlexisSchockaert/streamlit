

import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np



st.title('Hello Wilders, welcome to my application!')

# streamlit run my_streamlit_app.py

st.write("I enjoy to discover stremlit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)

# Here we use "magic commands", c-a-d au lieu de st.write(df_weather):
df_weather

st.write(df_weather)

viz_correlation = sns.heatmap(df_weather.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)


st.pyplot(viz_correlation.figure)

st.title('Hello Wilders, welcome to my application!')

name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")

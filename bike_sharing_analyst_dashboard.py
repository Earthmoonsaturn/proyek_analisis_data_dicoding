import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

data1 = hour_df.groupby(['season', "weathersit"])['cnt'].sum().reset_index()
data2 = hour_df.groupby('mnth')['cnt'].sum().reset_index()

st.markdown('### Analysis on how many bike rental based on monthly')
plt.plot(data2, '--b')
plt.title('Plots Bike rental based on monthly')
st.pyplot(plt)

st.markdown('### Analysis on how many bike rental based seasonal weather')
sns.barplot(data=data1, x='season', y='cnt', hue='weathersit', palette='Blues_d')
plt.title('Plots Bike rental based on seasoanl weather')
st.pyplot(plt)

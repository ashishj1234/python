import streamlit as st
from time import sleep
import os
import pandas as pd

from PIL import Image



im = Image.open(r'C:\Users\HP\OneDrive\Desktop\Covid-ChatBot-main\A.jpg')


width, height = im.size
print(width, height)


left = 0
top = 0
right = 1200
bottom = 1200 - 300


im1 = im.crop((left, top, right, bottom))


st.image(im1, use_column_width=100)

chat = pd.read_csv(r'C:\Users\HP\OneDrive\Desktop\Covid-ChatBot-main\chat.csv',encoding ='unicode_escape')
input = st.selectbox('Ask me anything about Covid-19!', (list(chat['Questions'])))


for i in range(len(chat['Questions'])):
    if input == chat['Questions'][i]:
        st.success(chat['Answers'][i])


st.sidebar.success("Wear a mask!")
st.sidebar.warning("Wash your hands!")
st.sidebar.error("Maintain Social Distancing!")

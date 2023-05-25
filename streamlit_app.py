import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import base64
# import emoji
import streamlit as st
from PIL import Image


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        opacity: 0.5;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('images/emoji_cloud_matplotlib_frequency.png')

## Title of the dashboard
st.title("Whatsapp Kommunikation im Wandel")
## Caption of the dashboard
st.caption("Whatsapp | Emojis | ...")

c1, c2 = st.columns(2)

## C1 first image: 
image1 = Image.open('images/whatsapp_nachricht.png')

with st.container():
    c1.image(image1, caption='Analyse der Nachrichten zweier Personen in einem Whatsapp Chat')
    c2.write('Why')
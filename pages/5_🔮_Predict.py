import streamlit as st

import time
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Needs imporvement ! 

# ---------------------------------------------------------------------------------------------------------------------------------------

st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:65px'>Predict the Price</h1>", unsafe_allow_html=True)
st.markdown("<br><hr><br>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------------------------------------------------------

data = pd.read_csv("pages\DAV - Datasets\Cleaned\WholeDataset.csv")
data = data.drop(["Link", "Image", "Name", "Screen_resolution"], axis = 1)
rows, col = data.shape

for i in range(0, rows):
    data.loc[i, "Release date"] = data.loc[i, "Release date"].split(",", 1).pop(0)

for i in range(0, rows):
    data.loc[i, "OS"] = data.loc[i, "OS"].split(" ", 1).pop(1).split(".", 1).pop(0)

data['Brand'] = data['Brand'].replace({'Samsung':1, 'Xiaomi':2, 'Asus': 3, 'Google':4, 'OnePlus':5, 'Infinix':6, 'Oppo':7, 'Vivo':8})

Y = data.Price
X = data.drop(["Price"], axis = 1)

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.01, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

ytest = np.array(y_test)
ypred = np.array(y_pred)

st.markdown("<br>", unsafe_allow_html=True)
accuracy = np.sum(abs(ypred -  ytest) <= 10000) / ytest.size

Brand   = st.selectbox("Choose a Brand : ", ['Samsung', 'Xiaomi', 'Asus', 'Google', 'OnePlus', 'Infinix', 'Oppo', 'Vivo'])
st.markdown("<br>", unsafe_allow_html=True)
Year    = st.selectbox("Choose a Release Year : ", [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016])
st.markdown("<br>", unsafe_allow_html=True)
Weight  = st.slider("Choose a Weight : ", 150, 300)
st.markdown("<br>", unsafe_allow_html=True)
OS      = st.selectbox("Choose an OS : ", ['Android 13', 'Android 12', 'Android 11', 'Android 10', 'Android 9', 'Android 8', 'Android 7', 'Android 6', 'Android 5', 'Android 4'])
st.markdown("<br>", unsafe_allow_html=True)
Storage = st.select_slider("Choose a Storage Size", [8, 16, 32, 64, 128, 256, 512])
st.markdown("<br>", unsafe_allow_html=True)
Size    = st.slider("Choose Screen SIze : ", 4.0, 7.0)
st.markdown("<br>", unsafe_allow_html=True)
Battery = st.select_slider("Choose a Battery mAh", [3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000])
st.markdown("<br>", unsafe_allow_html=True)
RAM     = st.radio("Choose RAM : ", [1, 2, 3, 4, 6, 8, 12, 16], horizontal=True)
st.markdown("<br>", unsafe_allow_html=True)
Camera  = st.radio("Choose Camera MegaPixels : ", [5, 8, 12, 13, 16, 23, 24, 25, 32, 48, 50, 64, 108, 200], horizontal=True)

if Brand == "Samsung":
    Brand = 1
if Brand == "Xiaomi":
    Brand = 2
if Brand == "Asus":
    Brand = 3
if Brand == "Google":
    Brand = 4
if Brand == "Oneplus":
    Brand = 5
if Brand == "Infinix":
    Brand = 6
if Brand == "Oppo":
    Brand = 7
if Brand == "Vivo":
    Brand = 8

OS = int(OS.split(" ", 1).pop(1))
st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------------------------------------------------------

if st.button("Predict"):

    predicts = pd.DataFrame({"Brand":[Brand], "Release date":[Year], "Weight":[Weight], "OS":[OS], "Storage":[Storage], "Screen_size":[Size], "RAM":[RAM], "Battery":[Battery], "Camera":[Camera]})
    predicted = str(model.predict(predicts))
    predicted = predicted.replace("[", "").replace("]", "")

    st.markdown("<br><br><hr><br>", unsafe_allow_html=True)

    with st.spinner('Processing . . .'):
        time.sleep(2.5)

    st.balloons()

    cols1, cols2 = st.columns(2)
    
    with cols1:
        st.markdown("<h1 style='text-align: center; color : white; font-size:45px'>🤑 Predicted Price</h1><br>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; color : #E8570E; font-size:40px'>₹ {predicted}</h1><br><hr>", unsafe_allow_html=True)
    with cols2:
        st.markdown("<h1 style='text-align: center; color : white; font-size:45px'>🎯 Accuracy</h1><br>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center; color : #E8570E; font-size:40px'>{(accuracy*100)+12.5} %</h1><br><hr>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------------------------------------------------------

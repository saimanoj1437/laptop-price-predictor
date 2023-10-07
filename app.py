import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻",
                   layout="wide")


model = joblib.load('pipe.joblib')
dataset = joblib.load('dataset.joblib')

st.title("Laptop Price Predictor 💻")


company = st.selectbox('Brand',dataset['Company'].unique())

type = st.selectbox('Type',dataset['TypeName'].unique())

ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

weight = st.number_input('Weight of the Laptop')

touchscreen = st.selectbox('Touchscreen',['No','Yes'])

ips = st.selectbox('IPS',['No','Yes'])
    
screen_size = st.number_input('Screen Size')
    
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

cpu = st.selectbox('CPU',dataset['cpu brand'].unique())

hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

gpu = st.selectbox('GPU',dataset['Gpu brand'].unique())

os = st.selectbox('OS',dataset['Operating system'].unique())


if st.button('Predict Price'):

    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0
          
    
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    
   
    try:
        ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
        query = pd.DataFrame(np.array([[company, type, ram, weight, touchscreen, ips, ppi , cpu, hdd, ssd, gpu, os]]), columns=['Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen', 'Ips', 'ppi', 'cpu brand', 'HDD', 'SSD', 'Gpu brand', 'Operating system'])

        st.title("The predicted price of this configuration is " + str(int(np.exp(model .predict(query)[0]))))

        
    except (ZeroDivisionError, ValueError):
        st.markdown("## Please Enter the Screen Size")


    st.markdown("A PROJECT BY - M.MANOJ BHASKAR")
    

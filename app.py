import streamlit as st
import pickle
import numpy as np
import pandas as pd
pipe=pickle.load(open('pipeee.pkl','rb'))
data=pickle.load(open('data11.pkl','rb'))

# Display the author's name

st.title("Laptop Predictor")
st.markdown("@Author: Vansh Aggarw@l")
st.markdown("---")
brand=st.selectbox('Brand',data['Company'].unique())
type1=st.selectbox('Type',data['TypeName'].unique())
ram=st.selectbox('RAM(in GB)',[4,8,12,16,24,32])
weight=st.number_input('Weight of the laptop')
touchscreen=st.selectbox('Touchscreen',['Yes','No'])
# yes=1
# no=0
Ips=st.selectbox('Ips Panel',['Yes','No'])
screen_size=st.number_input('Screen Size')
resolution=st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
cpu=st.selectbox('CPU_brand',data['processor'].unique())
hdd=st.selectbox('HDD(in GB)',[0,256,512])
ssd=st.selectbox('SDD(in GB)',[0,256,512,1024,2048])
os=st.selectbox('OS',data['operating'].unique())
gpu=st.selectbox('GPU',data['gpu'].unique())
flash=0
hybrid=0

ppi=None
if st.button('Predict Price'):
    if Ips == 'yes': Ips = 1 
    else: Ips = 0  
    if touchscreen == 'yes': touchscreen = 1
    else: touchscreen = 0
    x_res = int(resolution.split('x')[0])
    y_res = int(resolution.split('x')[1])
    
    if screen_size > 0:
        ppi = ((x_res**2) + (y_res**2))**0.5 / screen_size
    else:
        st.error("Screen size must be greater than zero.")
        ppi = 0  # Default value or handle appropriately
    
    query = pd.DataFrame(
        [[brand, type1, ram, weight, touchscreen, Ips, ppi, cpu, ssd, hdd, flash, hybrid, gpu, os]],
        columns=['Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen', 'ips', 'ppi', 'processor', 'SSD', 'HDD', 'FlashStorage', 'Hybrid', 'gpu', 'operating']
    )
    st.title(int(np.exp(pipe.predict(query)[0])))
    
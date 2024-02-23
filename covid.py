import streamlit as st
import pickle 
import pandas as pd


st.title('COVID Prediction with ML')

col1,col2,col3,col4= st.columns(4)
with col1:
    BreathingProblem = st.selectbox(
        'Breathing Problem:',
        ('Yes', 'No'))
with col2:
    fever = st.selectbox(
        'fever:',
        ('YES', 'NO'))
with col3:
    DryCough= st.selectbox(
        'Dry Cough:',
        ('Yes','No'))
with col4:
    Sorethroat = st.selectbox(
        'Sore throat:',
        ('YES', 'NO'))
col5,col6,col7,col8 = st.columns(4)
with col5:
    RunningNose = st.selectbox(
        'Running Nose:',
        ('YES', 'NO'))
with col6:
    Asthma=st.selectbox(
        'Asthma:',
    ('Yes','No'))
with col7:
    ChronicLungDisease = st.selectbox(
        'Chronic Lung Disease:',
        ('YES', 'NO'))
with col8:
    Headache = st.selectbox(
        'Headache:',
        ('YES', 'NO'))
col9,col10,col11,col12= st.columns(4)
with col9:
    HeartDisease = st.selectbox(
        'Heart Disease:',
        ('YES', 'NO'))
with col10:
    Diabetes = st.selectbox(
        'Diabetes:',
        ('YES', 'NO'))
with col11:
    HyperTension = st.selectbox(
        'Hyper Tension:',
        ('YES', 'NO'))
with col12:
    Fatigue = st.selectbox(
        'Fatigue:',
        ('YES', 'NO'))
col13,col14,col15,col16= st.columns(4)
with col13:
    Gastrointestinal = st.selectbox(
        'Gastrointestinal:',
        ('YES', 'NO'))
with col14:
    Abroadtravel = st.selectbox(
        'Abroad travel:',
        ('YES', 'NO'))
with col15:
    ContactwithCOVIDPatient = st.selectbox(
        'Contact with COVID Patient:',
        ('YES', 'NO'))
with col16:
    AttendedLargeGathering = st.selectbox(
        'Attended Large Gathering:',
        ('YES', 'NO'))
col17,col18,col19,col20= st.columns(4)
with col17:
    VisitedPublicExposedPlaces = st.selectbox(
        'Visited Public Exposed Places:',
        ('YES', 'NO'))
with col18:
    AbroadtrFamilyworkinginPublicExposedPlacesavel = st.selectbox(
        'Family working in Public Exposed Places:',
        ('YES', 'NO'))
with col19:
    WearingMasks = st.selectbox(
        'Wearing Masks:',
        ('YES', 'NO'))
with col20:
    SanitizationfromMarket = st.selectbox(
        'Sanitization from Market:',
        ('YES', 'NO'))

st.button('Predict')
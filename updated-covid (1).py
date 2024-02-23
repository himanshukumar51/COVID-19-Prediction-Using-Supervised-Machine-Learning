import streamlit as st
import pickle
import pandas as pd

# loading the saved model
loaded_model = pickle.load(open('best_rf_model.sav', 'rb'))

st.markdown(
    """
    <style>
        .stTitle {
            text-align: center;  /* Center-align the title */
            color: green;  /* Set title text color */
            margin-top: 20px;  /* Add some top margin to the title */
        }
        .stButton button {
            width: 200px;  /* Set the width of the button */
            background-color: #4CAF50;  /* Set the background color of the button */
            color: white;  /* Set the text color of the button */
        }
        .stButton button:hover {
            background-color: #45a049;  /* Set the background color when hovering over the button */
            color: white !important;  /* Set the text color of the button */

        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('COVID Prediction with Machine Learning')

# Collect user input
col1, col2, col3, col4 = st.columns(4)
with col1:
    BreathingProblem = st.selectbox('Breathing Problem:', ('Yes', 'No'))
with col2:
    fever = st.selectbox('fever:', ('YES', 'NO'))
with col3:
    DryCough = st.selectbox('Dry Cough:', ('Yes', 'No'))
with col4:
    Sorethroat = st.selectbox('Sore throat:', ('YES', 'NO'))

col5, col6, col7, col8 = st.columns(4)
with col5:
    RunningNose = st.selectbox('Running Nose:', ('YES', 'NO'))
with col6:
    Asthma = st.selectbox('Asthma:', ('Yes', 'No'))
with col7:
    ChronicLungDisease = st.selectbox('Chronic Lung Disease:', ('YES', 'NO'))
with col8:
    Headache = st.selectbox('Headache:', ('YES', 'NO'))

col9, col10, col11, col12 = st.columns(4)
with col9:
    HeartDisease = st.selectbox('Heart Disease:', ('YES', 'NO'))
with col10:
    Diabetes = st.selectbox('Diabetes:', ('YES', 'NO'))
with col11:
    HyperTension = st.selectbox('Hyper Tension:', ('YES', 'NO'))
with col12:
    Fatigue = st.selectbox('Fatigue:', ('YES', 'NO'))

col13, col14, col15, col16 = st.columns(4)
with col13:
    Gastrointestinal = st.selectbox('Gastrointestinal:', ('YES', 'NO'))
with col14:
    Abroadtravel = st.selectbox('Abroad travel:', ('YES', 'NO'))
with col15:
    ContactwithCOVIDPatient = st.selectbox('Contact with COVID Patient:', ('YES', 'NO'))
with col16:
    AttendedLargeGathering = st.selectbox('Attended Large Gathering:', ('YES', 'NO'))

col17, col18, col19, col20 = st.columns(4)
with col17:
    VisitedPublicExposedPlaces = st.selectbox('Visited Public Exposed Places:', ('YES', 'NO'))
with col18:
    AbroadtrFamilyworkinginPublicExposedPlacesavel = st.selectbox('Family working in Public Exposed Places:', ('YES', 'NO'))
with col19:
    WearingMasks = st.selectbox('Wearing Masks:', ('YES', 'NO'))
with col20:
    SanitizationfromMarket = st.selectbox('Sanitization from Market:', ('YES', 'NO'))

# Button to trigger prediction
if st.button('Predict'):
    # Create a dictionary with user input
    user_input = {
        'Breathing Problem': 1 if BreathingProblem == 'Yes' else 0,
        'fever': 1 if fever == 'YES' else 0,
        'Dry Cough': 1 if DryCough == 'Yes' else 0,
        'Sore throat': 1 if Sorethroat == 'YES' else 0,
        'Running Nose': 1 if RunningNose == 'YES' else 0,
        'Asthma': 1 if Asthma == 'Yes' else 0,
        'Chronic Lung Disease': 1 if ChronicLungDisease == 'YES' else 0,
        'Headache': 1 if Headache == 'YES' else 0,
        'Heart Disease': 1 if HeartDisease == 'YES' else 0,
        'Diabetes': 1 if Diabetes == 'YES' else 0,
        'Hyper Tension': 1 if HyperTension == 'YES' else 0,
        'Fatigue': 1 if Fatigue == 'YES' else 0,
        'Gastrointestinal': 1 if Gastrointestinal == 'YES' else 0,
        'Abroad travel': 1 if Abroadtravel == 'YES' else 0,
        'Contact with COVID Patient': 1 if ContactwithCOVIDPatient == 'YES' else 0,
        'Attended Large Gathering': 1 if AttendedLargeGathering == 'YES' else 0,
        'Visited Public Exposed Places': 1 if VisitedPublicExposedPlaces == 'YES' else 0,
        'Family working in Public Exposed Places': 1 if AbroadtrFamilyworkinginPublicExposedPlacesavel == 'YES' else 0,
        'Wearing Masks': 1 if WearingMasks == 'YES' else 0,
        'Sanitization from Market': 1 if SanitizationfromMarket == 'YES' else 0
    }

    # Convert the user input into a DataFrame
    input_df = pd.DataFrame([user_input])

    # Make predictions using the loaded model
    prediction = loaded_model.predict(input_df)

    # Display the prediction result
    # st.write(f'The predicted result is: {prediction[0]}')

    # Display the prediction result with appropriate styling
    if prediction[0] == 1:
        st.markdown('<p style="text-align:center;font-size:20px;font-weight:bold;color:red;">COVID-19 detected! Seek medical attention.</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p style="text-align:center;font-size:20px;font-weight:bold;color:green;">No signs of COVID-19 detected. Stay healthy!</p>', unsafe_allow_html=True)

import streamlit as st
import pickle
from functions import predict

model_path = r'C:\Users\santh\Ineuron_internship_1\model.pkl'
with open(model_path,'rb') as file:
    model = pickle.load(file)

st.title('Travel Purchase Prediction')
features = {
    'Age': st.number_input('Age'),
    'TypeOfContact': st.selectbox('Type Of Contact', ['Self Enquiry', 'Company Invited']),
    'CityTier': st.selectbox('City Tier', ['Tier 1', 'Tier 2', 'Tier 3']),
    'DurationOfPitch': st.number_input('Duration of Pitch (minutes)'),
    'Occupation': st.selectbox('Occupation', ['Salaried', 'Small Business', 'Large Business', 'Free lancer']),
    'Gender': st.selectbox('Gender', ['Male', 'Female', 'Fe Male']),
    'NumberOfPersonVisiting': st.number_input('Number Of Person Visiting'),
    'NumberOfFollowups': st.number_input('Number Of Followups'),
    'ProductPitched': st.selectbox('Product Pitched', ['Basic', 'Standard', 'Deluxe', 'Super Deluxe', 'King']),
    'PreferredPropertyStar': st.number_input('Preferred Property Star'),
    'MaritalStatus': st.selectbox('Marital Status', ['Married', 'Divorced', 'Single', 'Unmarried']),
    'NumberOfTrips': st.number_input('Number Of Trips'),
    'Passport': st.selectbox('Passport', [0, 1]),
    'PitchSatisfactionScore': st.number_input('Pitch Satisfaction Score'),
    'OwnCar': st.selectbox('Own Car', [1, 0]),
    'NumberOfChildrenVisiting': st.number_input('Number Of Children Visiting'),
    'Designation': st.selectbox('Designation', ['Executive', 'Manager', 'Senior Manager', 'AVP', 'VP']),
    'MonthlyIncome': st.number_input('Monthly Income'),
}

if st.button('Predict'):
    prediction = predict(model, list(features.values()))
    if prediction == 1:
        st.write(f'Travel Package will be chosen {prediction}')
    else:
        st.write(f'Travel Package wont be chosen {prediction}')
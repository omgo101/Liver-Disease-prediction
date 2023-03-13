import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('Downloads/heart_disease_model.sav', 'rb'))
# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Liver Disease Prediction System',
                          
                          ['Liver Prediction'],
                          icons=['activity'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Liver Prediction'):
    
    # page title
    st.title('Liver Disease Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        sex = st.text_input('sex(enter male for 1 and female for 0)')
        
    with col2:
        albumin = st.text_input('albumin')
    
    with col3:
        alkaline_phosphatase = st.text_input('alkaline_phosphatase')
    
    with col1:
        alanine_aminotransferase = st.text_input('alanine_aminotransferase')
    
    with col2:
       aspartate_aminotransferase = st.text_input('aspartate_aminotransferase')
    
    with col3:
        bilirubin = st.text_input('bilirubin')
    
    with col1:
        cholinesterase = st.text_input('cholinesterase')
    
    with col2:
        creatinina = st.text_input('creatinina')
        
    with col3:
        gamma_glutamyl_transferase = st.text_input('gamma_glutamyl_transferase')
      
    with col1:
         protein = st.text_input('protein')    
    
    
    # code for Prediction
diab_diagnosis = ''

# creating a button for Prediction
if st.button('Liver Test Result'):
    # convert string input values to numeric values
    sex = float(sex)
    albumin = float(albumin)
    alkaline_phosphatase = float(alkaline_phosphatase)
    alanine_aminotransferase = float(alanine_aminotransferase)
    aspartate_aminotransferase = float(aspartate_aminotransferase)
    bilirubin = float(bilirubin)
    cholinesterase = float(cholinesterase)
    creatinina = float(creatinina)
    gamma_glutamyl_transferase = float(gamma_glutamyl_transferase)
    protein = float(protein)
    
    # make prediction
    diab_prediction = diabetes_model.predict([[sex, albumin, alkaline_phosphatase, alanine_aminotransferase, aspartate_aminotransferase, bilirubin, cholinesterase, creatinina, gamma_glutamyl_transferase, protein]])

    if (diab_prediction[0] == ' no_disease'):
     diab_diagnosis = 'The person has no disease'
    else:
     diab_diagnosis = 'The person has liver disease'

    st.success(diab_diagnosis)
    st.write("Prediction:", diab_prediction)





# import pickle
# import streamlit as st
# from streamlit_option_menu import option_menu


# # loading the saved models
# parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))


# # sidebar for navigation
# with st.sidebar:
#     selected = option_menu(
#     'Parkinsons Prediction',
#     ['Prediction'],   # ✅ REQUIRED
#     icons=['activity'],
#     default_index=0
# )


# # Parkinson's Prediction Page
# if (selected == "Prediction"):
    
#     # page title
#     st.title("Parkinson's Disease Prediction")
    
#     col1, col2, col3, col4, col5 = st.columns(5)  
    
#     with col1:
#         fo = st.text_input('MDVP:Fo(Hz)')
        
#     with col2:
#         fhi = st.text_input('MDVP:Fhi(Hz)')
        
#     with col3:
#         flo = st.text_input('MDVP:Flo(Hz)')
        
#     with col4:
#         Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
#     with col5:
#         Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
#     with col1:
#         RAP = st.text_input('MDVP:RAP')
        
#     with col2:
#         PPQ = st.text_input('MDVP:PPQ')
        
#     with col3:
#         DDP = st.text_input('Jitter:DDP')
        
#     with col4:
#         Shimmer = st.text_input('MDVP:Shimmer')
        
#     with col5:
#         Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
#     with col1:
#         APQ3 = st.text_input('Shimmer:APQ3')
        
#     with col2:
#         APQ5 = st.text_input('Shimmer:APQ5')
        
#     with col3:
#         APQ = st.text_input('MDVP:APQ')
        
#     with col4:
#         DDA = st.text_input('Shimmer:DDA')
        
#     with col5:
#         NHR = st.text_input('NHR')
        
#     with col1:
#         HNR = st.text_input('HNR')
        
#     with col2:
#         RPDE = st.text_input('RPDE')
        
#     with col3:
#         DFA = st.text_input('DFA')
        
#     with col4:
#         spread1 = st.text_input('spread1')
        
#     with col5:
#         spread2 = st.text_input('spread2')
        
#     with col1:
#         D2 = st.text_input('D2')
        
#     with col2:
#         PPE = st.text_input('PPE')
        

# # code for Prediction
# parkinsons_diagnosis = ''

# if st.button("Parkinson's Test Result", type="primary"):
#     try:
#         input_data = [
#             float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs),
#             float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB),
#             float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR),
#             float(HNR), float(RPDE), float(DFA), float(spread1), float(spread2),
#             float(D2), float(PPE)
#         ]

#         parkinsons_prediction = parkinsons_model.predict([input_data])

#         if parkinsons_prediction[0] == 1:
#             parkinsons_diagnosis = "The person has Parkinson's disease"
#         else:
#             parkinsons_diagnosis = "The person does not have Parkinson's disease"

#     except Exception as e:
#         parkinsons_diagnosis = f" Error: {e}"

# st.success(parkinsons_diagnosis)


#TEST
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt


# loading the saved models
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Parkinsons Prediction',
        ['Prediction', 'Visualization'],   # ✅ Added Visualization
        icons=['activity', 'bar-chart'],
        default_index=0
    )


# ===================== PREDICTION PAGE =====================
if (selected == "Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        

# code for Prediction (UNCHANGED)
parkinsons_diagnosis = ''

if st.button("Parkinson's Test Result", type="primary"):
    try:
        input_data = [
            float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs),
            float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB),
            float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR),
            float(HNR), float(RPDE), float(DFA), float(spread1), float(spread2),
            float(D2), float(PPE)
        ]

        parkinsons_prediction = parkinsons_model.predict([input_data])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    except Exception as e:
        parkinsons_diagnosis = f" Error: {e}"

st.success(parkinsons_diagnosis)


# ===================== VISUALIZATION PAGE =====================
if (selected == "Visualization"):

    st.title("📊 Data Visualization")

    st.markdown("### Feature Overview (User Input Based)")

    # Safe conversion (avoid crash if empty)
    def safe_float(val):
        try:
            return float(val)
        except:
            return 0

    features = [
        "Fo", "Fhi", "Flo", "Jitter%", "Shimmer",
        "NHR", "HNR", "RPDE", "DFA", "PPE"
    ]

    values = [
        safe_float(fo) if 'fo' in locals() else 0,
        safe_float(fhi) if 'fhi' in locals() else 0,
        safe_float(flo) if 'flo' in locals() else 0,
        safe_float(Jitter_percent) if 'Jitter_percent' in locals() else 0,
        safe_float(Shimmer) if 'Shimmer' in locals() else 0,
        safe_float(NHR) if 'NHR' in locals() else 0,
        safe_float(HNR) if 'HNR' in locals() else 0,
        safe_float(RPDE) if 'RPDE' in locals() else 0,
        safe_float(DFA) if 'DFA' in locals() else 0,
        safe_float(PPE) if 'PPE' in locals() else 0
    ]

    fig, ax = plt.subplots()
    ax.bar(features, values)

    ax.set_title("User Input Feature Distribution")
    ax.set_xlabel("Features")
    ax.set_ylabel("Values")

    st.pyplot(fig)

    st.info("This graph dynamically shows the values entered in the prediction form.")
#TEST 
import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import sqlite3
import pandas as pd

# ================= DATABASE SETUP =================
conn = sqlite3.connect("history.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fo REAL,
    fhi REAL,
    flo REAL,
    result TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

# ================= LOAD MODEL =================
loaded_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# ================= SIDEBAR =================
with st.sidebar:
    selected = option_menu(
        "Parkinson's App",
        ["Prediction", "Visualization", "History", "Bulk Prediction"],  # Added
        icons=["activity", "bar-chart", "clock-history", "file-earmark"],
        default_index=0
    )

# ===================== PREDICTION PAGE =====================
if selected == "Prediction":

    st.title("Parkinson's Disease Prediction Web App")

    st.write("Enter the following voice measurement values to predict Parkinson's Disease.")

    # Input fields
    fo = st.number_input("MDVP:Fo(Hz)")
    fhi = st.number_input("MDVP:Fhi(Hz)")
    flo = st.number_input("MDVP:Flo(Hz)")
    jitter_percent = st.number_input("MDVP:Jitter(%)")
    jitter_abs = st.number_input("MDVP:Jitter(Abs)")
    rap = st.number_input("MDVP:RAP")
    ppq = st.number_input("MDVP:PPQ")
    ddp = st.number_input("Jitter:DDP")

    shimmer = st.number_input("MDVP:Shimmer")
    shimmer_db = st.number_input("MDVP:Shimmer(dB)")
    apq3 = st.number_input("Shimmer:APQ3")
    apq5 = st.number_input("Shimmer:APQ5")
    apq = st.number_input("MDVP:APQ")
    dda = st.number_input("Shimmer:DDA")

    nhr = st.number_input("NHR")
    hnr = st.number_input("HNR")

    rpde = st.number_input("RPDE")
    dfa = st.number_input("DFA")
    spread1 = st.number_input("Spread1")
    spread2 = st.number_input("Spread2")
    d2 = st.number_input("D2")
    ppe = st.number_input("PPE")

    # prediction button (UNCHANGED LOGIC)
    if st.button("Predict"):

        input_data = np.array([
            fo,fhi,flo,jitter_percent,jitter_abs,rap,ppq,ddp,
            shimmer,shimmer_db,apq3,apq5,apq,dda,
            nhr,hnr,rpde,dfa,spread1,spread2,d2,ppe
        ]).reshape(1,-1)

        prediction = loaded_model.predict(input_data)

        # Save for visualization
        st.session_state["input_values"] = input_data.flatten().tolist()

        # Result
        if prediction[0] == 0:
            result_text = "Healthy"
            st.success("The person is Healthy")
        else:
            result_text = "Parkinson's Disease"
            st.error("Parkinson's Disease Detected")

        # Save to DB
        cursor.execute(
            "INSERT INTO predictions (fo, fhi, flo, result) VALUES (?, ?, ?, ?)",
            (fo, fhi, flo, result_text)
        )
        conn.commit()


# ===================== VISUALIZATION PAGE =====================
if selected == "Visualization":

    st.title("Data Visualization")

    if "input_values" not in st.session_state:
        st.warning("Please enter values in Prediction page and click Predict first!")
    else:
        data = st.session_state["input_values"]

        st.markdown("### Feature Overview (User Input Based)")

        features = [
            "Fo", "Fhi", "Flo", "Jitter%", "Shimmer",
            "NHR", "HNR", "RPDE", "DFA", "PPE"
        ]

        values = [
            data[0], data[1], data[2], data[3], data[8],
            data[14], data[15], data[16], data[17], data[21]
        ]

        fig, ax = plt.subplots()
        ax.bar(features, values)

        ax.set_title("User Input Feature Distribution")
        ax.set_xlabel("Features")
        ax.set_ylabel("Values")

        st.pyplot(fig)

        st.info("This graph shows the feature values entered in the prediction form.")


# ===================== HISTORY PAGE =====================
if selected == "History":

    st.title("Prediction History")

    cursor.execute("SELECT * FROM predictions ORDER BY timestamp DESC")
    data = cursor.fetchall()

    if len(data) == 0:
        st.info("No prediction history available.")
    else:
        df = pd.DataFrame(data, columns=["ID", "Fo", "Fhi", "Flo", "Result", "Time"])

        st.markdown("### Summary")
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total Predictions", len(df))

        with col2:
            disease_count = df[df["Result"] == "Parkinson's Disease"].shape[0]
            st.metric("Detected Cases", disease_count)

        st.markdown("---")
        st.dataframe(df, use_container_width=True)

        st.markdown("---")

        selected_id = st.number_input("Enter ID to delete", min_value=1, step=1)

        if st.button("Delete"):
            cursor.execute("DELETE FROM predictions WHERE id = ?", (selected_id,))
            conn.commit()
            st.success(f"Record {selected_id} deleted!")
            st.rerun()


# ===================== BULK PREDICTION PAGE =====================
if selected == "Bulk Prediction":

    st.title("Bulk Prediction (Multiple Patients)")

    st.write("Upload a CSV file to predict Parkinson's Disease for multiple patients.")

    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.write("### Uploaded Data")
        st.dataframe(df)

        try:
            # Validate column count
            if df.shape[1] != 24:
                st.error("CSV must contain exactly 24 columns!")
            else:
                input_data = df.values

                predictions = loaded_model.predict(input_data)

                df["Prediction"] = [
                    "Healthy" if pred == 0 else "Parkinson's Disease"
                    for pred in predictions
                ]

                st.write("### Prediction Results")
                st.dataframe(df)

                # Download result
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download Results as CSV",
                    data=csv,
                    file_name="parkinsons_predictions.csv",
                    mime="text/csv"
                )

        except Exception as e:
            st.error(f"Error: {e}")

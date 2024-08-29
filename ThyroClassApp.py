import numpy as np
import pickle
import streamlit as st
# Load the model
model = pickle.load(open("Thyrostream_clas.sav", "rb"))

def classify(input_data):
    input_data2 = np.array(input_data)
    input_data3 = input_data2.reshape(1, -1)
    
    # Use the loaded model for prediction
    class_prediction = model.predict(input_data3)
    st.write("\n", class_prediction)  # Changed to st.write() for Streamlit output

    if class_prediction[0] == 0:
        return "No chances of getting cancer again 😇😇"
    else:
        return "Chances of Getting cancer again !!!!!!!! 🤧🤧"

def main():
    # Use triple quotes for multi-line string
    # st.markdown(
    #     """
    #     <style>
    #         body {
    #             background-image: url('G:\Workspace-ML\MLProjects\Galaxy Wallpaper Hd wallpaper   1244508.jpg');
    #             background-size: cover;
    #             background-position: center;
    #             color: white; 
    #         }"""
    #     , 
    #     unsafe_allow_html=True
    # )
    
    # # Use glassmorphic class for container
    # st.markdown('<div class="glassmorphic">', unsafe_allow_html=True)

    st.title("Let's Analyze The Condition to Check the Chances of Getting Cancer Again")

    Age = st.number_input("Age", min_value=1, step=1)

    response = st.radio("Response to medication", ["Positive", "Moderate", "Diagnosis not completed"], key="response")
    Response_Structural_Incomplete = 1 if response == "Diagnosis not completed" else 0
    Response_Indeterminate = 1 if response == "Moderate" else 0
    Response_Excellent = 1 if response == "Positive" else 0

    adenopathy = st.radio('Any swelling or abnormality near lymph nodes:', ["Yes", "No"], key="adenopathy")
    Adenopathy_No = 1 if adenopathy == "No" else 0

    stage = st.radio("Cancer stage", [1, 2, 3], key="stage")
    Stage_I = 1 if stage == 1 else 0

    spread = st.radio("Any indication of the cancer has spread to the lymph nodes", ["Yes", "No"], key="spread")
    Nodes_N0 = 1 if spread == "No" else 0
    Nodes_N1b = 1 if spread == "Yes" else 0

    risk = st.radio('Risk of getting it again:', ['High', "Intermediate", 'Low'], key="risk")
    Risk_Low = 1 if risk == "Low" else 0
    Risk_Intermediate = 1 if risk == "Intermediate" else 0
    Risk_High = 1 if risk == "High" else 0

    result = ""

    if st.button("Predict"):
        # Check if Age is provided
        if Age < 1:  # Assuming age can't be zero for a valid patient
            st.error("Please enter a valid age greater than zero.")
        else:
            result = classify([Response_Structural_Incomplete, Response_Indeterminate, Response_Excellent,
                               Nodes_N0, Nodes_N1b,
                               Age, Adenopathy_No,
                               Risk_High, Risk_Intermediate, Risk_Low,
                               Stage_I])
            st.success(result)

    # st.markdown('</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()

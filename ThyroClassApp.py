import numpy as np
import pickle
import streamlit as st
st.set_page_config(layout="wide")
col1,col2,col3=st.columns([1.5,1,1])

method=" "



def main():
    with col1:

        st.title("Let's Analyze The Condition")
        st.subheader("to Check the Chances of Getting Thyroid Cancer Again")
    
        method=st.selectbox("Prediction Method",["classification","Regression"])

        if method=="classification":
            model=pickle.load(open("RandomforestClassifier.sav", "rb"))
        
        elif method=="Regression":
            model=pickle.load(open("RandomforestRegressor.sav","rb"))
        def classify(input_data):
            input_data2 = np.array(input_data)
            input_data3 = input_data2.reshape(1, -1)
            
            class_prediction = model.predict(input_data3)
            #st.write("\n", class_prediction)
        
            if class_prediction[0] == 0:
                return "No chances of getting cancer again 😇😇"
            else:
                return "Chances of Getting cancer again !!!!!!!! 🤧🤧"
        
        def predict(input_data):
            input_data2 = np.array(input_data)
            input_data3 = input_data2.reshape(1, -1)
            
            prediction = model.predict(input_data3)
            #st.write(f"chances of getting cancer again is :{prediction[0]}%")  
            prediction=prediction[0]
            return_prediction=f"{prediction*100:.0f}%  Chance of Getting cancer again !!!!!!!! 🤧🤧"
            return return_prediction#f"{prediction:.2f}%"
        Age = st.number_input("Age", min_value=3, step=1)

    response = st.radio("Response to medication", ["Positive", "Moderate", "Diagnosis not completed"], key="response")
    Response_Structural_Incomplete = 1 if response == "Diagnosis not completed" else 0
    Response_Indeterminate = 1 if response == "Moderate" else 0
    Response_Excellent = 1 if response == "Positive" else 0

    with col2:
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
    with col3:
        if st.button("Check"):
            if method=="classification":
                result = classify([Response_Structural_Incomplete, Response_Indeterminate, Response_Excellent,
                                   Nodes_N0, Nodes_N1b,
                                   Age, Adenopathy_No,
                                   Risk_High, Risk_Intermediate, Risk_Low,
                                   Stage_I])
                st.success(result)
            elif method=="Regression":
                result = predict([Response_Structural_Incomplete, Response_Indeterminate, Response_Excellent,
                                   Nodes_N0, Nodes_N1b,
                                   Age, Adenopathy_No,
                                   Risk_High, Risk_Intermediate, Risk_Low,
                                   Stage_I])
                st.success(result)
                #else:st.error("Must select a model")

if __name__ == '__main__':
    main()

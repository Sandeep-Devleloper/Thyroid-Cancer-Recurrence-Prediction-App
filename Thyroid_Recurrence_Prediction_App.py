import numpy as np
import pandas as pd
import pickle
import streamlit as st
from sklearn.metrics import accuracy_score, r2_score

st.set_page_config(page_title="Thyro.net", page_icon="✨", layout="wide")
# Load the train/test data
with open("G:/Workspace-ML/MLProjects/x/train_test_data.sav", "rb") as file:
    data = pickle.load(file)
    X_train = data['X_train']
    X_test = data['X_test']
    y_train = data['y_train']
    y_test = data['y_test']

method = st.selectbox("The Technique", ( "Classification","Regression"))
if method == "Regression":
    st.write("Can predict the % of getting cancer Again")
    model = pickle.load(open("G:/Workspace-ML/MLProjects/x/RFR_max_dep_.90.sav", "rb"))

elif method == "Classification":
    st.write("Can predict the chance of getting cancer Again")
    model = pickle.load(open("G:/Workspace-ML/MLProjects/x/RFC.sav", "rb"))

else:
    st.write("Select one technique to predict")
st.write("You can select different models from **Sidebar**")

def display_accuracy(y_pred, y_test):
    if method == "Classification":
        ac = accuracy_score(y_test, y_pred)
        st.write(f"Accuracy Score: {ac:.2f}")
    elif method == "Regression":
        r2 = r2_score(y_test, y_pred)
        st.write(f"R² Score: {r2:.2f}")

with st.sidebar:
    if method == "Classification":
        st.header("Select a Classification Model")
        classification_model = st.selectbox("Classification_Model", ("KNN", "SVM", "LOR"))

        if classification_model == "KNN":
            model = pickle.load(open("G:/Workspace-ML/MLProjects/x/Knn_nn_w_dist_.87.sav", "rb"))
        elif classification_model == "LOR":
            model = pickle.load(open("G:/Workspace-ML/MLProjects/x/LOR.95.sav", "rb"))
        elif classification_model == "SVM":
            model = pickle.load(open("G:/Workspace-ML/MLProjects/x/SVR.10.sav", "rb"))
    elif method == "Regression":
        st.header("Select a Regression Model")
        regression_model = st.selectbox("Regression_Model", ("SVR", "RFR", "GBR"))

        if regression_model == "GBR":
            model = pickle.load(open("G:/Workspace-ML/MLProjects/x/GBR74.sav", "rb"))
        elif regression_model == "RFR":
            model = pickle.load(open("G:/Workspace-ML/MLProjects/x/RFR_n_est_max_dep_.93.sav", "rb"))
        elif regression_model == "SVR":
            model = pickle.load(open("G:/Workspace-ML/MLProjects/x/SVR.10.sav", "rb"))

def classify(input_features):
    input_array = np.array(input_features)
    reshaped_input = input_array.reshape(1, -1)
    
    # Align feature names with the training set
    # feature_names = ['Response_Structural_Incomplete', 'Response_Indeterminate', 'Response_Excellent',
    #                  'Nodes_N0', 'Nodes_N1b', 'Age', 'Adenopathy_No', 'Risk_High', 'Risk_Intermediate', 
    #                  'Risk_Low', 'Stage_I']
    # input_df = pd.DataFrame(reshaped_input, columns=feature_names)
    
    # Ensure the feature columns are consistent
    # input_df = input_df.reindex(columns=X_train.columns, fill_value=0)
    
    predicted_class = model.predict(reshaped_input)
    
    return "No chances of getting cancer again 😇😇" if predicted_class[0] == 0 else "Chances of Getting cancer again !!!!!!!! 🤧🤧"

def predict(input_features):
    input_array = np.array(input_features)
    reshaped_input = input_array.reshape(1, -1)
    
    predicted_value = model.predict(reshaped_input)[0]
    return f"{predicted_value:.2f}%"


def main():
    st.title("Wanna Know the Future")
    st.write("Let's Analyze Your Latest Diagnosis Results to Check Your Chances of Getting Cancer Again")

    Age = st.slider("Age", 3, 99)

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

    risk = st.radio('Risk estimate by latest Diagnosis:', ['High', "Intermediate", 'Low'], key="risk")
    Risk_Low = 1 if risk == "Low" else 0
    Risk_Intermediate = 1 if risk == "Intermediate" else 0
    Risk_High = 1 if risk == "High" else 0

    features=[Response_Structural_Incomplete,  Response_Excellent,
                              Nodes_N0, Nodes_N1b,
                              Age, Adenopathy_No,
                              Risk_High, Risk_Intermediate, Risk_Low,
                              Stage_I]#Response_Indeterminate

    if st.button("Check"):
        if method == "Classification":
            result = classify(features)
            st.success(result)
            with st.expander("See Accuracy"):
                y_pred = model.predict(X_test)
                display_accuracy(y_pred, y_test)

        elif method == "Regression":
            result = predict(features)
            st.success(f"Predicted chances: {result}")
            with st.expander("See R² Score"):
                y_pred = model.predict(X_test)
                display_accuracy(y_pred, y_test)

if __name__ == '__main__':
    main()

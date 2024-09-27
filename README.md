# Thyroid Recurrence Prediction App
![Screenshot 2024-09-04 030032](https://github.com/user-attachments/assets/ebe707d4-f30c-4a4f-bb46-1e335bf1e3f9)


# Thyroid Recurrence Prediction App

This project aims to predict the recurrence of thyroid disease using machine learning models such as Random Forest, SVM, and KNN. The application is built with Streamlit for easy user interaction.

## Features
- Predict thyroid recurrence based on patient data
- Multiple ML models for accurate predictions
- Hyperparameter tuning and cross-validation applied for optimal performance

## Tech Stack
- **Python**: Pandas, NumPy, Scikit-learn
- **Streamlit**: Frontend for web app
- **Machine Learning**: Random Forest, SVM, KNN

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/thyroid-recurrence-prediction.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Input patient data (age, TSH levels, etc.).
2. Choose the ML model.
3. Get predictions on the likelihood of thyroid recurrence.

## Models and Tuning
- **Random Forest**: Optimized using GridSearchCV.
- **SVM**: Hyperparameter tuning for kernel selection.
- **KNN**: Cross-validated for best accuracy.

## Future Improvements
- Incorporate more patient features for higher accuracy.
- Add visualization of model performance metrics.

## License
This project is licensed under the MIT License.


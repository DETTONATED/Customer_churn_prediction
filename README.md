# Customer Churn Prediction

## Project Overview

Customer Churn Prediction is a Machine Learning project designed to identify customers who are likely to leave a company. By analyzing customer demographics, account information, and service usage patterns, the model predicts whether a customer will churn or stay.

This project helps businesses improve customer retention strategies and reduce revenue loss.

---

## Dataset Information

The dataset contains customer-related information such as:

- Customer ID
- Gender
- Senior Citizen Status
- Partner Status
- Dependents
- Tenure
- Phone Service
- Internet Service
- Contract Type
- Payment Method
- Monthly Charges
- Total Charges
- Churn Status (Target Variable)

---

## Project Workflow

### 1. Data Collection
- Imported Customer Churn dataset
- Checked dataset structure and data types

### 2. Data Preprocessing
- Handled missing values
- Removed unnecessary columns
- Encoded categorical features
- Scaled numerical features

### 3. Exploratory Data Analysis (EDA)
- Distribution Analysis
- Churn Rate Analysis
- Correlation Heatmap
- Feature Relationships

### 4. Feature Engineering
- Label Encoding
- Feature Selection
- Data Transformation

### 5. Model Building
Machine Learning algorithms used:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Gradient Boosting Classifier
- XGBoost (if applicable)

### 6. Model Evaluation
Evaluation metrics:

- Accuracy Score
- Precision Score
- Recall Score
- F1 Score
- Confusion Matrix
- Classification Report

### 7. Prediction
The trained model predicts whether a customer is likely to:

- Stay
- Churn

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost
- Jupyter Notebook

---

## Project Structure

Customer_Churn/
│
├── data/
│   └── customer_churn.csv
│
├── notebooks/
│   └── Customer_Churn.ipynb
│
├── models/
│   └── churn_model.pkl
│
├── app.py
│
├── requirements.txt
│
└── README.md

---

## Results

The model successfully predicts customer churn based on customer behavior and service usage patterns.

Key insights:

- Customers with month-to-month contracts have higher churn rates.
- Higher monthly charges increase churn probability.
- Long-tenure customers are less likely to churn.
- Electronic check payment users tend to churn more frequently.

---

## Future Improvements

- Hyperparameter Tuning
- Model Deployment using Streamlit/FastAPI
- Real-Time Prediction API
- Advanced Ensemble Models

---

## Author

Badal Raj

Aspiring Data Scientist | Machine Learning Enthusiast

LinkedIn:
https://www.linkedin.com/in/badal-raj-aa3b3423b

GitHub:
https://github.com/yourusername

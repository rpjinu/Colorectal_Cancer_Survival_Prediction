# Colorectal_Cancer_Survival_Prediction
Deploying Colorectal Cancer Survival Prediction API with Streamlit: Train the best model (XGBoost/Random Forest), save it using joblib, and build a Streamlit app to take user inputs  and predict survival status in real-time with an interactive UI. 🚀🎯

<img src="https://github.com/rpjinu/Colorectal_Cancer_Survival_Prediction/blob/main/Project_image.png">

# 🏥 Colorectal Cancer Survival Prediction  

## 📌 Project Overview  
Colorectal cancer is a leading cause of cancer-related deaths worldwide. This project aims to predict **patient survival** based on **clinical, lifestyle, and treatment-related factors** using **machine learning models**.  

## 🎯 Objectives  
- 🏥 **Predict colorectal cancer survival status**  
- 📊 **Perform exploratory data analysis (EDA)**  
- 🏗 **Feature selection & engineering**  
- 🤖 **Train machine learning models (XGBoost & Random Forest)**  
- 🎯 **Evaluate & compare model performance**  
- 🌐 **Deploy the best model using Streamlit API**  

---

## 📂 Dataset Description  
The dataset contains **clinical, lifestyle, and treatment-related features** for patients diagnosed with colorectal cancer.  

### 🔹 Features  
| Feature Name               | Description |
|----------------------------|-------------|
| `Age`                      | Patient's age  |
| `Gender`                   | Male/Female  |
| `Family_History`           | Cancer history in family  |
| `Stage_at_Diagnosis`       | Cancer stage at first diagnosis  |
| `BMI`                      | Body Mass Index  |
| `Smoking_Status`           | Current/Former/Never smoker  |
| `Alcohol_Consumption`      | Regular/Occasional/Never  |
| `Physical_Activity_Level`  | Sedentary/Moderate/Active  |
| `Treatment_Access`         | Availability of medical treatment  |
| `Chemotherapy_Received`    | Whether chemotherapy was received  |
| `Survival_Status`          | **Target Variable** (Survived/Not Survived) |

---

## 🛠 Tech Stack  
- **Programming Language:** 🐍 Python  
- **Data Analysis:** 📊 Pandas, NumPy  
- **Visualization:** 📉 Matplotlib, Seaborn  
- **Machine Learning:** 🤖 Scikit-Learn, XGBoost, Random Forest  
- **Deployment:** 🌐 Streamlit  

---

## 🔍 Exploratory Data Analysis (EDA)  
✔ **Handle missing values**  
✔ **Check data distribution**  
✔ **Visualize correlations using heatmaps**  
✔ **Feature importance analysis**  

---

## 🚀 Model Training  
### 1️⃣ **Data Preprocessing**  
- Encode categorical variables  
- Handle missing values  
- Train-test split (80%-20%)  

### 2️⃣ **Machine Learning Models**  
✔ **Random Forest Classifier** 🌳  
✔ **XGBoost Classifier** 🚀  

### 3️⃣ **Model Evaluation**  
Metrics used to compare models:  
✅ **Accuracy**  
✅ **Precision & Recall**  


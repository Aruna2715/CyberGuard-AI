# 🛡️ CyberGuard AI

## AI-Powered Network Intrusion Detection System

CyberGuard AI is a machine learning-based Network Intrusion Detection System (NIDS) developed using the UNSW-NB15 dataset. The system analyzes network traffic and classifies network connections as either normal traffic or attack traffic.

---

# 👩‍💻 Internship Information

| Field | Details |
|------|------|
| Full Name | Aruna V S |
| Intern ID | CITS5433 |
| Selected For | Machine Learning |
| Organization | CODTECH IT SOLUTIONS PRIVATE LIMITED |
| Duration | 6 Weeks |
| Internship Period | 22 June 2026 – 03 August 2026 |

---

# 📌 Project Name

Network Intrusion Detection using Machine Learning

---

# 🎯 Project Scope

The objective of this project is to develop a machine learning model capable of identifying malicious network traffic.

The project includes:

- Data cleaning
- Data preprocessing
- Feature transformation
- Data visualization
- Model training
- Model evaluation
- Dashboard creation
- Intrusion prediction

---

# 📊 Dataset Information

### Dataset Name

UNSW-NB15 Dataset

### Dataset Statistics

| Dataset | Records | Features |
|------|------:|------:|
| Training Dataset | 175,341 | 45 |
| Testing Dataset | 82,332 | 45 |

### Attack Categories

- Normal
- Generic
- Exploits
- Fuzzers
- DoS
- Reconnaissance
- Analysis
- Backdoor
- Shellcode
- Worms

---

# 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Loaded training and testing datasets.
- Removed the `id` column.
- Removed the `attack_cat` column.
- Separated the `label` column.
- Identified categorical features.
- Applied feature transformation.
- Generated processed datasets.

### Categorical Features

- proto
- service
- state

### Processed Dataset Shape

| Dataset | Shape |
|------|------|
| Training Data | (175341, 194) |
| Testing Data | (82332, 194) |

---

# 🤖 Machine Learning Models

Three machine learning algorithms were used.

### Logistic Regression

- Accuracy: 80.97%
- Precision: 75.35%
- Recall: 97.25%
- F1-score: 84.91%
- ROC-AUC: 95.58%

---

### Random Forest

- Accuracy: 87.14%
- Precision: 81.74%
- Recall: 98.70%
- F1-score: 89.42%
- ROC-AUC: 97.91%

---

### XGBoost

- Accuracy: 87.37%
- Precision: 82.08%
- Recall: 98.60%
- F1-score: 89.58%
- ROC-AUC: 98.43%

---

# 🏆 Final Model

The XGBoost model achieved the highest performance and was selected as the final model for the CyberGuard AI system.

---

# 🖥️ Dashboard Features

The Streamlit dashboard contains four sections.

### 🛡️ Security Overview

- Model accuracy
- Attack recall
- ROC-AUC score
- Model comparison
- System pipeline

### 🔍 Intrusion Detection

- Upload network traffic data
- Detect malicious traffic
- Generate predictions
- Display attack probability

### 📊 Model Analytics

- Performance metrics
- Graphical analysis
- Model comparison

### ℹ️ About Project

- Project overview
- Technologies used
- Dataset summary

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Plotly
- Joblib
- Jupyter Notebook

---

# 📁 Project Structure

```text
Jupyter Home
│
├── Application.py
├── README.md
├── Network Intrusion Detection.ipynb
│
├── models/
│   ├── xgboost_intrusion_model.pkl
│   └── preprocessor.pkl
│
├── Dataset/
│   ├── UNSW_NB15_training-set.csv
│   └── UNSW_NB15_testing-set.csv
│
└── screenshots/
    ├── security_overview.png
    ├── intrusion_detection.png
    ├── prediction_results.png
    ├── model_analytics.png
    └── about_project.png
```

---

# 📸 Screenshots

- Security Overview
- Intrusion Detection
- Prediction Results
- Model Analytics
- About Project

---

# 📦 Project Deliverables

This repository contains:

- Source code
- Dataset files
- Trained model
- Preprocessor
- Jupyter notebook
- Dashboard screenshots
- README file

---

# ✅ Conclusion

CyberGuard AI successfully detects malicious network activity using machine learning techniques.

Among the evaluated models, XGBoost achieved the best performance with:

- Accuracy: 87.37%
- Precision: 82.08%
- Recall: 98.60%
- F1-score: 89.58%
- ROC-AUC: 98.43%

The final model was deployed through a Streamlit dashboard to provide an interactive intrusion detection system.

---

# 👩‍💻 Developed By

**Aruna V S**

**Intern ID:** CITS5433

**Machine Learning Intern**

**CODTECH IT SOLUTIONS PRIVATE LIMITED**
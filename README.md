# 💼 Salary Prediction Using Ensemble Learning

This project predicts salaries based on features like education, experience, company size, etc., using ensemble machine learning models. Built with **Streamlit** for the web app interface and trained using **scikit-learn**.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [How to Run](#-how-to-run)
- [Model Details](#-model-details)
- [Sample Prediction](#-sample-prediction)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

---

## 🔍 Overview

This salary prediction project:
- Uses a dataset sourced from Kaggle.
- Applies preprocessing and feature encoding.
- Trains an ensemble model (Random Forest, VotingClassifier, etc.).
- Deploys using **Streamlit** for real-time predictions.

---

## 🛠 Tech Stack

| Tool             | Usage                  |
|------------------|-------------------------|
| **Python**       | Core programming        |
| **Pandas**       | Data handling           |
| **scikit-learn** | Machine learning        |
| **Streamlit**    | Web app interface       |
| **Pickle**       | Model serialization     |
| **GitHub**       | Version control         |
| **IBM Cloud**    | (Optional) Cloud deployment |

---

## 📁 Project Structure


```
salary_prediction_project/
├── app.py               # Streamlit web app
├── salary_model.pkl     # Trained ML model
├── model_columns.pkl    # Columns used during training
├── requirements.txt     # Python dependencies
├── LICENSE              # MIT License
├── README.md            # Project documentation
└── dataset.csv          # (Optional) Dataset file
```

---

## 🚀 How to Run

### 📌 Prerequisites

- Python 3.x installed  
- Virtual environment (optional but recommended)

### 🔧 Setup Steps

```bash
# Step 1: Navigate to your project directory
cd path/to/salary_prediction_project

# Step 2: Create virtual environment (optional)
python -m venv env
.\env\Scripts\activate   # For Windows
source env/bin/activate  # For macOS/Linux

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the Streamlit app
streamlit run app.py
```

✅ After running the last command, the app will open in your browser at:  
**http://localhost:8501**


---

## 📊 Model Details

The model is trained using ensemble learning techniques to improve prediction accuracy. Specifically:

- **Random Forest Regressor**: Combines multiple decision trees.
- **Voting Regressor**: Averages predictions from multiple models.

### ✅ Features Used:
- Education Level  
- Years of Experience  
- Job Title  
- Employment Type

---

## 🧪 Sample Prediction

| Feature         | Value            |
|----------------|------------------|
| Education       | Master's Degree  |
| Experience      | 5 Years          |
| Job Title       | Data Scientist   |
| Employment Type | Full-time        |

🎯 **Predicted Salary**: ₹12,50,000 annually

---

## 📂 Dataset

The dataset used for this project was sourced from Kaggle:

🔗 https://www.kaggle.com/datasets/rkiattisak/salaly-prediction-for-beginer[Download The Dataset]

It includes features such as:
- Age
- Gender
- Education
- Job Title
- Year of Salry
- Salary

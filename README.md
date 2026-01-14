# Credit Risk Scoring Model

📌 Project Overview

This project develops a machine learning pipeline to predict credit default risk using the German Credit Dataset. As a sophomore Data Science student at CUHK Shenzhen, I built this model to apply statistical learning and data preprocessing techniques to a real-world financial problem.

📊 Key Results

Best Model: Random Forest (Accuracy: 0.74)

Best Interpretability: Logistic Regression (ROC-AUC: 0.75)

Key Risk Factors: Checking Account Status, Duration of Credit, and Credit Amount.

🛠 Tech Stack

Language: Python

Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

Environment: Jupyter Notebook

🧪 Data Pipeline

Cleaning: Handled missing values in Saving and Checking accounts by treating "missing" as a distinct risk category ("none").

Encoding: * Ordinal Encoding for ranked features (Savings, Checking).

One-Hot Encoding for nominal features (Housing, Purpose).

Scaling: Applied StandardScaler to numerical features (Age, Amount, Duration) to ensure model stability.

Handling Imbalance: Utilized class_weight='balanced' to account for the 70/30 distribution of Good/Bad loans.

📈 Business Insights

Based on the Feature Importance analysis:

Customers without a checking account or with "little" balance are significantly higher risk.

Longer credit durations (>24 months) show a strong correlation with default probability.

🚀 How to Run

Clone the repo.

Install dependencies: pip install -r requirements.txt.

Run Credit_Scoring_Model.ipynb.

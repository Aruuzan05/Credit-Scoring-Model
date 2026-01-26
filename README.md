# 🏦 End-to-End Credit Scoring & AI Financial Advisor

> A full-stack Data Science application that predicts creditworthiness using Machine Learning and provides personalized financial advice using Generative AI (Google Gemini).

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Gemini API](https://img.shields.io/badge/AI-Google%20Gemini-orange)

## 📸 Demo
![Dashboard Screenshot](path_to_your_screenshot.png)

## 🚀 Overview
This project bridges traditional Machine Learning with modern Generative AI to solve a fintech problem. It calculates a user's probability of default using a trained **Random Forest/Logistic Regression** model and subsequently uses a Large Language Model (LLM) to act as a **Virtual Financial Advisor**, interpreting the risk factors and suggesting actionable steps for improvement.

### Key Features
* **Credit Prediction Engine:** Real-time credit probability scoring based on user inputs (income, debt, age, etc.).
* **AI Financial Advisor:** Integrated **Google Gemini API** to analyze the specific factors lowering a user's score and generate a natural language improvement plan.
* **Database Integration:** **PostgreSQL** pipeline for robust data storage and retrieval.
* **Interactive UI:** User-friendly web interface built with **Streamlit**.

## 🛠️ Tech Stack
* **Language:** Python
* **Machine Learning:** Scikit-Learn (Logistic Regression, Random Forest), Pandas, NumPy
* **GenAI:** LangChain, Google Gemini API
* **Database:** PostgreSQL, SQLAlchemy
* **Web Framework:** Streamlit

## 📊 Model Performance
* **Algorithm:** Random Forest Classifier
* **Accuracy:** 85% (Example)
* **ROC-AUC:** 0.88 (Example)
* **Key Predictors:** Income, Debt-to-Income Ratio, Credit History Length.

## 💻 Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/yourusername/credit-scoring-app.git](https://github.com/yourusername/credit-scoring-app.git)
    cd credit-scoring-app
    ```

2.  **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables**
    Create a `.env` file in the root directory and add your API keys:
    ```bash
    GOOGLE_API_KEY=your_gemini_api_key_here
    DATABASE_URL=your_postgres_connection_string
    ```

5.  **Run the App**
    ```bash
    streamlit run main.py
    ```

## 📂 Project Structure
```text
├── data/               # Raw and processed datasets
├── models/             # Saved ML models (.pkl files)
├── src/                # Source code for training and evaluation
├── main.py             # Main Streamlit application
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation

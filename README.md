# Credit Guard AI

🛡️ Credit Guard AI: End-to-End Risk Scoring System

An interactive machine learning application that predicts credit default risk, built with a Streamlit frontend and a PostgreSQL database for real-time application logging.

🚀 Key Features

Machine Learning: Random Forest Classifier trained on the German Credit Dataset.

Interactive UI: Dynamic web dashboard for manual credit entry and risk analysis.

Data Persistence: Automatic logging of every application to a local PostgreSQL instance.

Modular Design: Professional Python structure with separation of concerns (UI, Logic, Storage).

🛠 Tech Stack

Languages: Python, SQLFrameworks: Streamlit

ML Libraries: Scikit-learn, Pandas, NumPy

Database: PostgreSQL (SQLAlchemy + Psycopg2)

📁 Repository Structure

├── app.py              # Main Streamlit application

├── credit_data.csv     # Training dataset

├── notebook/

│   └── analysis.ipynb  # Initial EDA and Modeling research

├── requirements.txt    # Python dependencies

└── README.md           # Project documentation

⚙️ Setup & Installation

1. Database Configuration
   
   Ensure you have a PostgreSQL database named finance_db created.
   
   Update the DB_PASS variable in app.py with your local password.
   
3. Environment Setup
   - Clone the repository
     
   git clone [https://github.com/Aruuzan05/Credit-Scoring-Model.git](https://github.com/Aruuzan05/Credit-Scoring-Model.git)

   - Install dependencies
     
    pip install -r requirements.txt
   
4. Run the App
   
   streamlit run app.py
   
📈 Model Performance

The model prioritizes Recall, ensuring that potential high-risk candidates are identified accurately to minimize financial loss for the lender.

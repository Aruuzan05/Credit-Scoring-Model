import streamlit as st 
import pandas as pd 
import numpy as np 
from sqlalchemy import create_engine, text
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler

# 1. CONFIGURATION COMPONENT
MY_PASSWORD = 'Bts20exo'
connection_url = f"postgresql://postgres:{MY_PASSWORD}@localhost:5432/finance_db"

# 2. DATA & MODEL COMPONENT (The "Engine")

@st.cache_resource
def get_model_engine():
    file = 'german_credit_risk.csv'
    df = pd.read_csv(file)

    le = LabelEncoder()
    categorical_cols = ['Sex', 'Housing', 'Saving accounts', 'Checking account', 'Purpose']
    mappings = {}
    
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col].astype(str))
        mappings[col] = dict(zip(le.classes_, le.transform(le.classes_)))

    X = df[['Age', 'Sex', 'Job', 'Housing', 'Saving accounts', 'Checking account', 'Credit amount', 'Duration']]
    y = df['Risk'].map({'good': 0, 'bad': 1})
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model, mappings

# 3. DATABASE COMPONENT (The "Storage")

def log_application_to_db(data_dict):
    try:
        engine = create_engine(connection_url)
        log_df = pd.DataFrame([data_dict])
        log_df.to_sql('application_logs', engine, if_exists = 'append', index = False)
        return True 
    except Exception as e:
        st.error(f"Database Error: {e}")
        return False 
    
# 4. UI COMPONENTS (The "Interface")

def ui_sidebar():
    st.sidebar.title("App Settings")
    st.sidebar.info("Connected to local PostgreSQL")
    st.sidebar.markdown("---")
    st.sidebar.caption("Project by Aruzhan Amangazy")

def ui_input_form(mappings):
    with st.form('credit_form'):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age", 18, 100, 30)
            sex = st.selectbox("Sex", list(mappings['Sex'].keys()))
            job = st.number_input("Job Type (0-3)", 0, 3, 2)
            housing = st.selectbox("Housing", list(mappings['Housing'].keys()))
        with col2:
            saving = st.selectbox("Saving Accounts", list(mappings['Saving accounts'].keys()))
            checking = st.selectbox("Checking Account", list(mappings['Checking account'].keys()))
            amount = st.number_input("Amount ($)", 100, 20000, 5000)
            duration = st.number_input("Duration (Mo)", 1, 72, 24)
        submitted = st.form_submit_button("Run Analysis")
        if submitted:
            return {
                    "age": age, "sex": sex, "job": job, "housing": housing,
                    "saving": saving, "checking": checking, "amount": amount, "duration": duration
            }
    return None 

def ui_display_results(prediction, probability):
    st.divider()
    if prediction == 0:
        st.success(f"✅ **LOW RISK** (Probability: {probability:.2%})")
        return "Good"
    else:
        st.error(f"⚠️ **HIGH RISK** (Probability: {probability:.2%})")
        return "Bad"
    
# 5. MAIN ORCHESTRATOR
def main():
    st.set_page_config(page_title="Credit Guard AI", page_icon="🛡️")
    st.title("🛡️ Credit Guard AI: Modular Edition")
    model, mappings = get_model_engine()
    ui_sidebar()
    
    user_input = ui_input_form(mappings)

    if user_input:
        features = pd.DataFrame([[
            user_input['age'], mappings['Sex'][user_input['sex']], user_input['job'],
            mappings['Housing'][user_input['housing']], mappings['Saving accounts'][user_input['saving']],
            mappings['Checking account'][user_input['checking']], user_input['amount'], user_input['duration']
        ]], columns=['Age', 'Sex', 'Job', 'Housing', 'Saving accounts', 'Checking account', 'Credit amount', 'Duration'])

        pred = model.predict(features)[0]
        prob = model.predict_proba(features)[0][1]

        risk_label = ui_display_results(pred, prob)

        db_record = {
            "age": user_input['age'], 
            "sex": user_input['sex'], 
            "amount": user_input['amount'], 
            "risk_prediction": risk_label, 
            "probability": prob
        }
    
        if log_application_to_db(db_record):
            st.caption("✨ Record synchronized with PostgreSQL.")


if __name__ == "__main__":
    main()
import streamlit as st
import joblib

# Load the model
model = joblib.load("salary_model.pkl")

# --- Page Config ---
st.set_page_config(page_title="Salary Predictor", page_icon="💼", layout="centered")

# --- Custom CSS Styling ---
st.markdown("""
    <style>
    .main {
        background-color: #f2f2f2;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
    }
    .prediction-box {
        padding: 15px;
        background-color: #e0f7fa;
        border-radius: 10px;
        font-size: 24px;
        color: #00796b;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title & Description ---
st.title("💼 Smart Salary Predictor")
st.subheader("🔍 Predict salaries using AI – Instantly!")

st.markdown("Enter the employee details below:")

# --- Input Layout ---
col1, col2 = st.columns(2)

with col1:
    sex = st.selectbox("Gender", ["Male", "Female"])
    designation = st.selectbox("Designation", ["Manager", "Executive", "Staff"])
    unit = st.selectbox("Unit", ["HR", "Sales", "IT", "Finance"])
    age = st.number_input("Age", 18, 70, value=30)

with col2:
    leaves_used = st.number_input("Leaves Used", 0, 30, value=5)
    leaves_remaining = st.number_input("Leaves Remaining", 0, 30, value=5)
    ratings = st.slider("Performance Rating", 1.0, 5.0, value=3.5, step=0.1)
    past_exp = st.number_input("Past Experience (Years)", 0, 40, value=2)

# --- Encoding ---
sex_enc = 1 if sex == "Male" else 0
designation_enc = {"Manager": 2, "Executive": 1, "Staff": 0}[designation]
unit_enc = {"HR": 0, "Sales": 1, "IT": 2, "Finance": 3}[unit]

# --- Predict Button ---
if st.button("🚀 Predict Salary"):
    features = [[sex_enc, designation_enc, unit_enc, age, leaves_used, leaves_remaining, ratings, past_exp]]
    salary = model.predict(features)[0]

    # --- Styled Output ---
    st.markdown(f"""
        <div class="prediction-box">
        💰 <strong>Estimated Salary:</strong> Rs. {salary:,.2f}
        </div>
    """, unsafe_allow_html=True)
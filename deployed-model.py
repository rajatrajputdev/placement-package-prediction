import streamlit as st  # Import Streamlit
from joblib import load  # Import joblib
from numpy import array  # Import numpy

# Load the trained model
model = load("./resources/placement-model.pkl")

# Customizing the page layout
st.set_page_config(page_title="Placement Package Predictor", page_icon="🎓", layout="centered")

# Styling
st.markdown(
    """
    <style>
        .main {
            background-color: #f4f4f4;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        .stTextInput, .stNumberInput, .stButton > button {
            font-size: 16px !important;
        }
        .stNumberInput input {
            padding: 10px;
            border-radius: 5px;
        }
        .stButton > button {
            background-color: #4CAF50 !important;
            color: white !important;
            border-radius: 5px;
            padding: 10px 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App Header
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎓 Placement Package Predictor</h1>", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align: center; font-size: 18px;'>Enter your CGPA to predict the expected placement package.</p>", 
    unsafe_allow_html=True
)

# Input field
gpa = st.number_input("Enter CGPA:", min_value=0.0, max_value=10.0, step=0.1, format="%.1f")

# Predict button
if st.button("Predict Package 💰"):
    input_features = array([[gpa]])
    prediction = model.predict(input_features)[0]
    
    st.markdown(
        f"""<div style='background-color: #DFF0D8; padding: 15px; border-radius: 5px; text-align: center;'>
        <h3 style='color: black'>Predicted Package: <span style='color: #4CAF50;'>{prediction:.2f} LPA</span></h3>
        </div>""",
        unsafe_allow_html=True
    )

import streamlit as st
import pickle
from pathlib import Path
from typing import Any

st.set_page_config(
    page_title="Placement Predictor",
    page_icon="P",
    layout="wide",
    initial_sidebar_state="collapsed",
)


@st.cache_resource
def load_model() -> Any:
    model_path = Path(__file__).with_name("placement.pkl")
    if not model_path.is_file():
        raise FileNotFoundError(f"Model file not found: {model_path}")

    with model_path.open("rb") as model_file:
        return pickle.load(model_file)


data_model = load_model()

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    :root {
        --ink: #172033;
        --muted: #667085;
        --paper: #f7f8fc;
        --card: #ffffff;
        --line: #e6e9f0;
        --accent: #ef6c4d;
        --accent-dark: #c94d32;
        --blue: #5267d9;
    }

    .stApp {
        background: radial-gradient(circle at 85% 0%, #fff0df 0, transparent 32%), var(--paper);
        color: var(--ink);
    }

    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stSidebar"] { display: none; }
    .block-container { max-width: 1120px; padding: 3.5rem 2rem 4rem; }

    .brand { color: var(--accent); font: 700 0.85rem 'Space Grotesk', sans-serif; letter-spacing: .12em; text-transform: uppercase; }
    h1, h2, h3, p, label, .stMarkdown { font-family: 'DM Sans', sans-serif; }
    h1 { color: var(--ink); font: 700 clamp(2.5rem, 5vw, 4.8rem)/.98 'Space Grotesk', sans-serif; letter-spacing: -.055em; margin: .55rem 0 1rem; max-width: 720px; }
    .intro { color: var(--muted); font-size: 1.08rem; line-height: 1.65; max-width: 570px; margin-bottom: 2.5rem; }
    .panel { background: var(--card); border: 1px solid var(--line); border-radius: 22px; box-shadow: 0 18px 50px rgba(32, 43, 75, .08); padding: 2rem 2.2rem 1.5rem; }
    .eyebrow { color: var(--blue); font: 700 .75rem 'Space Grotesk', sans-serif; letter-spacing: .13em; text-transform: uppercase; margin-bottom: .6rem; }
    .panel h2 { color: var(--ink); font: 600 1.45rem 'Space Grotesk', sans-serif; margin: 0 0 .35rem; }
    .hint { color: var(--muted); font-size: .93rem; margin: 0 0 1.5rem; }
    [data-testid="stNumberInput"] label { color: var(--ink); font-weight: 600; }
    [data-testid="stNumberInput"] input { background-color: #ffffff; border-color: var(--line); border-radius: 10px; color: var(--ink) !important; -webkit-text-fill-color: var(--ink); font-size: 1.05rem; }
    [data-testid="stNumberInput"] input:focus { border-color: var(--accent); box-shadow: 0 0 0 1px var(--accent); }
    [data-testid="stNumberInput"] button { background-color: #ffffff; color: var(--ink); }
    [data-testid="stNumberInput"] button:hover { background-color: #fff0df; color: var(--accent-dark); }
    .stButton > button { background: var(--accent); border: 0; border-radius: 10px; color: white; font-weight: 700; min-height: 2.7rem; padding: 0 1.6rem; transition: all .2s ease; }
    .stButton > button:hover { background: var(--accent-dark); box-shadow: 0 8px 20px rgba(239, 108, 77, .25); color: white; transform: translateY(-1px); }
    .result { background: #172033; border-radius: 18px; color: white; margin-top: 1.3rem; padding: 1.4rem 1.6rem; }
    .result-label { color: #b9c0d4; font-size: .78rem; letter-spacing: .1em; text-transform: uppercase; }
    .result-value { color: #ffb49f; font: 700 2rem 'Space Grotesk', sans-serif; margin-top: .3rem; }
    .side-note { border-left: 3px solid var(--accent); color: var(--muted); font-size: .95rem; line-height: 1.65; margin: 4rem 0 0 1.4rem; padding-left: 1.2rem; }
    @media (max-width: 700px) { .block-container { padding: 2rem 1rem 3rem; } .panel { padding: 1.4rem; } .side-note { margin: 1.5rem 0 0; } }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="brand">Academic intelligence</div>', unsafe_allow_html=True)
st.title("See where your CGPA can take you.")
st.markdown(
    '<p class="intro">Get a quick placement score estimate from your academic performance. Adjust your CGPA below and explore your predicted result.</p>',
    unsafe_allow_html=True,
)

left, right = st.columns([1.45, 1], gap="large")
with left:
    st.markdown(
        '<div class="panel"><div class="eyebrow">01 / Your profile</div><h2>Enter your academic score</h2><p class="hint">Type your current CGPA below.</p>',
        unsafe_allow_html=True,
    )
    data = st.number_input("CGPA", min_value=0.0, max_value=10.0, value=6.63, step=0.01, format="%.2f")
    if st.button("Calculate placement score", type="primary"):
        prediction = data_model.predict([[data]])
        st.markdown(
            f'<div class="result"><div class="result-label">Predicted placement score</div><div class="result-value">{prediction[0]:.2f}</div></div>',
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown(
        '<div class="side-note"><strong>A clearer next step.</strong><br><br>This estimate is a starting point for understanding how your academic performance may influence placement outcomes.</div>',
        unsafe_allow_html=True,
    )
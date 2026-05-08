import streamlit as st
import pandas as pd
import plotly.express as px
import time

# --- Page Configuration ---
st.set_page_config(page_title="CareMate | Innovating Elderly Care", layout="wide")

# --- Custom Styles ---
st.markdown("""
    <style>
    .main { background-color: #f0f8ff; }
    h1 { 
        color: #003366; 
        font-size: 3.5rem; 
        font-weight: 900; 
        text-transform: uppercase;
        margin-bottom: 0px;
    }
    h2 { color: #1f77b4; border-bottom: 3px solid #1f77b4; padding-bottom: 5px; font-weight: 700; margin-top: 30px;}
    .stButton>button { background-color: #1f77b4; color: white; border-radius: 20px; font-weight: bold; }
    .feature-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        border-left: 10px solid #1f77b4;
    }
    .step-box {
        background-color: #ffffff;
        border: 2px solid #1f77b4;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        color: #003366;
        min-height: 80px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .arrow {
        text-align: center;
        font-size: 2rem;
        color: #1f77b4;
        line-height: 80px;
    }
    .logo-text {
        font-size: 1.2rem;
        color: #1f77b4;
        font-weight: bold;
        letter-spacing: 2px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar Configuration ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=150)
    st.title("CareMate Hub")
    st.markdown("### Project Vision")
    st.write("Redefining medical accompaniment through AI and Empathy.")
    st.markdown("---")
    st.write("**Core Team:**")
    st.info("Wan-Ning Tseng\n\nBo-Ying Zhang")
    
    st.write("Project Readiness")
    st.progress(85)
    st.caption("Phase: NTHU Startup Garage Finalist")

# --- Header Section ---
title_container = st.container()
with title_container:
    st.markdown('<p class="logo-text">CARE MATE SOLUTIONS</p>', unsafe_allow_html=True)
    st.title("CareMate: The Future of Elderly Medical Care")
    st.subheader("Transforming Loneliness into Professional Companionship")
    st.write("---")

# --- Section 1: Crisis Analysis ---
st.header("1. The Critical Crisis: Why CareMate Exists")
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("### The Aging Tsunami")
    st.write("""
    Taiwan is on the brink of a historic demographic shift. By 2025, one in every five citizens will be over 65. 
    Currently, there are over 4 million seniors, and more than 60% suffer from chronic conditions. 
    The reality of modern society is harsh:
    - **Dual-Income Stress:** 70% of households are dual-income, making frequent leave impossible.
    - **The Sandwich Generation:** Middle-aged professionals are crushed by dual care responsibilities.
    - **Geographical Barriers:** Distance prevents children from navigating complex hospital systems with parents.
    """)
with col2:
    st.info("### The Failure of Current Systems")
    st.write("""
    1. **Home Caregivers:** Chronically undersupplied and expensive for short visits.
    2. **Personal Agents:** Lack background checks and formal accountability.
    3. **Migrant Workers:** Face severe language barriers in clinical settings.
    4. **Volunteers:** Lack the schedule consistency required for medical follow-ups.
    """)

# --- Section 2: Visualized Operational Flow ---
st.header("2. Visualized Operational Journey")
st.write("Our systematic approach ensures every medical visit is tracked, secure, and professional.")

# Flowchart implementation using columns
flow_col1, arrow1, flow_col2, arrow2, flow_col3, arrow3, flow_col4 = st.columns([3, 1, 3, 1, 3, 1, 3])

with flow_col1:
    st.markdown('<div class="step-box">1. Demand Submission & Health Profile</div>', unsafe_allow_html=True)
with arrow1:
    st.markdown('<div class="arrow">➔</div>', unsafe_allow_html=True)
with flow_col2:
    st.markdown('<div class="step-box">2. AI-Powered Smart Matching</div>', unsafe_allow_html=True)
with arrow2:
    st.markdown('<div class="arrow">➔</div>', unsafe_allow_html=True)
with flow_col3:
    st.markdown('<div class="step-box">3. Digital Contract & Escrow Payment</div>', unsafe_allow_html=True)
with arrow3:
    st.markdown('<div class="arrow">➔</div>', unsafe_allow_html=True)
with flow_col4:
    st.markdown('<div class="step-box">4. Biometric Check-in & Departure</div>', unsafe_allow_html=True)

# Second row of the flow
st.write("") 
flow_col5, arrow4, flow_col6, arrow5, flow_col7, arrow6, flow_col8 = st.columns([3, 1, 3, 1, 3, 1, 3])

with flow_col5:
    st.markdown('<div class="step-box">5. Clinical Support & Medical Recording</div>', unsafe_allow_html=True)
with arrow4:
    st.markdown('<div class="arrow">➔</div>', unsafe_allow_html=True)
with flow_col6:
    st.markdown('<div class="step-box">6. Safe Return & Final Geofencing</div>', unsafe_allow_html=True)
with arrow5:
    st.markdown('<div class="arrow">➔</div>', unsafe_allow_html=True)
with flow_col7:
    st.markdown('<div class="step-box">7. Family Debrief & Health Report</div>', unsafe_allow_html=True)
with arrow6:
    st.markdown('<div class="arrow">➔</div>', unsafe_allow_html=True)
with flow_col8:
    st.markdown('<div class="step-box">8. Automated Settlement & Payout</div>', unsafe_allow_html=True)

# --- Section 3: Innovative Ecosystem ---
st.header("3. Service Infrastructure")
tab1, tab2, tab3 = st.tabs(["Service Packages", "Smart Matching", "Safety Protocol"])
with tab1:
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown('<div class="feature-card"><h3>Basic Support</h3><p>Registration assistance and clinical transcription for complete family transparency.</p></div>', unsafe_allow_html=True)
    with col_b:
        st.markdown('<div class="feature-card"><h3>Premium Transit</h3><p>Barrier-free fleet integration with real-time GPS monitoring.</p></div>', unsafe_allow_html=True)
    with col_c:
        st.markdown('<div class="feature-card"><h3>Health Ledger</h3><p>Automated digital health records synchronized across devices.</p></div>', unsafe_allow_html=True)
with tab2:
    st.write("### AI Matching Simulation")
    if st.button("Simulate AI Matching"):
        with st.spinner('Syncing...'):
            time.sleep(1.5)
            st.success("Optimal Caregiver Match Found.")
with tab3:
    st.write("### Safety Framework")
    st.write("- **QR Biometrics:** Secure identity verification.\n- **Geofencing:** Route deviation alerts.\n- **Escrow:** Payment security.")

# --- Section 4: Market & Financials ---
st.header("4. Financial Viability")
col_l, col_r = st.columns(2)
with col_l:
    market_data = pd.DataFrame({
        "Category": ["Seniors", "Chronic", "Target", "Initial"],
        "Value (K)": [4000, 2400, 900, 180]
    })
    st.plotly_chart(px.funnel(market_data, x='Value (K)', y='Category', title="Market Funnel"), use_container_width=True)
with col_r:
    exp_data = {"Platform": 100000, "Marketing": 100000, "HR": 20000, "Admin": 1565000, "Reserve": 60000}
    st.plotly_chart(px.pie(values=list(exp_data.values()), names=list(exp_data.keys()), hole=0.4, title="Budget Allocation"), use_container_width=True)

# --- Footer ---
st.markdown("---")
st.write("### CareMate: Empowering Families, Protecting Seniors.")
st.caption("Copyright 2026 CareMate Strategic Planning Team | NTHU")

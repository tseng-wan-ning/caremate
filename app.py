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
    /* Blue Bold Title */
    h1 { 
        color: #003366; 
        font-size: 3.5rem; 
        font-weight: 900; 
        text-transform: uppercase;
        margin-bottom: 0px;
    }
    h2 { color: #1f77b4; border-bottom: 3px solid #1f77b4; padding-bottom: 5px; font-weight: 700; }
    .stButton>button { background-color: #1f77b4; color: white; border-radius: 20px; font-weight: bold; }
    .feature-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        border-left: 10px solid #1f77b4;
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
    # Logo Placeholder & Branding
    st.markdown('<p class="logo-text">CARE MATE SOLUTIONS</p>', unsafe_allow_html=True)
    st.title("CareMate: The Future of Elderly Medical Care")
    st.subheader("Transforming Loneliness into Professional Companionship")
    st.write("---")

# --- Section 1: Critical Crisis Analysis ---
st.header("1. The Critical Crisis: Why CareMate Exists")
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### The Aging Tsunami")
    st.write("""
    Taiwan is on the brink of a historic demographic shift. By 2025, one in every five citizens will be over 65. 
    This is a daily crisis for millions of families. Currently, there are over 4 million 
    seniors, and more than 60% suffer from chronic conditions like hypertension, diabetes, or heart disease. 
    These conditions require consistent, high-frequency medical follow-ups.
    
    The reality of modern society is harsh:
    - **Dual-Income Stress:** 70% of households are dual-income. Taking a day off for a 4-hour hospital wait is a luxury many families cannot afford.
    - **The Sandwich Generation:** Middle-aged professionals are crushed between career demands and the needs of their aging parents.
    - **Geographical Barriers:** Many children live in different cities or abroad, leaving their parents to navigate complex hospital systems alone.
    """)

with col2:
    st.info("### The Failure of Current Systems")
    st.write("""
    Why don't current solutions work?
    1. **Home Caregivers:** Chronically undersupplied. Hourly rates are often prohibitive for simple hospital visits.
    2. **Personal Agents:** Found through word-of-mouth, these lack background checks and formal rating systems.
    3. **Migrant Workers:** Face severe language barriers in medical settings, which can lead to misinterpretation of clinical instructions.
    4. **Volunteers:** Lack the schedule consistency required for critical diagnostic appointments.
    """)

# --- Section 2: Service Ecosystem ---
st.header("2. Our Innovative Ecosystem")
st.write("CareMate is a full-service infrastructure designed for safety and institutional efficiency.")

tab1, tab2, tab3 = st.tabs(["Service Packages", "Smart Matching", "Safety Protocol"])

with tab1:
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown('<div class="feature-card"><h3>Basic Support</h3><p>Registration assistance, clinical accompaniment, and real-time medical recording to ensure family members stay informed.</p></div>', unsafe_allow_html=True)
    with col_b:
        st.markdown('<div class="feature-card"><h3>Premium Transit</h3><p>Integration with barrier-free transportation fleets. Includes door-to-door escorting with GPS monitoring.</p></div>', unsafe_allow_html=True)
    with col_c:
        st.markdown('<div class="feature-card"><h3>Health Ledger</h3><p>A digital health resume tracking medication changes and future appointments automatically.</p></div>', unsafe_allow_html=True)

with tab2:
    st.write("### How the AI Matching Works")
    st.write("""
    Our proprietary algorithm uses a Triple-Check Logic:
    - **Qualification Layer:** Mandatory verification of caregiver certifications and background checks.
    - **Compatibility Layer:** Matches language proficiency (Hakka, Taiwanese, Mandarin) to ensure patient comfort.
    - **Efficiency Layer:** Optimizes caregiver routes to minimize transit time and costs.
    """)
    if st.button("Simulate AI Matching Process"):
        with st.spinner('Analyzing caregiver database...'):
            time.sleep(2)
            st.success("Match Found: 98% Compatibility with Professional Caregiver")

with tab3:
    st.write("### Absolute Safety Framework")
    st.write("""
    We treat security as our core priority:
    - **QR Biometrics:** Double-blind verification between caregiver and patient to start the service.
    - **Geofencing:** System alerts if the transit route deviates from the pre-planned hospital path.
    - **Escrow Payments:** Funds are released only after the family reviews the final medical report.
    """)

# --- Section 3: Financial & Market Analysis ---
st.header("3. Financial Viability and Scalability")

col_left, col_right = st.columns([1, 1])

with col_left:
    st.write("### Market Potential")
    market_data = pd.DataFrame({
        "Category": ["Total Seniors", "Chronic Patients", "Target Families", "Initial Users"],
        "Population (K)": [4000, 2400, 900, 180]
    })
    fig_market = px.funnel(market_data, x='Population (K)', y='Category', title="Market Conversion Funnel")
    st.plotly_chart(fig_market, use_container_width=True)

with col_right:
    st.write("### Annual Expenditure Detail")
    exp_data = {
        "Platform Development": 100000,
        "Marketing Operations": 100000,
        "HR and Training": 20000,
        "Admin and Rent": 1565000,
        "Emergency Fund": 60000
    }
    df_exp = pd.DataFrame(list(exp_data.items()), columns=['Item', 'Cost'])
    fig_exp = px.pie(df_exp, values='Cost', names='Item', hole=0.4, color_discrete_sequence=px.colors.sequential.Blues_r)
    st.plotly_chart(fig_exp, use_container_width=True)

# --- Section 4: Operational Workflow ---
st.header("4. Detailed Implementation and Operations")
with st.expander("Click to view Full Operational Manual", expanded=True):
    st.write("""
    **Phase 1: Pre-Service Preparation**
    - User Registration: Comprehensive upload of medical history and mobility status.
    - Caregiver Training: Mandatory 40-hour training covering hospital navigation and emergency response.
    
    **Phase 2: The Accompaniment Journey**
    - Check-in: GPS logging at the residence and patient identification.
    - Hospital Navigation: Managing kiosk registration and clinic wait times.
    - Digital Transcription: Real-time recording of doctor instructions for family review.
    
    **Phase 3: Post-Service Integration**
    - Safe Return: Final GPS check-out at the senior's residence.
    - Family Debrief: Detailed report containing clinical findings and next appointment dates.
    - Settlement: Automated billing and caregiver compensation.
    """)

# --- Footer ---
st.markdown("---")
st.write("### CareMate: Empowering Families, Protecting Seniors.")
st.caption("Copyright 2026 CareMate Strategic Planning Team | National Tsing Hua University")

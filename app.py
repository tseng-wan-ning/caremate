import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="CareMate Executive Summary",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- PROFESSIONAL CSS (CORPORATE STYLE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #2c3e50;
    }
    .main {
        background-color: #ffffff;
    }
    .stAlert {
        border-radius: 2px;
        border: none;
        background-color: #f8f9fa;
    }
    h1, h2, h3 {
        color: #1a3a5f;
        font-weight: 600;
        border-bottom: 2px solid #e9ecef;
        padding-bottom: 10px;
    }
    .metric-card {
        background-color: #f1f4f9;
        padding: 20px;
        border-left: 5px solid #1a3a5f;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- TITLE SECTION ---
st.title("CareMate: Professional Medical Accompaniment Platform")
st.markdown("**Executive Business Proposal | Strategic Planning 2026**")
st.markdown("*Prepared by: Wan-Ning Tseng (112071077), Bo-Ying Zhang (112072172)*")

# --- SECTION 1: CORE STRATEGY ---
st.header("I. Strategic Vision & Core Values")
col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Mission Statement")
    st.write("""
    As Taiwan transitions into a super-aged society, the gap between elderly healthcare needs and family 
    support availability has widened significantly. CareMate provides a secure, institutionalized 
    platform for medical accompaniment, ensuring that seniors receive professional care while 
    alleviating the career and psychological pressures on the younger generation.
    """)
with col2:
    st.subheader("Core Values")
    st.write("- **Professional Trust:** Rigorous screening & audit.")
    st.write("- **Safety Infrastructure:** Real-time tracking & data logging.")
    st.write("- **Dignified Care:** Empathy-driven senior support.")

# --- SECTION 2: MARKET ANALYSIS & QUANTITATIVE DATA ---
st.header("II. Market Analysis & Demand Forecast")
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("Elderly Population", "20% (2025E)", "Super-aged Threshold")
with m2:
    st.metric("Chronic Disease Base", "2.4M Patients", "Target Market")
with m3:
    st.metric("Annual Caregiver Loss", "130,000+", "Labor Shortage")
with m4:
    st.metric("Dual-Income Ratio", "70%", "Demand Driver")

with st.container():
    st.write("#### Pain Point Analysis: Structural Gaps in Care")
    st.table(pd.DataFrame({
        "Current Solutions": ["Domestic Helpers", "Personal Agents", "Migrant Workers", "Volunteers"],
        "Critical Shortcomings": [
            "Fixed schedules, high overhead",
            "Lack of rating systems, low transparency",
            "Communication barriers, limited medical literacy",
            "Unstable availability, non-standardized quality"
        ]
    }))

# --- SECTION 3: OPERATIONAL ARCHITECTURE ---
st.header("III. Operational Infrastructure & Service Flow")
st.write("#### Integrated Medical Accompaniment System (IMAS)")

# Highlighting the 8 stages with a professional expander
with st.expander("Detailed System Architecture & Workflow (8 Stages)", expanded=True):
    st.markdown("""
    1. **Demand Acquisition:** Users submit profile, health history, and specific requirements (Language/Gender).
    2. **AI Matching Engine:** Triple-layer filter (Certification, Availability, Historical Rating).
    3. **Verification & Escrow:** Digital contract signing and deposit freeze via integrated payment gateways.
    4. **Deployment:** GPS geofencing triggers upon arrival; caregiver identity verified via QR biometrics.
    5. **Clinical Management:** Real-time logging of physician instructions, billing codes, and prescription data.
    6. **Rehabilitation Log:** Post-consultation report generation including follow-up scheduling.
    7. **Validation:** Bi-directional rating system and automated health file updates.
    8. **Financial Settlement:** Automated reconciliation of base fees, mileage, and medical advances.
    """)

# Service Classification Table
st.write("#### Service Categorization & Human Capital")
c1, c2 = st.columns(2)
with c1:
    st.write("**Caregiver Tiers**")
    st.write("- **Type A (Certified):** NT$500-800/hr (Professional caregivers)")
    st.write("- **Type B (Medical Interns):** NT$300-450/hr (Medical/Nursing students)")
    st.write("- **Type C (Retired Experts):** NT$450-650/hr (Retired Nurses/Social Workers)")
with c2:
    st.write("**Operational Features**")
    st.write("- **Fleet Management:** Partnership with Uber/Barrier-free taxi services.")
    st.write("- **Smart Reminders:** Automated LINE notifications for follow-up & medication.")
    st.write("- **Digital Ledger:** Secure storage of medical records & history.")

# --- SECTION 4: FINANCIALS & GROWTH MODEL ---
st.header("IV. Financial Projections & Business Model")
col_f1, col_f2 = st.columns([1, 1])

with col_f1:
    st.write("#### Revenue Architecture")
    revenue_data = pd.DataFrame({
        "Revenue Stream": ["Service Fees", "Matching Commission (30%)", "B2B Partnership", "Gov. Grants"],
        "Weight": [60, 25, 10, 5]
    })
    fig = px.pie(revenue_data, values='Weight', names='Revenue Stream', 
                 color_discrete_sequence=['#1a3a5f', '#2c3e50', '#5a7d9a', '#a9c0d3'])
    fig.update_layout(showlegend=True, margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig, use_container_width=True)

with col_f2:
    st.write("#### Annual Capital Requirements")
    budget_data = {
        "Platform Development": 100000,
        "Marketing & Acquisition": 100000,
        "HR & Training Operations": 20000,
        "Admin & Infrastructure": 1565000,
        "Operations Reserve": 60000
    }
    st.bar_chart(pd.Series(budget_data))
    st.markdown("**Total Projected Capital: TWD 1,845,000 / Year**")

# --- SECTION 5: COMPETITIVE ADVANTAGE ---
st.header("V. Competitive Advantage & Social Impact")
st.write("""
- **Technological Barrier:** AI matching algorithms and blockchain-verified certifications.
- **Service Standardization:** Uniform training protocols and multi-language support (Mandarin, Taiwanese, Hakka, English).
- **ESG Alignment:** Direct contribution to UN Sustainable Development Goal 3 (Good Health and Well-being).
""")

st.markdown("---")
st.caption("© 2026 CareMate Strategic Planning Team | Confidential & Proprietary")

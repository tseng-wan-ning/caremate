import streamlit as st
import pandas as pd
import plotly.express as px
import time

# --- Page Configuration ---
st.set_page_config(page_title="CareMate | Strategic Business Proposal", layout="wide")

# --- Advanced CSS for Consulting Style ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    /* Royal Blue Title Style */
    h1 { 
        color: #002366; 
        font-size: 3.8rem; 
        font-weight: 900; 
        letter-spacing: -1px;
        margin-bottom: 0px;
    }
    h2 { 
        color: #1f77b4; 
        border-bottom: 2px solid #e1e4e8; 
        padding-bottom: 10px; 
        font-weight: 700; 
        margin-top: 50px;
    }
    .stButton>button { 
        background: linear-gradient(90deg, #003366 0%, #1f77b4 100%); 
        color: white; border: none; padding: 10px 25px; border-radius: 4px; font-weight: bold;
    }
    .info-card {
        background-color: #f8f9fa;
        padding: 30px;
        border-radius: 4px;
        border-top: 4px solid #002366;
        height: 100%;
    }
    .value-box {
        background-color: #002366;
        color: white;
        padding: 20px;
        border-radius: 4px;
        text-align: center;
    }
    .step-box {
        background-color: #eef4f9;
        border: 1px solid #1f77b4;
        padding: 15px;
        border-radius: 4px;
        text-align: center;
        font-size: 0.9rem;
        color: #002366;
        font-weight: 600;
        height: 100px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .logo-text {
        font-size: 1.2rem;
        color: #1f77b4;
        font-weight: bold;
        letter-spacing: 3px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.title("Project Dashboard")
    st.markdown("---")
    st.write("**Core Team**")
    st.info("Wan-Ning Tseng | Bo-Ying Zhang")
    st.write("**Institutional Affiliation**")
    st.write("National Tsing Hua University")
    st.markdown("---")
    st.write("**Status: Finalist**")
    st.progress(85)

# --- Header with Logo & Royal Blue Title ---
title_container = st.container()
with title_container:
    col_logo, col_empty = st.columns([1, 8])
    with col_logo:
        # 這裡放置專案 Logo 圖示
        st.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=80)
    
    st.markdown('<p class="logo-text">CARE MATE SOLUTIONS 2026</p>', unsafe_allow_html=True)
    st.title("CareMate: Strategic Medical Accompaniment")
    st.subheader("An Institutional Response to Taiwan's Aging Society Crisis")
    st.write("---")

# --- Section 1: The Crisis ---
st.header("I. Market Dynamics & The Silver Crisis")
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("#### Structural Demographic Shift")
    st.write("""
    Taiwan’s entry into a super-aged society is not merely a demographic transition; it is a structural shock to the national healthcare infrastructure. By 2025, over 20% of the population will be over 65, creating a critical bottleneck in outpatient management. 
    
    The crisis is multifaceted:
    1. **Medical Complexity:** 60% of seniors handle 3+ chronic conditions, requiring high-frequency hospital visits.
    2. **Workforce Erosion:** 130,000 professional workers quit annually for elderly care, causing a multi-billion TWD productivity loss.
    3. **The Urban Displacement:** Children are increasingly decoupled from their parents' residential districts, making immediate accompaniment logistically impossible.
    """)
    st.markdown('<div class="value-box">Target Market: 1.8M High-Frequency Patients</div>', unsafe_allow_html=True)

with col2:
    st.markdown("#### Quantitative Market Funnel")
    market_df = pd.DataFrame({
        "Stage": ["Total Elderly", "Chronic Patients", "Care Gap Households", "Addressable Market"],
        "Value": [4000, 2400, 900, 180]
    })
    st.plotly_chart(px.funnel(market_df, x='Value', y='Stage', color_discrete_sequence=['#002366']), use_container_width=True)

# --- Section 2: Visualized Operational Workflow ---
st.header("II. Operational Flow & Service Architecture")
st.write("Ensuring a seamless transition from home to hospital with real-time institutional oversight.")

# Row 1 of Flow
f1, a1, f2, a2, f3, a3, f4 = st.columns([3, 1, 3, 1, 3, 1, 3])
f1.markdown('<div class="step-box">1. Profile & Health Ledger Creation</div>', unsafe_allow_html=True)
a1.markdown('<h2 style="border:none; text-align:center; margin:0;">→</h2>', unsafe_allow_html=True)
f2.markdown('<div class="step-box">2. AI Matching & Vetting Engine</div>', unsafe_allow_html=True)
a2.markdown('<h2 style="border:none; text-align:center; margin:0;">→</h2>', unsafe_allow_html=True)
f3.markdown('<div class="step-box">3. Digital Escrow & Contract Secure</div>', unsafe_allow_html=True)
a3.markdown('<h2 style="border:none; text-align:center; margin:0;">→</h2>', unsafe_allow_html=True)
f4.markdown('<div class="step-box">4. Biometric Identity Verification</div>', unsafe_allow_html=True)

# Row 2 of Flow
st.write("")
f5, a4, f6, a5, f7, a6, f8 = st.columns([3, 1, 3, 1, 3, 1, 3])
f5.markdown('<div class="step-box">5. Clinical Support & Transcription</div>', unsafe_allow_html=True)
a4.markdown('<h2 style="border:none; text-align:center; margin:0;">→</h2>', unsafe_allow_html=True)
f6.markdown('<div class="step-box">6. Safe Return & Geofencing Check</div>', unsafe_allow_html=True)
a5.markdown('<h2 style="border:none; text-align:center; margin:0;">→</h2>', unsafe_allow_html=True)
f7.markdown('<div class="step-box">7. Digital Debrief & Family Report</div>', unsafe_allow_html=True)
a6.markdown('<h2 style="border:none; text-align:center; margin:0;">→</h2>', unsafe_allow_html=True)
f8.markdown('<div class="step-box">8. Automated Reconciliation & Payout</div>', unsafe_allow_html=True)

# --- Section 3: Competitive Strategy Matrix ---
st.header("III. Competitive Advantage & Comparison")
comp_data = {
    "Feature": ["Vetting Process", "Real-time GPS", "Medical Recording", "Insurance Coverage", "Pricing Transparency"],
    "CareMate": ["Rigorous/Institutional", "Yes (Real-time)", "Professional Transcription", "Comprehensive", "High (Standardized)"],
    "Traditional Agency": ["Minimal/None", "No", "Verbal Only", "Partial", "Low (Varies)"],
    "Volunteers": ["Variable", "No", "Unreliable", "None", "Free"]
}
st.table(pd.DataFrame(comp_data))

# --- Section 4: Revenue & Financial Sustainability ---
st.header("IV. Financial Sustainability Model")
col_rev, col_exp = st.columns(2)

with col_rev:
    st.write("#### Revenue Diversification")
    rev_data = pd.DataFrame({
        "Stream": ["Direct Fees", "Commissions", "B2B Partnership", "Gov Contracts"],
        "Share": [60, 25, 10, 5]
    })
    st.plotly_chart(px.pie(rev_data, values='Share', names='Stream', hole=0.5, color_discrete_sequence=px.colors.sequential.Blues_r), use_container_width=True)

with col_exp:
    st.write("#### Annual Budget Allocation (TWD)")
    exp_data = {"R&D": 100000, "Marketing": 100000, "HR": 20000, "Operations": 1565000, "Reserve": 60000}
    st.bar_chart(pd.Series(exp_data))

# --- Section 5: The "CareMate" Business Canvas ---
st.header("V. Strategic Business Canvas")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="info-card"><b>Key Partners</b><br>Hospital Social Work Depts<br>Uber/Taxi Fleets<br>Insurance Providers</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="info-card"><b>Value Proposition</b><br>Peace of mind for families<br>Dignity for seniors<br>Standardized care protocols</div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="info-card"><b>Customer Segments</b><br>Dual-income professionals<br>Overseas Taiwanese<br>Single-living seniors</div>', unsafe_allow_html=True)

# --- Detailed Manual ---
st.header("VI. Detailed Operational Appendix")
with st.expander("Explore Comprehensive Implementation Manual"):
    st.write("""
    **I. Caregiver Recruitment & Audit:** 
    Our recruitment is decentralized yet strictly audited. We prioritize certified nursing assistants and medical students from top-tier universities. Each candidate undergoes a psychological assessment and a 40-hour 'Compassion & Logistics' training module.
    
    **II. The Tech Stack:** 
    CareMate utilizes a hybrid cloud architecture. The AI matching engine processes over 50 variables per request, including linguistic compatibility (Mandarin, Taiwanese, Hakka) and specific medical expertise required for the visit.
    
    **III. Post-Service Analytics:** 
    We don't just finish a visit; we create a data loop. Every visit generates a structured data point that helps families track long-term health trends, which can be shared with primary physicians for better diagnostic outcomes.
    """)

# --- Footer ---
st.markdown("---")
st.caption("© 2026 CareMate Strategic Planning Team | National Tsing Hua University | Confidential Business Proposal")

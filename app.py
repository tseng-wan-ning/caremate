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
    h1 { 
        color: #002366; 
        font-size: 3.8rem; 
        font-weight: 900; 
        letter-spacing: -1px;
        margin-top: 0px;
        margin-bottom: 10px;
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
        color: white; border: none; padding: 12px 25px; border-radius: 4px; font-weight: bold; width: 100%;
    }
    .info-card {
        background-color: #f8f9fa;
        padding: 30px;
        border-radius: 4px;
        border-top: 4px solid #002366;
        height: 100%;
    }
    .calculator-box {
        background-color: #eef4f9;
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #1f77b4;
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
        margin-bottom: -10px;
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
    st.write("**Project Readiness**")
    st.progress(85)

# --- Header Section ---
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
    Taiwan’s entry into a super-aged society by 2025 creates a critical bottleneck in outpatient management. 
    1. **Medical Complexity:** 60% of seniors handle 3+ chronic conditions.
    2. **Workforce Erosion:** 130,000 workers quit annually for elderly care.
    3. **Urban Displacement:** Children are decoupled from their parents' residential districts.
    """)
with col2:
    market_df = pd.DataFrame({
        "Stage": ["Total Elderly", "Chronic Patients", "Care Gap Households", "Addressable Market"],
        "Value": [4000, 2400, 900, 180]
    })
    st.plotly_chart(px.funnel(market_df, x='Value', y='Stage', color_discrete_sequence=['#002366']), use_container_width=True)

# --- Section 2: Visualized Operational Workflow ---
st.header("II. Operational Flow & Service Architecture")
f1, a1, f2, a2, f3, a3, f4 = st.columns([3, 1, 3, 1, 3, 1, 3])
f1.markdown('<div class="step-box">1. Profile & Health Ledger Creation</div>', unsafe_allow_html=True)
a1.markdown('<h2 style="border:none; text-align:center; margin:0;">→</h2>', unsafe_allow_html=True)
f2.markdown('<div class="step-box">2. AI Matching & Vetting Engine</div>', unsafe_allow_html=True)
a2.markdown('<h2 style="border:none; text-align:center; margin:0;">→</h2>', unsafe_allow_html=True)
f3.markdown('<div class="step-box">3. Digital Escrow & Contract Secure</div>', unsafe_allow_html=True)
a3.markdown('<h2 style="border:none; text-align:center; margin:0;">→</h2>', unsafe_allow_html=True)
f4.markdown('<div class="step-box">4. Biometric Identity Verification</div>', unsafe_allow_html=True)

st.write("")
f5, a4, f6, a5, f7, a6, f8 = st.columns([3, 1, 3, 1, 3, 1, 3])
f5.markdown('<div class="step-box">5. Clinical Support & Transcription</div>', unsafe_allow_html=True)
a4.markdown('<h2 style="border:none; text-align:center; margin:0;">→</h2>', unsafe_allow_html=True)
f6.markdown('<div class="step-box">6. Safe Return & Geofencing Check</div>', unsafe_allow_html=True)
a5.markdown('<h2 style="border:none; text-align:center; margin:0;">→</h2>', unsafe_allow_html=True)
f7.markdown('<div class="step-box">7. Digital Debrief & Family Report</div>', unsafe_allow_html=True)
a6.markdown('<h2 style="border:none; text-align:center; margin:0;">→</h2>', unsafe_allow_html=True)
f8.markdown('<div class="step-box">8. Automated Reconciliation & Payout</div>', unsafe_allow_html=True)

# --- Section 3: Interactive Tools (New!) ---
st.header("III. Interactive Business Simulation")
st.write("Explore the financial logic and market impact of the CareMate model.")

col_calc, col_sim = st.columns(2)

with col_calc:
    st.subheader("Service Fee Estimator")
    st.markdown('<div class="calculator-box">', unsafe_allow_html=True)
    caregiver_type = st.selectbox("Select Caregiver Tier", ["Certified Professional (NT$600/hr)", "Medical Intern (NT$350/hr)", "Retired Nurse (NT$500/hr)"])
    hours = st.slider("Accompaniment Duration (Hours)", 1, 12, 4)
    transport = st.checkbox("Include Barrier-free Transportation (NT$400 base)")
    
    # Logic
    rate = 600 if "Certified" in caregiver_type else 350 if "Intern" in caregiver_type else 500
    base_fee = rate * hours
    transport_fee = 400 if transport else 0
    total = base_fee + transport_fee
    platform_fee = total * 0.3
    
    st.write(f"**Base Service Fee:** NT$ {base_fee}")
    st.write(f"**Platform Matching Fee (30%):** NT$ {int(platform_fee)}")
    st.markdown(f"### **Total Estimated Cost: NT$ {int(total + platform_fee)}**")
    st.markdown('</div>', unsafe_allow_html=True)

with col_sim:
    st.subheader("Market Revenue Projection")
    market_share = st.select_slider("Target Market Share (Taipei Region)", options=[0.5, 1.0, 2.0, 5.0, 10.0], value=1.0)
    avg_order = 2500 # Estimated avg revenue per service
    households = 30000 # Taipei target households
    
    projected_revenue = (households * (market_share/100)) * avg_order * 12
    st.write(f"**Target Households:** {int(households * (market_share/100))}")
    st.write(f"**Estimated Annual Revenue:**")
    st.title(f"NT$ {int(projected_revenue):,}")
    st.info("Based on a conservative frequency of 1 visit/month per household.")

# --- Section 4: Revenue & Financial Sustainability ---
st.header("IV. Financial Sustainability Model")
col_rev, col_exp = st.columns(2)
with col_rev:
    rev_data = pd.DataFrame({"Stream": ["Direct Fees", "Commissions", "B2B Partnership", "Gov Contracts"], "Share": [60, 25, 10, 5]})
    st.plotly_chart(px.pie(rev_data, values='Share', names='Stream', hole=0.5, color_discrete_sequence=px.colors.sequential.Blues_r), use_container_width=True)
with col_exp:
    exp_data = {"R&D": 100000, "Marketing": 100000, "HR": 20000, "Operations": 1565000, "Reserve": 60000}
    st.bar_chart(pd.Series(exp_data))

# --- Section 5: Strategic Business Canvas ---
st.header("V. Strategic Business Canvas")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="info-card"><b>Key Partners</b><br>Hospital Social Work Depts<br>Uber/Taxi Fleets<br>Insurance Providers</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="info-card"><b>Value Proposition</b><br>Peace of mind for families<br>Dignity for seniors<br>Standardized care protocols</div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="info-card"><b>Customer Segments</b><br>Dual-income professionals<br>Overseas Taiwanese<br>Single-living seniors</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.caption("© 2026 CareMate Strategic Planning Team | National Tsing Hua University | Confidential Business Proposal")

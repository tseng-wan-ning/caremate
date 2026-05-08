import streamlit as st
import pandas as pd
import plotly.express as px
import time

# --- 網頁配置 ---
st.set_page_config(page_title="CareMate | Innovating Elderly Care", layout="wide")

# --- 自定義風格 (色彩鮮艷、活潑排版) ---
st.markdown("""
    <style>
    .main { background-color: #f0f8ff; }
    h1 { color: #ff4b4b; font-size: 3rem; text-shadow: 2px 2px #ffeded; }
    h2 { color: #1f77b4; border-bottom: 3px solid #1f77b4; padding-bottom: 5px; }
    .stButton>button { background-color: #ff4b4b; color: white; border-radius: 20px; }
    .feature-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        border-left: 10px solid #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 側邊欄：詳細資訊與動畫佔位 ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=150)
    st.title("CareMate Hub")
    st.markdown("### 🌟 Project Vision")
    st.write("Redefining medical accompaniment through AI & Empathy.")
    st.markdown("---")
    st.write("**Core Team:**")
    st.success("Wan-Ning Tseng\n\nBo-Ying Zhang")
    
    # 這裡可以放進度條，增加動態感
    st.write("Project Readiness")
    st.progress(85)

# --- 標題動畫效果 ---
title_container = st.container()
with title_container:
    st.title("CareMate: The Future of Elderly Medical Care")
    st.subheader("Transforming Loneliness into Professional Companionship")
    st.write("---")

# --- 第一章：深度背景與痛點 (字數擴充) ---
st.header("1. The Critical Crisis: Why CareMate Exists")
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 🛑 The Aging Tsunami")
    st.write("""
    Taiwan is on the brink of a historic demographic shift. By 2025, one in every five citizens will be over 65. 
    This isn't just a statistic; it's a daily crisis for millions of families. Currently, there are over 4 million 
    seniors, and more than 60% suffer from chronic conditions like hypertension, diabetes, or heart disease. 
    These conditions require not just treatment, but **consistent, high-frequency medical follow-ups.**
    
    The reality of modern society is harsh:
    - **Dual-Income Stress:** 70% of households are dual-income. Taking a day off for a 4-hour hospital wait is a luxury many can't afford.
    - **The 'Sandwich' Generation:** Middle-aged professionals are crushed between career demands and the needs of their aging parents.
    - **Geographical Barriers:** As urbanization continues, many children live in different cities or even countries (Overseas Taiwanese), leaving their parents to navigate complex hospital systems alone.
    """)

with col2:
    st.info("### ⚠️ The Failure of Current Systems")
    st.write("""
    Why don't current solutions work?
    1. **Home Caregivers:** They are chronically undersupplied. Getting a slot is like winning the lottery, and the hourly rates are prohibitive for simple hospital visits.
    2. **Personal Agents:** Often found through word-of-mouth, these lack any background checks. The risk of elder abuse or financial fraud is a constant anxiety for families.
    3. **Migrant Workers:** While hardworking, the language barrier in a medical setting is dangerous. Misunderstanding a doctor's dosage instruction can be fatal.
    4. **Volunteers:** They have the heart, but not the schedule. Reliability is the number one requirement for medical appointments, and volunteers cannot guarantee consistency.
    """)

# --- 第二章：詳細服務架構 (加上互動元件) ---
st.header("2. Our Innovative Ecosystem")
st.write("CareMate is not just an app; it is a full-service infrastructure designed for safety and efficiency.")

tab1, tab2, tab3 = st.tabs(["💎 Service Packages", "🤖 Smart Matching", "🛡️ Safety Protocol"])

with tab1:
    col_a, col_b, col_c = st.columns(3)
    col_a.markdown('<div class="feature-card"><h3>Basic Support</h3><p>Registration assistance, clinical accompaniment, and real-time medical recording. We ensure the family knows exactly what the doctor said.</p></div>', unsafe_allow_html=True)
    col_b.markdown('<div class="feature-card"><h3>Premium Transit</h3><p>Integration with barrier-free Uber/Taxi fleets. Door-to-door service with GPS monitoring from start to finish.</p></div>', unsafe_allow_html=True)
    col_c.markdown('<div class="feature-card"><h3>Health Ledger</h3><p>A digital health resume for the senior, tracking blood pressure, medication changes, and future appointments automatically.</p></div>', unsafe_allow_html=True)

with tab2:
    st.write("### How the AI Matching Works")
    st.write("""
    Our proprietary algorithm uses a **Triple-Check Logic**:
    - **Qualification Layer:** Only certified caregivers or vetted medical students can join.
    - **Compatibility Layer:** Matches language (Hakka, Taiwanese) and personality traits to ensure the senior feels comfortable.
    - **Efficiency Layer:** Optimizes the caregiver's route to reduce transit costs for the user.
    """)
    if st.button("Simulate AI Matching Process"):
        with st.spinner('Analyzing caregiver database...'):
            time.sleep(2)
            st.success("Match Found: 98% Compatibility with Caregiver 'Senior Nurse Lin'")

with tab3:
    st.write("### Absolute Safety Framework")
    st.write("""
    We treat safety as our 'Product Zero'.
    - **QR Biometrics:** Both the senior and caregiver must scan a QR code to start the service.
    - **Geofencing:** If the caregiver deviates from the hospital route by more than 500 meters, an automatic alert is sent to our 24/7 center.
    - **Escrow Payments:** Funds are only released after the family reviews the medical report.
    """)

# --- 第三章：商業與財務 (豐富圖表) ---
st.header("3. Financial Viability & Scalability")

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
        "Platform & AI": 100000,
        "Omni-channel Marketing": 100000,
        "Personnel Training": 20000,
        "Admin & Operations": 1565000,
        "Emergency Fund": 60000
    }
    df_exp = pd.DataFrame(list(exp_data.items()), columns=['Item', 'Cost'])
    fig_exp = px.pie(df_exp, values='Cost', names='Item', hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig_exp, use_container_width=True)

# --- 第四章：深度執行方案 (字數最大化) ---
st.header("4. Detailed Implementation & Operations")
with st.expander("Click to expand Full Operational Manual", expanded=False):
    st.write("""
    **Phase 1: Pre-Service Preparation**
    - User Registration: Comprehensive medical history upload, including allergies and mobility status.
    - Caregiver Training: A mandatory 40-hour module covering hospital layouts, emergency response, and psychological support.
    
    **Phase 2: The Accompaniment Journey**
    - Check-in: GPS log at the residence. Photo verification of the senior's status.
    - Hospital Navigation: Assisting with kiosk registration, navigating complex corridors, and managing waiting times.
    - The 'Doctor's Note': Caregivers use our app's voice-to-text tool to record clinical instructions, ensuring 100% accuracy in dosage and follow-up dates.
    
    **Phase 3: Post-Service Integration**
    - Safe Return: Final GPS check-out at home.
    - Family Debrief: A digital report sent via LINE/Email containing: 
        1. Summary of the doctor's findings.
        2. Next appointment date.
        3. Observations on the senior's mood/physical state.
    - Settlement: Automated billing and caregiver payout every Friday.
    """)

# --- 結語 ---
st.markdown("---")
st.balloons() # 重新整理時會有氣球
st.write("### CareMate: Empowering Families, Protecting Seniors.")
st.caption("© 2026 CareMate Team | NTHU Innovation Garage. All Rights Reserved.")

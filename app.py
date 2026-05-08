import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="CareMate | Medical Accompaniment Platform", layout="wide", initial_sidebar_state="expanded")

# --- CUSTOM CSS FOR VIBE ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=100)
st.sidebar.title("CareMate Navigation")
app_mode = st.sidebar.selectbox("Choose a Section", 
    ["Project Overview", "Market Analysis", "Service & Workflow", "Business Model", "Financial Plan"])

st.sidebar.markdown("---")
st.sidebar.write("**Team Members:**")
st.sidebar.info("Wan-Ning Tseng (Sunny)\n\nBo-Ying Zhang")

# --- 1. PROJECT OVERVIEW ---
if app_mode == "Project Overview":
    st.title("🏥 CareMate: Medical Accompaniment Platform")
    st.subheader("Secure Support, Safe Guardian, Warm Companionship")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Vision
        As Taiwan enters a super-aged society, many seniors require regular medical follow-ups. However, children often cannot accompany them due to work, distance, or life pressure. 
        **CareMate** is dedicated to providing a safe, trustworthy platform that bridges the gap between family needs and professional care.
        
        ### Core Values
        - **Trustworthy Entrustment:** Stringent vetting for peace of mind.
        - **Safety Guardian:** Real-time tracking and medical recording.
        - **Warm Companionship:** Respectful care for seniors to maintain their dignity.
        """)
    with col2:
        st.success("**Project Milestone**\n\nNTHU Startup Garage Finalist")
        st.warning("**Focus Area**\n\nESG & Silver Economy")

# --- 2. MARKET ANALYSIS ---
elif app_mode == "Market Analysis":
    st.title("📈 Market Insights & Demand")
    
    # Key Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("Elderly Pop. (2025)", "20%", "Super-aged")
    m2.metric("Chronic Disease Rate", "60%+", "High Demand")
    m3.metric("Caregiver Turnover", "130k+", "Annual")

    with st.expander("🔍 Deep Dive: Pain Points"):
        c1, c2 = st.columns(2)
        c1.write("**For Family Members:**\n- Work-life conflict\n- Geographical distance\n- Information asymmetry (Medical jargon)")
        c2.write("**Existing Service Gaps:**\n- In-home caregivers: High cost, scheduling difficulty\n- Personal agents: Low transparency, high risk\n- Migrant workers: Language barriers")

    st.markdown("### Target Audience")
    st.write("Primary: 30-55 year-old professionals in Tier-1 cities (Taipei, Taichung, Kaohsiung).")

# --- 3. SERVICE & WORKFLOW ---
elif app_mode == "Service & Workflow":
    st.title("⚙️ Service Architecture & AI Matching")
    
    st.markdown("#### The 8-Step Smart Matching Journey")
    steps = ["1. Demand Submission", "2. AI Matching", "3. Reservation", "4. Departure", "5. Hospital Support", "6. Return", "7. Report Gen", "8. Settlement"]
    st.write(" ➔ ".join(steps))
    
    tab1, tab2 = st.tabs(["Service Types", "Staff Categories"])
    
    with tab1:
        st.markdown("""
        - **Standard:** Check-in, medical recording, medication collection.
        - **Premium:** Barrier-free transportation (Uber/Wheelchair Taxi).
        - **Value-added:** Smart health tracking & follow-up reminders via LINE.
        """)
    
    with tab2:
        st.write("Caregivers are vetted and audited annually.")
        col_a, col_b = st.columns(2)
        col_a.info("**Type A: Certified Caregivers**\n\nRate: NT$500-800/hr")
        col_b.info("**Type B: Medical Students**\n\nRate: NT$300-450/hr")

# --- 4. BUSINESS MODEL ---
elif app_mode == "Business Model":
    st.title("💎 Business Strategy")
    
    st.markdown("### Revenue Streams")
    biz_data = {
        "Source": ["Direct Service Fees", "Matching Commission", "B2B Partnership", "Gov. Contracts"],
        "Share": [60, 25, 10, 5]
    }
    df_biz = pd.DataFrame(biz_data)
    fig_biz = px.pie(df_biz, values='Share', names='Source', title='Projected Revenue Distribution')
    st.plotly_chart(fig_biz)

    with st.container():
        st.write("### Pricing Strategy")
        st.table({
            "Service": ["Base Accompaniment", "Platform Fee", "Urgent/Rush Fee"],
            "Price": ["NT$500/hr", "30% of Service Fee", "+50% Premium"]
        })

# --- 5. FINANCIAL PLAN ---
elif app_mode == "Financial Plan":
    st.title("💰 Annual Budget Projection")
    
    budget_data = {
        "Category": ["Platform Dev", "Marketing", "HR/Training", "Admin & Rent", "Miscellaneous"],
        "Amount (TWD)": [100000, 100000, 20000, 1565000, 60000]
    }
    df_budget = pd.DataFrame(budget_data)
    
    col_chart, col_val = st.columns([2, 1])
    with col_chart:
        fig = px.bar(df_budget, x='Category', y='Amount (TWD)', color='Category', text_auto='.2s')
        st.plotly_chart(fig)
    
    with col_val:
        st.metric("Total Annual Capital", "TWD 1,845,000")
        st.write("**Key Expenditures:**\n- Office Rent (TWD 10k/mo)\n- Ad Spend (Google/FB/KOL)")

st.markdown("---")
st.caption("© 2026 CareMate Project Team | National Tsing Hua University")

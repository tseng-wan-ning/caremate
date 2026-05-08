import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time

# --- Page Configuration ---
st.set_page_config(page_title="CareMate | Strategic Proposal", layout="wide")

# --- Advanced CSS for Visual Hierarchy ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    
    /* Extreme Font Size Differences for Hierarchy */
    .super-title {
        color: #003366;
        font-size: 4.5rem;
        font-weight: 900;
        line-height: 1;
        margin-bottom: 0.5rem;
    }
    .section-header {
        color: #1f77b4;
        font-size: 2.2rem;
        font-weight: 700;
        border-bottom: 4px solid #1f77b4;
        padding-bottom: 10px;
        margin-top: 50px;
    }
    .sub-header {
        color: #5a7d9a;
        font-size: 1.5rem;
        font-weight: 600;
        margin-top: 20px;
    }
    .body-text {
        font-size: 1.1rem;
        line-height: 1.8;
        color: #444444;
    }
    
    /* Decorative Elements */
    .feature-card {
        background-color: #f8f9fa;
        padding: 30px;
        border-radius: 5px;
        border-top: 8px solid #003366;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    }
    .highlight-box {
        background-color: #003366;
        color: white;
        padding: 40px;
        border-radius: 10px;
        text-align: center;
    }
    .step-label {
        font-size: 0.9rem;
        color: #1f77b4;
        font-weight: bold;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header Section ---
st.markdown('<p style="color: #1f77b4; font-weight: bold; letter-spacing: 3px;">BUSINESS PROPOSAL 2026</p>', unsafe_allow_html=True)
st.markdown('<h1 class="super-title">CAREMATE</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 1.8rem; color: #5a7d9a;">The Future of Professional Medical Accompaniment</p>', unsafe_allow_html=True)

col_team1, col_team2 = st.columns(2)
with col_team1:
    st.markdown("**Strategic Planning:** Wan-Ning Tseng (Sunny)")
with col_team2:
    st.markdown("**Financial Analysis:** Bo-Ying Zhang")

st.write("---")

# --- Section 1: The Market Dashboard ---
st.markdown('<h2 class="section-header">01 Market Intelligence</h2>', unsafe_allow_html=True)

col_metric1, col_metric2, col_metric3 = st.columns(3)
with col_metric1:
    st.markdown('<div class="stat-box">', unsafe_allow_html=True)
    st.metric("Elderly Dependency Ratio", "20%", "+5% Growth")
    st.write("Targeting the 2025 super-aged society milestone.")
    st.markdown('</div>', unsafe_allow_html=True)

with col_metric2:
    # Gauge Chart for Market Readiness
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 70,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Dual-Income Family Ratio (%)", 'font': {'size': 16}},
        gauge = {'axis': {'range': [None, 100]}, 'bar': {'color': "#003366"}}
    ))
    fig_gauge.update_layout(height=250, margin=dict(t=50, b=0, l=20, r=20))
    st.plotly_chart(fig_gauge, use_container_width=True)

with col_metric3:
    st.metric("Addressable Market", "180,000", "Annual Users")
    st.write("Initial focus on Tier-1 cities in Taiwan.")

# --- Section 2: Deep Dive Analysis ---
st.markdown('<h2 class="section-header">02 Structural Problem Analysis</h2>', unsafe_allow_html=True)

col_text1, col_text2 = st.columns(2)
with col_text1:
    st.markdown('<p class="sub-header">The Crisis of Care</p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">The "Aging Tsunami" is not merely a demographic statistic; it represents a fundamental collapse of the traditional family care model. Currently, over <b>4 million seniors</b> reside in Taiwan, with 60% requiring chronic disease management. The <b>"Sandwich Generation"</b> (aged 30-55) is increasingly unable to balance corporate productivity with the rigorous demands of hospital accompaniment, leading to significant economic loss and emotional burnout.</p>', unsafe_allow_html=True)

with col_text2:
    st.markdown('<p class="sub-header">Market Gaps</p>', unsafe_allow_html=True)
    # Professional Bullet Points with CSS
    st.markdown("""
    <div style="background-color: #f1f4f9; padding: 20px; border-radius: 5px;">
    - <b>Institutional Rigidity:</b> Current home care services lack the flexibility for 4-hour medical windows.<br>
    - <b>Transparency Deficit:</b> Unregulated agents offer no background verification or quality audits.<br>
    - <b>Linguistic Barriers:</b> Foreign caregivers struggle with complex clinical terminology in Taiwanese hospitals.
    </div>
    """, unsafe_allow_html=True)

# --- Section 3: The CareMate Solution Flow ---
st.markdown('<h2 class="section-header">03 Operational Architecture</h2>', unsafe_allow_html=True)

# Visualizing the Flow with Cards
step_cols = st.columns(4)
steps = [
    ["STAGE 01", "Acquisition", "User health profiling and smart data onboarding."],
    ["STAGE 02", "Matching", "AI-driven selection based on language and location."],
    ["STAGE 03", "Deployment", "Secure biometric check-in and GPS-tracked transit."],
    ["STAGE 04", "Clinical", "Real-time medical transcription and family debrief."]
]

for i, col in enumerate(step_cols):
    with col:
        st.markdown(f"""
        <div class="feature-card">
        <p class="step-label">{steps[i][0]}</p>
        <p style="font-size: 1.3rem; font-weight: bold; color: #1f77b4;">{steps[i][1]}</p>
        <p style="font-size: 0.9rem;">{steps[i][2]}</p>
        </div>
        """, unsafe_allow_html=True)

# --- Section 4: Financial & Scalability ---
st.header("04 Financial & Scaling Model")

tab_rev, tab_exp = st.tabs(["REVENUE STREAMS", "CAPITAL ALLOCATION"])

with tab_rev:
    rev_data = pd.DataFrame({
        "Source": ["Service Fees", "Commission", "B2B", "Grants"],
        "Value": [60, 25, 10, 5]
    })
    fig_rev = px.sunburst(rev_data, path=['Source'], values='Value', color='Value', 
                          color_continuous_scale='Blues', title="Revenue Ecosystem")
    st.plotly_chart(fig_rev, use_container_width=True)

with tab_exp:
    exp_data = {"R&D": 100000, "Marketing": 100000, "HR": 20000, "Ops": 1565000, "Misc": 60000}
    fig_exp = px.bar(x=list(exp_data.keys()), y=list(exp_data.values()), 
                     labels={'x':'Department', 'y':'Budget (TWD)'},
                     color=list(exp_data.values()), color_continuous_scale='Blues')
    st.plotly_chart(fig_exp, use_container_width=True)

# --- Footer ---
st.markdown('<div class="highlight-box"><h3>CARE MATE SOLUTIONS</h3><p>Institutionalizing Empathy through Technology.</p></div>', unsafe_allow_html=True)
st.caption("© 2026 CareMate Team | National Tsing Hua University Strategic Planning Portfolio")

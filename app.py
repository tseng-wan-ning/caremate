import streamlit as st

# 網頁設定
st.set_page_config(page_title="陪診家 CareMate 創業企畫書", layout="wide")

# 側邊欄導覽
st.sidebar.title("導覽選單")
menu = st.sidebar.radio("跳轉至章節：", [
    "一、創業理念", 
    "二、市場需求分析", 
    "三、服務內容與流程", 
    "四、商業模式與定價", 
    "五、財務預算"
])

# 頁首
st.title("🏥 陪診家 CareMate")
st.subheader("安心託付、安全守護、溫暖陪伴")
st.info("台灣首創安全信賴的陪病媒合平台")

if menu == "一、創業理念":
    st.header("✨ 創業理念與核心價值")
    col1, col2 = st.columns(2)
    with col1:
        st.write("### 創業理念")
        st.write("台灣邁入高齡社會，子女因工作或距離無法親自陪診。我們提供安全、可信賴的平台，讓子女安心，長者有尊嚴。")
    with col2:
        st.write("### 核心價值")
        st.success("✅ 安心託付\n\n✅ 安全守護\n\n✅ 溫暖陪伴")

elif menu == "二、市場需求分析":
    st.header("📊 問題與市場需求分析")
    
    tab1, tab2, tab3 = st.tabs(["痛點分析", "目標族群", "市場規模"])
    
    with tab1:
        st.write("### 子女與長者的具體痛點")
        st.error("❌ 時間衝突：子女工作與門診重疊")
        st.error("❌ 地理距離：遠距照護困難")
        st.error("❌ 溝通隔閡：醫療資訊遺漏")
        
    with tab2:
        st.write("### 目標族群")
        st.write("- **核心對象**：30-55 歲雙薪家庭，月入 5 萬以上之都會區族群。")
        st.write("- **潛在市場**：海外子女、單身長者、醫護合作機構。")

    with tab3:
        st.write("### 市場預估 (台北市為例)")
        st.metric(label="預估目標家庭數", value="30,000 戶")
        st.metric(label="初期市佔目標 (5%)", value="1,500 戶")

elif menu == "三、服務內容與流程":
    st.header("🛠️ 服務內容與媒合流程")
    
    st.write("### 核心服務項目")
    items = {
        "基礎服務": "門診陪診、檢查陪伴、記錄醫囑回報家屬",
        "加值服務": "一般/無障礙接送、長途就醫安排",
        "增值服務": "智能健康管理、回診提醒、用藥提醒"
    }
    st.table(items)
    
    st.write("### 智能媒合 8 大階段")
    st.image("https://via.placeholder.com/800x400.png?text=Workflow+Visualization") # 此處可替換成你的流程圖網址
    st.write("1. 需求提交 ➔ 2. 智能篩選 ➔ 3. 預約確認 ➔ 4. 抵達接送 ➔ 5. 醫院陪診 ➔ 6. 服務結束 ➔ 7. 報告生成 ➔ 8. 款項結算")

elif menu == "四、商業模式與定價":
    st.header("💰 商業模式設計")
    
    st.write("### 統一收費標準")
    pricing_data = [
        {"項目": "陪診服務", "收費方式": "計時", "費用": "NT$500 / 小時"},
        {"項目": "平台媒合費", "收費方式": "抽成", "費用": "服務費 30%"},
        {"項目": "交通費", "收費方式": "里程計費", "費用": "實報實銷"},
        {"項目": "加班/急件", "收費方式": "附加費", "費用": "基礎費用 +50%"}
    ]
    st.table(pricing_data)

elif menu == "五、財務預算":
    st.header("💵 初期資金投入預估")
    total_budget = 1845000
    st.write(f"### 第一年預計投入總金額：TWD {total_budget:,}")
    
    expenses = {
        "平台架設": 100000,
        "宣傳行銷": 100000,
        "人事培訓": 20000,
        "行政租金": 1565000,
        "雜費": 60000
    }
    st.bar_chart(expenses)
    st.write("*(單位：新台幣)*")

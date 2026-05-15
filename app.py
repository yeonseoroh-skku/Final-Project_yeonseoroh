import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# 1. Page Configuration (SKKU & Fashion Theme)
st.set_page_config(
    page_title="Joseon Punk Hub | Yeonseo Roh",
    page_icon="💎",
    layout="wide"
)

# 2. Sidebar Navigation
st.sidebar.title("💎 Fashion Data Hub")
st.sidebar.markdown("Produced by **Yeonseo Roh** (SKKU)")
menu = st.sidebar.radio("Select Analysis", 
    ["Home", "Aesthetic Radar", "Sentiment Tracker", "Sustainability Scorecard", "Trend Diffusion Map"])

# --- DATA GENERATION (실제 데이터를 대신할 샘플 데이터) ---
def get_fashion_data():
    traits = ['Volume', 'Complexity', 'Color Saturation', 'Durability', 'Formalness']
    joseon = [9, 10, 4, 3, 10]
    modern = [7, 6, 9, 8, 5]
    return pd.DataFrame({'Trait': traits, 'Joseon Style': joseon, 'Modern Street': modern})

# --- MENU 1: HOME ---
if menu == "Home":
    st.title("💎 Fashion Evolution & Trend Intelligence Hub")
    st.markdown("> **A Data-Driven Exploration: Joseon Aesthetics vs. Modern Streetwear**")
    
    st.image("https://images.unsplash.com/photo-1523381210434-271e8be1f52b?q=80&w=1200", caption="Digitalizing the Fashion Zeitgeist")
    
    st.write("---")
    st.header("Project Overview")
    st.info("이 대시보드는 조선시대의 복식 데이터와 현대 스트릿 웨어 데이터를 비교하여, 과거의 예술적 DNA가 어떻게 현대에 재해석되는지 정량적으로 분석합니다.")

# --- MENU 2: AESTHETIC RADAR ---
elif menu == "Aesthetic Radar":
    st.header("✨ Aesthetic Radar: Silhouette Comparison")
    df = get_fashion_data()

    # Radar Chart (Plotly Graph Objects)
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=df['Joseon Style'], theta=df['Trait'], fill='toself', name='Joseon Style'))
    fig.add_trace(go.Scatterpolar(r=df['Modern Street'], theta=df['Trait'], fill='toself', name='Modern Streetwear'))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
        showlegend=True,
        template="plotly_dark"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.write("조선시대 복식은 **Complexity(복잡성)**와 **Formalness(격식)**에서 높은 점수를 보이며, 현대 스트릿은 **Saturation(채도)**이 강조됩니다.")

# --- MENU 3: SENTIMENT TRACKER ---
elif menu == "Sentiment Tracker":
    st.header("📈 Brand Sentiment & Vibe Tracker")
    
    # 가상의 감성 지수 데이터
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Brand Heat (Authenticity)", value="88%", delta="5%")
    with col2:
        st.metric(label="Consumer Prestige Score", value="92", delta="-2")

    # Time-series sentiment chart
    time_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Positive': [70, 75, 80, 85, 88],
        'Negative': [10, 8, 12, 5, 4]
    })
    fig = px.line(time_data, x='Month', y=['Positive', 'Negative'], title="Monthly Sentiment Trend", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

# --- MENU 4: SUSTAINABILITY ---
elif menu == "Sustainability Scorecard":
    st.header("🌿 Sustainability Scorecard")
    fabrics = ['Organic Cotton', 'Recycled Poly', 'Traditional Silk', 'Synthetic Nylon']
    footprint = [20, 35, 15, 80]
    
    fig = px.bar(x=fabrics, y=footprint, color=fabrics, 
                 labels={'x':'Fabric Type', 'y':'CO2 Footprint Score'},
                 title="Environmental Impact by Textile", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

# --- MENU 5: TREND MAP ---
elif menu == "Trend Diffusion Map":
    st.header("🗺️ Global Trend Diffusion Map")
    # 가상의 지도 데이터
    map_data = pd.DataFrame({
        'lat': [37.5665, 48.8566, 40.7128, 35.6762],
        'lon': [126.9780, 2.3522, -74.0060, 139.6503],
        'Trend_Volume': [100, 85, 90, 70]
    })
    st.map(map_data)
    st.caption("Seoul (Origin) -> Paris -> NY -> Tokyo diffusion intensity.")

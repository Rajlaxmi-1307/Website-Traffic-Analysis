
# ============================================================
# WEBSITE TRAFFIC ANALYSIS DASHBOARD
# Using Python, Pandas, Plotly and Streamlit
# ============================================================


# STEP 1: IMPORT REQUIRED LIBRARIES

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from pathlib import Path


# STEP 2: PAGE CONFIGURATION

st.set_page_config(
    page_title="Website Traffic Analysis",
    page_icon="📊",
    layout="wide"
)


# STEP 3: CUSTOM CSS

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

h1 {
    color: #172554;
    font-weight: bold;
}

h2, h3 {
    color: #1e3a8a;
}

[data-testid="stMetric"] {
    background-color: white;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
}

[data-testid="stSidebar"] {
    background-color: #eef2ff;
}

</style>
""", unsafe_allow_html=True)


# STEP 4: LOAD DATASET

BASE_DIR = Path(__file__).resolve().parent.parent

CLEANED_FILE = BASE_DIR / "dataset" / "cleaned_website_traffic.csv"
RAW_FILE = BASE_DIR / "dataset" / "website_wata.csv"

if CLEANED_FILE.exists():
    web = pd.read_csv(CLEANED_FILE)

elif RAW_FILE.exists():
    web = pd.read_csv(RAW_FILE)

else:
    st.error("Dataset file not found! Check the dataset folder.")
    st.stop()


# STEP 5: CHECK REQUIRED COLUMNS

required_columns = [
    "Page Views",
    "Session Duration",
    "Bounce Rate",
    "Traffic Source",
    "Time on Page",
    "Previous Visits",
    "Conversion Rate"
]

missing_columns = [
    col for col in required_columns
    if col not in web.columns
]

if missing_columns:
    st.error(f"Missing columns: {missing_columns}")
    st.stop()


# STEP 6: DATA PREPROCESSING

web = web.drop_duplicates().copy()

numeric_columns = [
    "Page Views",
    "Session Duration",
    "Bounce Rate",
    "Time on Page",
    "Previous Visits",
    "Conversion Rate"
]

for column in numeric_columns:
    web[column] = pd.to_numeric(
        web[column],
        errors="coerce"
    )

web = web.dropna(subset=required_columns).copy()

web["Traffic Source"] = web["Traffic Source"].astype(str)

if web.empty:
    st.error("No valid records available in the dataset.")
    st.stop()


# STEP 7: SIDEBAR FILTERS

st.sidebar.title("🎯 Dashboard Filters")

st.sidebar.markdown("---")

traffic_sources = sorted(
    web["Traffic Source"].unique()
)

selected_source = st.sidebar.selectbox(
    "Select Traffic Source",
    ["All"] + traffic_sources
)

if selected_source == "All":
    filtered_web = web.copy()

else:
    filtered_web = web[
        web["Traffic Source"] == selected_source
    ].copy()


st.sidebar.markdown("---")

st.sidebar.info(
    "Use this filter to analyze website performance "
    "for different traffic sources."
)

st.sidebar.markdown("### 📌 Project Information")

st.sidebar.write("Project: Website Traffic Analysis")
st.sidebar.write("Language: Python")
st.sidebar.write("Libraries: Pandas, NumPy, Plotly")
st.sidebar.write("Dashboard: Streamlit")


# STEP 8: CALCULATE KPIs

total_sessions = len(filtered_web)

total_page_views = filtered_web["Page Views"].sum()

avg_session = filtered_web["Session Duration"].mean()

avg_bounce = filtered_web["Bounce Rate"].mean()

avg_conversion = filtered_web["Conversion Rate"].mean()


# STEP 9: DASHBOARD TITLE

st.title("📊 Website Traffic Analysis Dashboard")

st.markdown(
    "Analyze website visitors, traffic sources, "
    "engagement and conversion performance."
)

st.markdown("---")


# STEP 10: WEBSITE PERFORMANCE OVERVIEW

st.header("📌 Website Performance Overview")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Sessions",
    f"{total_sessions:,}"
)

col2.metric(
    "Total Page Views",
    f"{total_page_views:,.0f}"
)

col3.metric(
    "Avg Session Duration",
    f"{avg_session:.2f}"
)

col4.metric(
    "Avg Conversion Rate",
    f"{avg_conversion:.1%}"
)

col5.metric(
    "Avg Bounce Rate",
    f"{avg_bounce:.1%}"
)


st.markdown("---")


# STEP 11: TRAFFIC SOURCE DISTRIBUTION

st.header("🌐 Traffic Source Distribution")

traffic_data = (
    filtered_web["Traffic Source"]
    .value_counts()
    .reset_index()
)

traffic_data.columns = [
    "Traffic Source",
    "Sessions"
]

fig1 = px.pie(
    traffic_data,
    names="Traffic Source",
    values="Sessions",
    hole=0.45,
    title="Website Traffic Distribution",
    color_discrete_sequence=px.colors.qualitative.Set2
)

fig1.update_traces(
    textposition="inside",
    textinfo="percent+label"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)


st.markdown("---")


# STEP 12: PAGE VIEWS BY TRAFFIC SOURCE

st.header("📄 Page Views Analysis")

page_views_data = (
    filtered_web.groupby("Traffic Source")["Page Views"]
    .sum()
    .reset_index()
    .sort_values("Page Views", ascending=False)
)

fig2 = px.bar(
    page_views_data,
    x="Traffic Source",
    y="Page Views",
    color="Traffic Source",
    title="Total Page Views by Traffic Source",
    text_auto=".0f"
)

fig2.update_layout(
    showlegend=False,
    xaxis_title="Traffic Source",
    yaxis_title="Total Page Views"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)


st.markdown("---")


# STEP 13: SESSION DURATION ANALYSIS

st.header("⏱️ Session Duration Analysis")

session_data = (
    filtered_web.groupby("Traffic Source")["Session Duration"]
    .mean()
    .reset_index()
    .sort_values("Session Duration", ascending=False)
)

fig3 = px.bar(
    session_data,
    x="Traffic Source",
    y="Session Duration",
    color="Traffic Source",
    title="Average Session Duration by Traffic Source",
    text_auto=".2f"
)

fig3.update_layout(
    showlegend=False,
    xaxis_title="Traffic Source",
    yaxis_title="Average Session Duration"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)


st.markdown("---")


# STEP 14: BOUNCE RATE ANALYSIS

st.header("📉 Bounce Rate Analysis")

bounce_data = (
    filtered_web.groupby("Traffic Source")["Bounce Rate"]
    .mean()
    .reset_index()
    .sort_values("Bounce Rate", ascending=False)
)

fig4 = px.bar(
    bounce_data,
    x="Traffic Source",
    y="Bounce Rate",
    color="Traffic Source",
    title="Average Bounce Rate by Traffic Source",
    text_auto=".2%"
)

fig4.update_layout(
    showlegend=False,
    xaxis_title="Traffic Source",
    yaxis_title="Average Bounce Rate",
    yaxis_tickformat=".0%"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)


st.markdown("---")


# STEP 15: CONVERSION RATE ANALYSIS

st.header("🎯 Conversion Rate Analysis")

conversion_data = (
    filtered_web.groupby("Traffic Source")["Conversion Rate"]
    .mean()
    .reset_index()
    .sort_values("Conversion Rate", ascending=False)
)

fig5 = px.bar(
    conversion_data,
    x="Traffic Source",
    y="Conversion Rate",
    color="Traffic Source",
    title="Average Conversion Rate by Traffic Source",
    text_auto=".1%"
)

fig5.update_layout(
    showlegend=False,
    xaxis_title="Traffic Source",
    yaxis_title="Average Conversion Rate",
    yaxis_tickformat=".0%"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)


st.markdown("---")


# STEP 16: TIME ON PAGE ANALYSIS

st.header("⌛ Time on Page Analysis")

time_data = (
    filtered_web.groupby("Traffic Source")["Time on Page"]
    .mean()
    .reset_index()
    .sort_values("Time on Page", ascending=False)
)

fig6 = px.bar(
    time_data,
    x="Traffic Source",
    y="Time on Page",
    color="Traffic Source",
    title="Average Time on Page by Traffic Source",
    text_auto=".2f"
)

fig6.update_layout(
    showlegend=False,
    xaxis_title="Traffic Source",
    yaxis_title="Average Time on Page"
)

st.plotly_chart(
    fig6,
    use_container_width=True
)


st.markdown("---")


# STEP 17: CORRELATION HEATMAP

st.header("🔥 Correlation Analysis")

correlation = filtered_web[
    numeric_columns
].corr()

fig7 = px.imshow(
    correlation,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    title="Website Traffic Correlation Heatmap",
    aspect="auto",
    zmin=-1,
    zmax=1
)

st.plotly_chart(
    fig7,
    use_container_width=True
)


st.markdown("---")


# STEP 18: SESSION ENGAGEMENT ANALYSIS

st.header("👥 Visitor Engagement Analysis")

fig8 = px.scatter(
    filtered_web,
    x="Session Duration",
    y="Page Views",
    color="Traffic Source",
    size="Previous Visits",
    hover_data=[
        "Bounce Rate",
        "Time on Page",
        "Conversion Rate"
    ],
    title="Session Duration vs Page Views"
)

st.plotly_chart(
    fig8,
    use_container_width=True
)


st.markdown("---")


# STEP 19: BEST PERFORMING TRAFFIC SOURCE

st.header("🏆 Best Performing Traffic Source")

best_source = conversion_data.iloc[0]["Traffic Source"]

best_conversion = conversion_data.iloc[0]["Conversion Rate"]

col1, col2 = st.columns(2)

col1.metric(
    "Best Traffic Source",
    best_source
)

col2.metric(
    "Average Conversion Rate",
    f"{best_conversion:.2%}"
)


# STEP 20: BUSINESS INSIGHTS

st.header("💡 Business Insights")

best_engagement = session_data.iloc[0]["Traffic Source"]

lowest_bounce = bounce_data.iloc[-1]["Traffic Source"]

highest_page_views = page_views_data.iloc[0]["Traffic Source"]

st.success(
    f"🏆 {best_source} has the highest average conversion rate."
)

st.info(
    f"⏱️ {best_engagement} has the longest average session duration."
)

st.success(
    f"📄 {highest_page_views} generates the highest total page views."
)

st.info(
    f"📉 {lowest_bounce} has the lowest average bounce rate."
)


# STEP 21: DATASET PREVIEW

st.markdown("---")

st.header("📋 Website Traffic Dataset")

st.write(
    f"Total Records: {len(filtered_web)}"
)

st.dataframe(
    filtered_web,
    use_container_width=True
)


# STEP 22: DOWNLOAD CSV REPORT

st.markdown("---")

st.header("📥 Download Traffic Report")

csv_data = filtered_web.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇️ Download CSV Report",
    data=csv_data,
    file_name="website_traffic_report.csv",
    mime="text/csv"
)


# STEP 23: FOOTER

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:gray;">

    <h4>Website Traffic Analysis Using Python</h4>

    <p>Developed using Pandas, NumPy, Plotly and Streamlit</p>

    <p>Data Science Project | 2026</p>

    </div>
    """,
    unsafe_allow_html=True
)

import streamlit as st
import sqlite3
import pandas as pd

DB_FILE = "../data/alerts.db"

# Connect to SQLite and fetch all alerts
def load_data():
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql_query("SELECT * FROM alerts", conn)
    conn.close()
    return df

# Streamlit dashboard layout
def main():
    st.set_page_config(page_title="AUTODEFEND Dashboard", layout="wide")
    st.title("🛡️ AUTODEFEND - Incident Response Dashboard")

    # Load the alerts
    df = load_data()

    # Sidebar filters
    st.sidebar.header("Filters")
    type_filter = st.sidebar.multiselect("Alert Type", df["type"].unique())
    action_filter = st.sidebar.multiselect("Action", df["action"].unique())
    min_score = st.sidebar.slider("Minimum Risk Score", 0, 100, 0)

    # Apply filters
    filtered_df = df.copy()
    if type_filter:
        filtered_df = filtered_df[filtered_df["type"].isin(type_filter)]
    if action_filter:
        filtered_df = filtered_df[filtered_df["action"].isin(action_filter)]
    filtered_df = filtered_df[filtered_df["score"] >= min_score]

    # Display data
    st.subheader(f"Showing {len(filtered_df)} Alerts")
    st.dataframe(filtered_df, use_container_width=True)

    # Summary metrics
    st.markdown("---")
    st.subheader("📊 Quick Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Alerts", len(df))
    col2.metric("High Risk (≥75)", len(df[df["score"] >= 75]))
    col3.metric("Actions: BLOCK_IP", len(df[df["action"] == "BLOCK_IP"]))

    # Chart visualization
    st.markdown("### 🚨 Alerts by Type")
    chart_data = df.groupby("type")["score"].mean().sort_values(ascending=False)
    st.bar_chart(chart_data)

if __name__ == "__main__":
    main()

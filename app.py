import streamlit as st
import pandas as pd
import plotly.express as px
from google_sheets import append_mood, get_today_moods

# Set the page title
st.set_page_config(page_title="Mood of the Queue", layout="centered")

st.title("🧠 Mood of the Queue")
st.caption("Log and track the mood of your support queue throughout the day.")

# Create two tabs
tab1, tab2 = st.tabs(["📝 Log Mood", "📊 View Moods"])

# Log Mood Tab
with tab1:
    st.subheader("Log your mood")
    mood = st.selectbox("Select your mood", ["😊 Happy", "😕 Confused", "😠 Frustrated", "🎉 Excited"])
    note = st.text_input("Add a short note (optional)")

    if st.button("Submit Mood"):
        mood_emoji = mood.split()[0]  # extract just the emoji
        append_mood(mood_emoji, note)
        st.success("Mood logged successfully!")

# View Moods Tab
from datetime import datetime
import time

with tab2:
    st.subheader("Mood Summary")

    # Select a date
    selected_date = st.date_input("Select a date", datetime.today().date())

    df = get_today_moods()

    if df.empty:
        st.info("No moods logged yet.")
    else:
        # Filter by selected date
        df = df[df['timestamp'].dt.date == selected_date]

        if df.empty:
            st.warning("No moods logged for this date.")
        else:
            mood_counts = df['mood'].value_counts().reset_index()
            mood_counts.columns = ['Mood', 'Count']
            fig = px.bar(mood_counts, x='Mood', y='Count', color='Mood', title=f"Moods on {selected_date}")
            st.plotly_chart(fig, use_container_width=True)

    # Auto-refresh every 30 seconds
    st.caption("⏱️ Auto-refreshing every 30 seconds...")
    time.sleep(30)
    st.rerun()

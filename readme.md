# Mood of the Queue 🧠

A lightweight internal tool built using Python and Streamlit that allows support team members to log the “vibe” of the queue in real time — whether it’s joyful, frustrating, or just plain confusing.

This app records mood entries in a Google Sheet and visualizes them with a live-updating chart. It's designed to be fast, minimal, and easy to deploy for internal use.

---

## 🚀 Features

- Select mood (😊 😠 😕 🎉) with an optional note
- Stores logs with timestamp in a Google Sheet
- View real-time bar chart of today’s moods
- Filter entries by date
- Chart auto-refreshes every 30 seconds

---

## 📸 Demo Walkthrough

[Loom Video Walkthrough](https://your-loom-link-here.com)

---

## 📊 Live Sheet (View-Only Access)

[Google Sheet Link (view only)](https://your-google-sheet-view-link.com)

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** for UI
- **gspread + oauth2client** for Google Sheets integration
- **Plotly** for data visualization
- **Pandas** for data handling

---

## 🔐 How to Set Up Google Sheets Integration

This app uses a Google Sheets backend via a service account. You'll need to create your own `credentials.json` to run it.

### 📥 Step-by-Step Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select an existing one)
3. Enable these APIs:
   - Google Sheets API
   - Google Drive API
4. Navigate to: APIs & Services → Credentials → Create Credentials → Service Account

5. Once created, go to your service account:

- Click **"Keys" → "Add Key" → "JSON"**
- This downloads `credentials.json` — place this in your project root (not included in the repo)

6. Share your Google Sheet with the **client_email** from the credentials (ending in `.iam.gserviceaccount.com`) and give it **Editor** access.

# Place your credentials.json in the root directory

# Run the app

streamlit run app.py

import streamlit as st
from pymongo import MongoClient

# ---------------- MONGODB CONNECTION ----------------
client = MongoClient("mongodb://localhost:27017/")
db = client["trading_app"]
collection = db["feedback"]

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Feedback",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Feedback")

# ---------------- USER CHECK ----------------
if "user" not in st.session_state or st.session_state["user"] is None:
    st.warning("Please login first to give feedback.")
    st.stop()

username = st.session_state["user"]

# ---------------- FEEDBACK FORM ----------------
st.subheader("We value your feedback 💬")

feedback_text = st.text_area("Write your feedback here:")

if st.button("Submit Feedback"):

    if feedback_text.strip() == "":
        st.error("Please write something before submitting.")
    else:
        # store in MongoDB
        data = {
            "username": username,
            "feedback": feedback_text
        }

        collection.insert_one(data)

        st.success("✅ Feedback submitted successfully!")
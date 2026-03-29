import streamlit as st
import bcrypt
from db import users_collection

# Hash password
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Verify password
def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Register User
def register():
    st.title("Register")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if users_collection.find_one({"email": email}):
            st.error("User already exists!")
        else:
            hashed_pw = hash_password(password)
            users_collection.insert_one({
                "username": username,
                "email": email,
                "password": hashed_pw
            })

            st.success("Registered successfully! Redirecting to login...")

            # 👇 IMPORTANT LINE (redirect logic)
            st.session_state["redirect_to_login"] = True
            st.rerun()

# Login User
def login():
    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = users_collection.find_one({"email": email})

        if user and verify_password(password, user["password"]):
            st.session_state["user"] = user["username"]
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid credentials")
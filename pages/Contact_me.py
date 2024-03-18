import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Enter Your Email")
    raw_message = st.text_area("Your message here...")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
    {raw_message}"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Email Sent, I'll be in touch!")

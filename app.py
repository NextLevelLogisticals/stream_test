import streamlit as st

# Define your secure code or password here
SECURE_CODE = "tpads"

# Create a password input field so that the code is not displayed
user_code = st.text_input("Enter the access code to view the app:", type="password")

# Verify the code entered by the user
if user_code != SECURE_CODE:
    st.warning("Access Denied: Incorrect code. Please try again.")
    st.stop()  # Stop further execution of the app if the code is wrong

# Content accessible only when the correct code is entered
st.title("Hello World!")
st.write("Welcome to my Streamlit app deployed on Azure!")

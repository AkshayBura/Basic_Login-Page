import streamlit as st
import requests

st.title("Login Page")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
if st.button("Login"):
    data = {"username": username, "password": password}
    response = requests.post("http://127.0.0.1:5000/login", data=data)

    if response.status_code == 200:
        st.success("Login successful!")
        st.session_state.access_token = response.json()["access_token"]
        st.write("Redirecting to 'Blogs' page...")
        st.progress(0) 
        st.text("Redirecting in 3 seconds...")
        st.text("2")
        st.text("1")

        st.experimental_rerun()

if hasattr(st.session_state, 'access_token'):
    st.experimental_set_query_params(access_token=st.session_state.access_token)

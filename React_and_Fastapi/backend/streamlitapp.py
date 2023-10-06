import streamlit as st
import requests

st.title("Login page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username and password:
        data = {"username": username, "password": password}
        response = requests.post("http://127.0.0.1:5000/login", data=data)

        if response.status_code == 200:
            st.success("Login successful!")
            access_token =  response.json()['access_token']
            # st.write("Access Token:", response.json()["access_token"])
            # st.write("Token Type:", response.json()["token_type"])

            resp = requests.get('http://127.0.0.1:5000/blog', headers={"Authorization": f"Bearer {access_token}"})
            res = resp.json()
            st.write(res)

        else:
            st.error("Login failed. Invalid credentials.")
    else:
            st.error("Please enter username and password.")
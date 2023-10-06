import streamlit as st
import requests

access_token = st.experimental_get_query_params().get("access_token")

if access_token:
    st.title("Blogs")
    st.write("Welcome to the Blogs page!")

    response = requests.get("http://127.0.0.1:5000/blogs", headers={"Authorization": f"Bearer {access_token}"})
    if response.status_code == 200:
        blogs = response.json()
        for blog in blogs:
            st.write(f"- {blog['title']}")
    else:
        st.error("Failed to retrieve blogs.")

else:
    st.info("Please log in to access the Blogs page.")

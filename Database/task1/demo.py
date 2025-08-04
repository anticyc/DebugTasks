import streamlit as st
from models import *
import re

st.set_page_config(page_title="User Management", page_icon=":robot:", layout="wide")
st.markdown("# User Management :robot:")

st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            display: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

database = create_db()

st.write("## Create User")
name = st.text_input("Name")
email = st.text_input("Email")
info = st.text_area("Info")
if st.button("Create User"):
    if name == "" or email == "" or re.match(r"[^@]+@[^@]+\.[^@]+", email) is None:
        st.error("Name and Email are required. Email must be valid.")
    else:
        user = User(name=name, email=email, info=info)
        with database.begin() as session:
            existing_user = session.query(User).filter_by(email=email).first()
            if existing_user:
                st.error("User with this email already exists.")
            else:
                session.add(user)
                st.success("User created successfully!")

if st.button("Show Users"):
    with database.begin() as session:
        users = session.query(User).all()
        if users:
            st.write("### Users List")
            for user in users:
                st.markdown(f"**ID:** {user.id}, **Name:** {user.name}, **Email:** {user.email}, **Info:** {user.info}, **Created At:** {user.created_at}")
        else:
            st.write("No users found.")
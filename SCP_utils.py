
import streamlit as st


# Add a selectbox to the sidebar:
def add_how_contact():
    add_selectbox = st.sidebar.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone')
    )


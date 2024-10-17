import streamlit as st
from page_one import page_one
from page_two import page_two

# Function to check password
def check_password():
    password = st.session_state.get('password', '')
    return password == st.secrets["password"]

# Initialize session state
if 'password' not in st.session_state:
    st.session_state.password = ''
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Sidebar for password input and navigation
if not st.session_state.authenticated:
    with st.sidebar:
        st.session_state.password = st.text_input("Enter password:", type='password')
        if st.button("Submit"):
            if check_password():
                st.session_state.authenticated = True
                st.success("Password correct! Access granted.")
            else:
                st.error("Incorrect password")
else:
    with st.sidebar:
        st.header("Navigation")
        # Ensure 'page' is always defined
        page = st.radio("Select a page:", ["Home", "Page One", "Page Two"])

# Ensure the page variable is accessible outside the sidebar block
if st.session_state.authenticated:
    if 'page' in locals() or 'page' in globals():  # Check if 'page' is defined
        if page == "Home":
            st.title("Welcome to My Streamlit App")
            st.write("This is the homepage content.")
        elif page == "Page One":
            page_one()  # Call the function for Page One
        elif page == "Page Two":
            page_two()  # Call the function for Page Two
else:
    st.write("Please enter the password to access the app.")

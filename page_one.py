import streamlit as st

def page_one():
    st.title("Page One")
    st.write("This is the content of Page One.")

    # Add more content as needed
    st.subheader("Sample DataFrame")
    data = {'Column 1': [1, 2, 3, 4], 'Column 2': [10, 20, 30, 40]}
    st.write(data)

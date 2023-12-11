import streamlit as st

st.set_page_config(
  page_title="Clock",
  page_icon="🕔"
)
st.title("Settings:")

hide_st_style = """
    <style>
    header {visibility: hidden;}
    </stile>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
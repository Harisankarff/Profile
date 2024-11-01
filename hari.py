import streamlit as st

st.set_page_config(page_icon=":heart:", page_title="Hari Sankar", layout= "wide")
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

def display_centered_title(text, level=1, font_size=38):
    style = f"text-align: center; font-size: {font_size}px; border-radius: 5px;"
    st.markdown(f"<h{level} style='{style}'>{text}</h{level}>", unsafe_allow_html=True)

display_centered_title("Hari Sankar", level=2, font_size=48)


st.write("")
st.write("")
st.write("Hello Everyone, I'am Hari Sankar and I am currently studying 1st year in Polytechnic at VSVN Polytechnic College.")
st.write("---")
st.write("My Freefire ID is 8237487238.")
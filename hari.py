import streamlit as st
from PIL import Image

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
st.write("Hello Everyone, I'am Hari Sankar and I am currently pursuing 1st year EEE at VSVN Polytechnic College, Virudhunagar.")
st.write("---")
with st.container():
    ffleft,ffright=st.columns(([1,2]))
    with ffleft:
        image= Image.open("WhatsApp Image 2024-11-01 at 14.20.29_ac8b3075.jpg")
        st.image(image)

    with ffright:
        st.write("Dedicated and motivated Freefire player :video_game:")
        st.write("Available for BR, CS and Custom matches.")
        st.subheader("Contact the below form") 
        st.write("BEWARE :skull_and_crossbones: : SPAM OR INAPPROPRIATE MESSAGES WILL BE NOTED UNDER SECTION Section 66A of the Information Technology Act of 2000 by CYBERCRIME.")
        contact_form = """
<form action="https://formsubmit.co/hariff7806@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" id="name" name="name" placeholder="Your name" required>
            <input type="number" id="phno" name="phno" placeholder="Your number" required>
            <textarea         name="message" placeholder="Your message here"></textarea>
            <button id="btn" type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
        def local_css(file_name):
                    with open(file_name) as f:
                        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

        local_css("style.css")

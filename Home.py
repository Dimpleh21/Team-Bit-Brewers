import base64
import streamlit as st

st.set_page_config(page_title='Disease Detection',page_icon='🧊',initial_sidebar_state="collapsed")
@st.cache_data
def get_img_as_base64(file):
    with open(file,"rb") as f:
        data=f.read()
    return base64.b64encode(data).decode()
get_img_as_base64("dna.jpg")



st.markdown(
    """
    <style>
    /* Set font family and size */
    .my-text {
        font-family: "K2D", sans-serif;
        font-size: 60px;
        justify-content: center;
    }

    
    </style>
    """,
    unsafe_allow_html=True
)


# Text content with custom class
st.markdown('<div class="text-container"><span class="my-text">WE START WHERE THE WORLD STOPS</span></div>', unsafe_allow_html=True)
st.markdown(
    """
    <style>
    /* Position the button */
    .button-container {
        position: relative;
        top: 70%;
        left: 70%;
        transform: translate(-90%, -50%);
    }
    </style>
    """,
    unsafe_allow_html=True
)
button_clicked = st.button(label="Get started", key="custom_button", )
button_container = st.markdown(
    f'<div class="button-container"></div>',
    unsafe_allow_html=True
)
if button_clicked:
    st.switch_page("pages/Dashboard.py")

st.markdown(
    """
    <style>
    /* Position the button */
    .row-widget.stButton{
        position: absolute;
        top: 120%;
        left: 90%;
        transform: translate(-50%, 400%);
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    /* Position the button */
    .my-text{
        position: relative;
        top: 50%;
        left: -20%;
        transform: translate(-50%, -50%);
        color
    }
    </style>
    """,
    unsafe_allow_html=True
)
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .main {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-attachment: local;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('dna.jpg')


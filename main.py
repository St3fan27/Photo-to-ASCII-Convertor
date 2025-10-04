import streamlit as st
from image_convertor import ASCIIConverter

# Create an instance of the converter
converter = ASCIIConverter()

st.title("🎨 Photo to ASCII Converter")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Width selector
width = st.select_slider(
    "Select ASCII width",
    options=[50, 100, 150, 200],
    value=100
)

if uploaded_file:
    # Convert image to ASCII
    ascii_art = converter.convert(uploaded_file, new_width=width)

    # Display in a code block
    st.subheader("ASCII Art")
    st.code(ascii_art, language="text")

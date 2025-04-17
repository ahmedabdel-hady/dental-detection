import streamlit as st
from PIL import Image
import random
import time

# Define class names (dental conditions)
class_names = ['Caries', 'Gingivitis', 'Tooth Discoloration', 'Ulcers', 'Hypodontia', 'Calculus']

# Dummy function to simulate image processing and prediction
def predict_image(image):
    # Simulate a delay for processing
    time.sleep(2)
    return random.choice(class_names)

# Set custom page configurations
st.set_page_config(page_title="Dental Condition Classifier", page_icon="🦷")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .header {
        text-align: center;
        font-size: 36px;
        color: #2e86c1;
    }
    .subheader {
        text-align: center;
        font-size: 20px;
        color: #2e86c1;
    }
    .image-container {
        display: flex;
        justify-content: center;
    }
    .prediction {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #2ecc71;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Page title
st.markdown("<h1 class='header'>🦷 Dental Condition Classifier</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Upload an image to classify dental conditions.</p>", unsafe_allow_html=True)

# File uploader for image
uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image in the center
    st.markdown("<div class='image-container'>", unsafe_allow_html=True)
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Simulate prediction with a loading spinner
    with st.spinner("Processing image..."):
        predicted_label = predict_image(image)

    # Display the predicted dental condition
    st.markdown(f"<div class='prediction'>Predicted Dental Condition: {predicted_label}</div>", unsafe_allow_html=True)

# Footer to improve user experience
st.markdown("<p style='text-align: center; margin-top: 40px;'>Powered by AI 🧠 | Streamlit</p>", unsafe_allow_html=True)

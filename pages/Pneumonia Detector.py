import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

# # Load the pre-trained CNN models
# /*pneumonia_model = tf.keras.models.load_model('pneumonia_detection_model.h5')
# other_disease_model = tf.keras.models.load_model('other_disease_detection_model.h5')

# # Define the classes for each prediction
# pneumonia_class_names = ['Normal', 'Pneumonia']
# other_disease_class_names = ['Healthy', 'Disease']

# # Function to preprocess the image
# def preprocess_image(image):
#     image = tf.image.resize(image, (224, 224))
#     image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
#     return image

# # Function to make predictions for pneumonia detection
# def predict_pneumonia(image):
#     img_array = np.array(image)
#     img_array = preprocess_image(img_array)
#     img_array = np.expand_dims(img_array, axis=0)
#     prediction = pneumonia_model.predict(img_array)
#     return pneumonia_class_names[np.argmax(prediction)]

# # Function to make predictions for other disease detection
# def preprocess_image_for_other_disease(image):
#     # Preprocess image for other disease model
#     # Add your preprocessing steps here
#     return image

# def predict_other_disease(image):
#     img_array = np.array(image)
#     img_array = preprocess_image_for_other_disease(img_array)
#     img_array = np.expand_dims(img_array, axis=0)
#     prediction = other_disease_model.predict(img_array)
#     return other_disease_class_names[np.argmax(prediction)]*/

# Streamlit app
st.set_page_config(page_title='Disease Detection',page_icon='🧊',initial_sidebar_state="expanded")
st.title('Disease Detection')
st.markdown(
    """
    <style>
    body {
        background-image: url('dna.jpg');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

uploaded_image = st.file_uploader("Choose an image...", type="jpg")
st.write('WE START WHERE THE WORLD STOPS')



if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Use the CNN models to make predictions on the uploaded image
    pneumonia_prediction = predict_pneumonia(image)
    other_disease_prediction = predict_other_disease(image)

    st.write(f"Pneumonia Prediction: {pneumonia_prediction}")
    st.write(f"Other Disease Prediction: {other_disease_prediction}")
    

   

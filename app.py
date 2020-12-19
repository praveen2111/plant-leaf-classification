import streamlit as st
import io
import numpy as np
from PIL import Image
import tensorflow as tf
import efficientnet.tfkeras as efn

st.title("Plant Disease Detection")
st.write("Just upload your Plant's Leaf Image and get predictions if your plant is healthy or not.")

#Loading Model
model = tf.keras.models.load_model("model.h5")

#File uploader
uploaded_file = st.file_uploader("Choose your plant leaf image", type=['png','jpg'])

predictions_map = {0:"is Healthy", 1:"has Multiple diseases", 2:"has Rust", 3:"has Scab"}

if uploaded_file is not None:

    image = Image.open(io.BytesIO(uploaded_file.read()))

    st.image(image,use_column_width=True)

    #Image Preprocessing
    resized_image = np.array(image.resize((512,512)))/255.
    #Adding batch dimensions
    image_batch = resized_image[np.newaxis,:,:,:]
    # Getting the predictions from the model
    predictions_arr = model.predict(image_batch)

    predictions = np.argmax(predictions_arr)

    result_text = f"The Plant Leaf {predictions_map[predictions]} with {int(predictions_arr[0][predictions]*100)}% Probability"

    if predictions==0:
        st.success(result_text)
    else:
        st.error(result_text)

    
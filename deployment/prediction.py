import streamlit as st
import cv2
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import datetime

# Load File

model_imp = load_model('./src/model.keras')

def run():
    # Title
    st.title('Safe and Unsafe Working Condition')

    # Sub Header
    st.subheader('Safety Prediction of Working Condition Image ')

    # Image
    image = Image.open('./src/image12.jpg')
    st.image(image)

    # Create form
    with st.form(key='safety-prediction'):

        st.markdown('Data ID')

        date = st.date_input("Select a date", help='Input the time the photo was taken or obtained')
        time = st.time_input("Select a time")
        timestamp = datetime.datetime.combine(date, time)

        name_id = st.text_input('ID', value='---name/id---', help='Input your name or identity')

        uploaded_img = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])

        submitted = st.form_submit_button('Predict')

    # Data inference
    data_inf_input = {
        'timestamp': timestamp,
        'name_id': name_id,
    }

    # Data frame
    st.markdown('Data Summary:')
    data_inference = pd.DataFrame([data_inf_input])
    st.dataframe(data_inference)

    # Preprocessing

    if uploaded_img is not None:
        img_pil = Image.open(uploaded_img).convert('RGB')
        img_arr = np.array(img_pil)
        # Resize as input model (img_height × img_width)
        img_resized = cv2.resize(img_arr, (200, 200))
        # Scaling
        img_array = np.array(img_resized) / 255.
        # Change dimension
        img_dims = np.expand_dims(img_array, axis=0)
        st.image(uploaded_img)
    else:
        st.warning("Please upload an image to continue.")

    st.markdown('Result:')
    # Prediction
    if submitted:
        prob = model_imp.predict(img_dims)

        # Convert to class (0 = safe, 1 = unsafe)
        pred = 1 if prob >= 0.5 else 0
        class_names = ['SAFE', 'UNSAFE']
        label = class_names[pred]
        percentage = prob[0][0] * 100

        # Result
        st.write(f"#### Prediction: this image consider {label} working condition.")
        st.write(f"##### Probability: {percentage:.2f} % ")

if __name__ == '__main__':
    run()
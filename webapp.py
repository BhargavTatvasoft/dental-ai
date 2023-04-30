import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
import os
import cv2
from tensorflow.keras import layers
from tensorflow.keras import preprocessing
import smtplib, ssl
from email.message import EmailMessage
import imghdr


st.header("DentalAI - Revolutionising diagnoses")


def predict(image, emailTo, name):
    
    port = 587
    model = load_model('CNN.h5')
    input_shape = ((60, 60, 3))
    
    image = cv2.resize(image, (60, 60))
    
    image_array = np.expand_dims(image, axis=0)
    
    result = model.predict(image_array)
    
    
    if result[0][0] > 0.40:
        emailFrom = "periodetection@outlook.com"
        smtp_server = "smtp-mail.outlook.com"
        password = "yash@2005"
        
        message = f"""\
            Subject: Patient Notification

            Your patient {name} has a dental disease. Kindly get in touch with them. """
        
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            
            server.login(emailFrom, password)
            server.sendmail(emailFrom, emailTo, message)
        return "You have a noticeable periodontal issue. Your dentist has been notified"
        
        
        
    elif result[0][0] <= 0.40:
        return "Your teeth are clean! No need to worry"
    
    


def main():
    name = st.text_input("Enter your name")
    emailTo = st.text_input("Enter your dentist's email address")
    file = st.file_uploader("Upload the image of your teeth..", type=['jpg', 'jpeg','png'])
    if file:
        img = Image.open(file)
        imgCV = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        result = predict(imgCV, emailTo, name)
        st.caption(result)
    


main()
    
    
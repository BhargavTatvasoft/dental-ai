# dental-ai
A webapp built on a convolutional neural network and a dataset (from scratch), which aims to make the process of detecting and diagnosing dental diseases much easier. 

# How it works (front-end)

It's a simple process: 

1. Enter your name and your dentist's email ID. (soon to feature mobile no. option instead of email)
2. Upload frontal image of teeth.
3. Wait for a few seconds ... and voila! Your teeth have been diagnosed.
4. If your teeth are a-okay, you'll be told so, but if there is a risk of a dental issue, your dentist will be sent an email notifying them of the same.

# How it works (back-end)

1. Name and email ID are collected and stored as variables to be used with smtplib later.
2. A convolutional neural network (CNN) built using TensorFlow was trained on a custom dataset of ~1000 images of teeth compiled by myself.
3. The model was saved in a .h5 file and loaded into a different .py file, where the uploaded image is checked by the CNN.
4. Depending on the predicted result, an email can be sent to the dentist using smtplib (outlook). 

import streamlit as st
import PIL
from PIL import Image
import os
import io



st.title('Caries-Detector v0.6')

st.header('Please upload an image')

#load image
#image = Image.open(file).convert('jpg') 

import imageio.v3 as iio
import cv2

def get_image_path(img):
    # Create a directory and save the uploaded image.
    file_path = f"/content/{img.name}"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as img_file:
        img_file.write(img.getbuffer())
    return file_path
def get_image_name(img):
    # Create a directory and save the uploaded image.
    file_path = f"/content/{img.name}"
    file_name = f"{img.name}"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as img_file:
        img_file.write(img.getbuffer())
    return file_name

uploaded_file = st.file_uploader("**Upload a Chest X-Ray Image**", type= ['png', 'jpg', 'jpeg'] )
if st.button('Запустить'):
    #os.system("rm 'democaries2.jpg'")
    #os.system("rmdir 'my_project'")
    os.system("rm -rf 'my_project'")
    source2=get_image_path(uploaded_file)
    source3=get_image_name(uploaded_file)
   # print(source3)
    
    (os.system("yolo task=detect mode=predict model='Caries-Detector-v0.6/best.pt' project='my_project' name='my_results' show=True conf=0.5 source=%s"% source3))
#detect object

#os.path.exists(file_path):

col1, col2 = st.columns(2)

if st.button('Отобразить'):
    source_image=('/content/my_project/my_results/%s'% get_image_name(uploaded_file)) 

# Adding image to the first column if image is uploaded
    with col1:
        # Opening the uploaded image
        uploaded_image = PIL.Image.open(source_image)
        # Adding the uploaded image to the page with a caption
        st.image(source_image,
                  caption="Uploaded Image",
                  use_column_width=True
                  )

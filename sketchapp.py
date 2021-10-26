
import streamlit as st
import numpy as np
from PIL import Image
import cv2

def sketch(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray_invert = cv2.bitwise_not(img_gray)
    img_blur = cv2.GaussianBlur(img_gray_invert, (21,21), sigmaX=0,sigmaY=0)
    img_blur_invert = cv2.bitwise_not(img_blur)
    sketch_img = cv2.divide(img_gray,img_blur_invert, scale=256)
    return(sketch_img)

st.title("convert your image into pencil sketch")

file_image = st.file_uploader("upload your image", type=['jpeg','jpg', 'pmg'])

if file_image is None:
    st.write("Please Upload a Photo")

else:
    img = Image.open(file_image)
    final_sketch = sketch(np.array(img))
    st.write("Input Image")
    st.image(img)
    st.write("Output Image")
    st.image(final_sketch)
    if st.button("download sketch image"):
        img_final = Image.fromarray(final_sketch)
        img_final.save('sketch_img.jpeg')
        st.write('download completed')


import streamlit as st 
import cv2
import io 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def main():
    #title
    st.title("Thin Section: Porosity Calculator")
    st.write("*Calculate your thin section porosity*")
    
    #uploadfile
    uploaded_file = st.file_uploader(label="Upload your PNG or JPG File", type=['jpg','png','jpeg'])
        
    try:
        original_image = Image.open(uploaded_file)
        original_image = np.array(original_image)
        processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(processed_image,(5,5),0)
    
        threshold_min = st.slider("THRESHOLD SLIDER",min_value=0,max_value=255)
        ret3,th3 = cv2.threshold(blur,threshold_min,255,cv2.THRESH_BINARY)
        
        st.image([original_image,th3],use_column_width='auto',caption=['Original','Calculated'])
        
        n_white_pix = np.sum(th3 == 255) #255 dan 0 adalah RGB code
        n_black_pix = np.sum(th3 == 0)
        porosity = n_black_pix/(n_white_pix+n_black_pix)
        
        st.write('# Porosity',porosity.round(3))
    except Exception as e:
        print(st.write('## Please Upload the Image'))

if __name__ == '__main__':
    main()
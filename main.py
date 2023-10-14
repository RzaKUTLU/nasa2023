import numpy as np
import streamlit as st

def drone():
    page_by_img = """
             <style>
             [data-testid="stAppViewContainer"]{
             background: url("https://i.gazeteoksijen.com/storage/files/images/2022/06/01/yasamak-bir-orman-gibi-kardescesine-GDL0.jpg");
             background-size: cover;top: 0px}

             [data-testid="stHeader"]{
             background-color: rgba(0,0,0,0);
              }

             [data-testid="stToolbar"]{
             right: 2rem;}
             </style>
              """
    st.markdown(page_by_img, unsafe_allow_html=True)
    st.text("")
    st.text("")

    st.markdown('<div style="color: white;font-size: 32px;font-weight: bold;">Fire Fighting with Drone WEBSITE</div>',
                unsafe_allow_html=True)

    # YouTube video link
    video_link = "https://youtu.be/bRrNiXUAR7I"
    st.video(video_link)

if __name__ == "__main__":
    drone()

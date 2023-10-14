import numpy as np
import streamlit as st

def drone():


    st.markdown('<div style="color: white;font-size: 32px;font-weight: bold;">Fire Fighting with Drone WEBSITE</div>',
                unsafe_allow_html=True)

    # YouTube video link
    video_link = "https://youtu.be/bRrNiXUAR7I"
    st.video(video_link)

if __name__ == "__main__":
    drone()

import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_animation_1 = "https://lottie.host/85ee42ed-6bcd-4c3c-ada9-550eba743f1c/8zHYd2FA7w.json"
lottie_anime_json = load_lottie_url(lottie_animation_1)

lottie_animation_2 = "https://lottie.host/91fe3eb1-f734-4dd0-a42d-f9cd7c05bf41/KdhnxKznkT.json"
lottie_anime_json_2 = load_lottie_url(lottie_animation_2)

# Create a layout with three columns: left for the student animation, center for the gesture text, and right for the learn animation
col1, col2, col3 = st.columns([4, 3, 4])  # Adjust column widths as needed

# Place the student animation in the left column
with col1:
    st_lottie(lottie_anime_json_2, key="student")

# Place the gesture text in the center column
with col2:
    st.markdown(
        "<h1 style='text-align: center; color: green; margin: 0;'>Gesture</h1>", 
        unsafe_allow_html=True
    )

# Place the learn animation in the right column
with col3:
    st_lottie(lottie_anime_json, key="learn")

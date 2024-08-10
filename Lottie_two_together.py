import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_animation_1 = "https://lottie.host/91fe3eb1-f734-4dd0-a42d-f9cd7c05bf41/KdhnxKznkT.json"
lottie_anime_json_1 = load_lottie_url(lottie_animation_1)

lottie_animation_2 = "https://lottie.host/85ee42ed-6bcd-4c3c-ada9-550eba743f1c/8zHYd2FA7w.json"
lottie_anime_json = load_lottie_url(lottie_animation_2)

# Center the image at the top
st_lottie(lottie_anime_json_1, key="student", height=300)

# Center the text below the image
st.markdown(
    "<h1 style='text-align:center; color: green;'>Gesture <span style='color: orange;'>Learn</span></h1>", 
    unsafe_allow_html=True
)

# Place the learn animation in the right column
# with col3:
#     st_lottie(lottie_anime_json, key="learn")

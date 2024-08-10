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

# Display the Lottie animation in the sidebar
with st.sidebar:
    st_lottie(lottie_anime_json_1, key="student_sidebar", height=250)

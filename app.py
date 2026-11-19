"""Happy Birthday Sweety - Streamlit wrapper.

Shows index.html full screen. The photo is embedded into the page
so it loads inside Streamlit's frame.
"""
import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

HERE = Path(__file__).parent

st.set_page_config(page_title="Happy Birthday Sweety", page_icon="🎂", layout="wide")

# Remove Streamlit's own header, padding and footer so the page fills the screen.
st.markdown(
    """
    <style>
      #MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {display: none !important;}
      .block-container, [data-testid="stMainBlockContainer"] {padding: 0 !important; max-width: 100% !important;}
      [data-testid="stAppViewContainer"], .stApp {background: #170a2b;}
      iframe {height: 100vh !important; width: 100% !important; border: 0; display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (HERE / "index.html").read_text(encoding="utf-8")
photo = base64.b64encode((HERE / "photo.jpg").read_bytes()).decode()
html = html.replace('src="photo.jpg"', f'src="data:image/jpeg;base64,{photo}"')

components.html(html, height=900, scrolling=True)

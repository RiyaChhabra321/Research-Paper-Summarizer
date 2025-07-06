import streamlit as st
import google.generativeai as genai
import re

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def clean_text(text):
    cleaned = re.sub(r'\s+', ' ', text)  # Collapse spaces
    cleaned = re.sub(r'[^\x00-\x7F]+', ' ', cleaned)  # Remove non-ASCII
    return cleaned.strip()


def summarize_text(text):
    try:
        cleaned = clean_text(text)
        prompt = f"Summarize this academic text clearly in a few

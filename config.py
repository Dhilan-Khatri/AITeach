import os

# Try Streamlit's secrets first (used on Streamlit Cloud); ignore if unavailable.

try:

import streamlit as st

_secrets = st.secrets

except Exception:

_secrets = {}

def _get(name, default=""):

# look in Streamlit secrets, then environment variables, then a default

if name in _secrets:

return _secrets[name]

return os.environ.get(name, default)

GROQ_API_KEY = _get("GROQ_API_KEY")

HF_API_KEY = _get("HF_API_KEY")

GROQ_MODELS = ["llama-3.1-8b-instant", "llama-3.3-70b-versatile"]

HF_MODELS = ["meta-llama/Llama-3.1-8B-Instruct"]

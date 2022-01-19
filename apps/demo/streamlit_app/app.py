# GeneSpeak demo app

import os
import streamlit as st
import pyautogui
from utils import setup_sidebar, setup_preamble, setup_app

st.header("GeneSpeak - Demo App")

setup_preamble()

options, buttons = setup_sidebar()

placeholder = st.empty()
with placeholder.container():
    st.write("## Simple Conversion: `Text` 🔄 `DNA`")
    setup_app(options)

if buttons["reset"] or buttons["refresh"]:
    if os.environ.get("DISPLAY") is not None:
        pyautogui.hotkey("ctrl", "F5")
    else:
        placeholder.empty()
        st.warning("Refresh the webpage manually!")

# GeneSpeak demo app

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
    pyautogui.hotkey("ctrl", "F5")

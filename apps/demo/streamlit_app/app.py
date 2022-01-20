# GeneSpeak demo app

import os
import streamlit as st
# import pyautogui
from utils import setup_sidebar, setup_preamble, setup_app, is_streamlit_cloud

## To emulate streamlit cloud specific app
## restrictions uncomment the following line
# os.environ["ST_IS_STREAMLIT_CLOUD"] = "1"

st.header("GeneSpeak - Demo App")

setup_preamble()

options, buttons = setup_sidebar()

placeholder = st.empty()
with placeholder.container():
    st.write("## Simple Conversion: `Text` 🔄 `DNA`")
    setup_app(options)

if buttons["reset"] or buttons["refresh"]:
    if not is_streamlit_cloud():
        # if os.environ.get("DISPLAY") is not None:
        #     try:
        #         pyautogui.hotkey("ctrl", "F5")
        #     except Exception as e:
        #         st.error(e)
        pass
    else:
        placeholder.empty()
        st.warning("Refresh the webpage manually!")

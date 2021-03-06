# GeneSpeak demo app

# import os
# import pyautogui # This does not work on Streamlit Cloud
# import utils as U
from composer import appfactory as A
import streamlit as st

## To emulate streamlit cloud specific app
## restrictions uncomment the following line
# os.environ["ST_IS_STREAMLIT_CLOUD"] = "0"

st.header("GeneSpeak - Demo App 🧬")

A.setup_preamble()

options, buttons = A.setup_sidebar()

placeholder = st.empty()
with placeholder.container():
    st.write("## Simple Conversion: `Text` 🔄 `DNA`")
    A.setup_app(options)

if buttons["reset"] or buttons["refresh"]:
    # if not U.is_streamlit_cloud():
    #     # if os.environ.get("DISPLAY") is not None:
    #     #     try:
    #     #         pyautogui.hotkey("ctrl", "F5")
    #     #     except Exception as e:
    #     #         st.error(e)
    #     pass
    # else:
    placeholder.empty()
    st.warning("Refresh the webpage manually!")

# st.info("Showing an IFrame")
# st.components.v1.iframe("https://sugatoray.github.io/genespeak", height=500, scrolling=True)

import os
import streamlit as st
import itertools
import pyperclip
from genespeak import text_to_dna, dna_to_text
from textwrap import dedent
from dataclasses import dataclass
from typing import Tuple, Dict, Optional



DEFAULT_SCHEMA = "ACGT"

@st.cache
@dataclass
class Defaults:
    TEXT_INPUT_ASCII: str = "Hello World!"
    TEXT_INPUT_UTF8: str = "Hello World 👍!"
    TEXT_INPUT_OPTIONS: Tuple[str] = ("Text Field", "Text Area")
    CONVERT_TO_OPTIONS: Tuple[str] = ("DNA", "TEXT")
    CONVERSION_STRATEGIES: Tuple[str] = ("ascii", "utf-8")
    CONVERSION_SCHEMA: str = DEFAULT_SCHEMA
    CONVERSION_SCHEMAS: Tuple[str] = tuple(''.join(i) for i in itertools.permutations(DEFAULT_SCHEMA, 4))
    GENESPEAK_BANNER_URL: str = r"https://raw.githubusercontent.com/sugatoray/genespeak/master/docs/assets/images/genespeak_banner_01.png"
    APP_URL: str = r"https://share.streamlit.io/sugatoray/genespeak/master/apps/demo/streamlit_app/app.py"
    APP_URL_SHORT: str = r"https://tinyurl.com/genespeak-demo"


def add_about_section():
    """Adds an About section to the app."""

    st.write("## ℹ️ About")
    st.info(dedent(f"""
        This web [app][#streamlit-app] is maintained by [Sugato Ray][#linkedin].
        You can follow me on social media:

        - [@sugatoray | LinkedIn][#linkedin]
        - [@sugatoray | Twitter][#twitter]
        - [@sugatoray | GitHub][#github]

        [#linkedin]: https://www.linkedin.com/in/sugatoray/
        [#twitter]: https://twitter.com/sugatoray
        [#github]: https://github.com/sugatoray
        [#streamlit-app]: {Defaults.APP_URL}

        Short URL: {Defaults.APP_URL_SHORT}
        """)
    )

def setup_sidebar() -> Tuple[Dict, Dict]:
    with st.sidebar:
        st.write("## ⚙️ Parameters")

        options = dict()
        buttons = dict()
        options["text_input_type"] = st.radio(
            label="Choose text input type",
            options=Defaults.TEXT_INPUT_OPTIONS,
            index=0,
        )
        options["convert_to"] = st.radio(
            label="Convert to",
            options=Defaults.CONVERT_TO_OPTIONS,
            index=0,
        )
        options["strategy"] = st.radio(
            label="Convertion strategy",
            options=Defaults.CONVERSION_STRATEGIES,
            index=0,
        )
        options["schema"] = st.selectbox(
            label="Convertion schema",
            options=Defaults.CONVERSION_SCHEMAS,
            index=0,
        )

        col1, col2, _ = st.columns([1, 1, 2])
        with col1:
            buttons["reset"] = st.button("Reset")
        with col2:
            buttons["refresh"] = st.button("Refresh")

        st.write("---")

        add_about_section()

    return options, buttons


# @st.cache(suppress_st_warning=True)
def setup_preamble():
    with st.container():
        st.image(Defaults.GENESPEAK_BANNER_URL, caption="GeneSpeak Banner")

        st.write(dedent("""
            <!--- BADGES: START --->
            [![GitHub - License](https://img.shields.io/github/license/sugatoray/genespeak?logo=github&style=flat&color=green)][#github-license]
            [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/genespeak?logo=pypi&style=flat&color=blue)][#pypi-package]
            [![PyPI - Package Version](https://img.shields.io/pypi/v/genespeak?logo=pypi&style=flat&color=orange)][#pypi-package]
            [![Conda - Platform](https://img.shields.io/conda/pn/conda-forge/genespeak?logo=anaconda&style=flat)][#conda-forge-package]
            [![Conda (channel only)](https://img.shields.io/conda/vn/conda-forge/genespeak?logo=anaconda&style=flat&color=orange)][#conda-forge-package]
            [![Conda Recipe](https://img.shields.io/static/v1?logo=conda-forge&style=flat&color=green&label=recipe&message=genespeak)][#conda-forge-feedstock]
            [![Docs - GitHub.io](https://img.shields.io/static/v1?logo=github&style=flat&color=pink&label=docs&message=genespeak)][#docs-package]
            [![CodeFactor](https://www.codefactor.io/repository/github/sugatoray/genespeak/badge)][#codefactor-package]

            [#github-license]: https://github.com/sugatoray/genespeak/blob/master/LICENSE
            [#pypi-package]: https://pypi.org/project/genespeak/
            [#conda-forge-package]: https://anaconda.org/conda-forge/genespeak
            [#conda-forge-feedstock]: https://github.com/conda-forge/genespeak-feedstock
            [#docs-package]: https://sugatoray.github.io/genespeak/
            [#codefactor-package]: https://www.codefactor.io/repository/github/sugatoray/genespeak
            <!--- BADGES: END --->

            GeneSpeak allows you to encode regular text as DNA single-strand
            using base-pairs (`A`, `C`, `G`, `T`) and convert back to the
            original text. Text encoding is done for both `ascii` and
            `utf-8` characters based on the `strategy` keyword argument.

            """),
            unsafe_allow_html=True,
        )

        st.error(dedent("""
            If your text includes ***emojis*** or ***non-english*** characters, you **must
            use `utf-8` conversion strategy** to convert unicode characters into equivalent DNA
            base-pair sequence.
            """)
        )


def setup_app(options: Dict):

    on_st_cloud = is_streamlit_cloud()
    # Determine conversion direction (Text to DNA) or (DNA to Text)
    if options["convert_to"] == "DNA":
        _from, _to = "TEXT", "DNA"
    elif options["convert_to"] == "TEXT":
        _from, _to = "DNA", "TEXT"

    # Determine default text based on schema: ascii or utf-8
    text_value = ""
    if options["strategy"] == "ascii":
        text_value = Defaults.TEXT_INPUT_ASCII
    elif options["strategy"] == "utf-8":
        text_value = Defaults.TEXT_INPUT_UTF8

    if _to == "TEXT":
        text_value = text_to_dna(text_value, schema=options["schema"], strategy=options["strategy"])

    # Get Input (X) from User
    if options["text_input_type"] == "Text Field":
        X = st.text_input(f"{_from} Input as string", value=text_value)
    else:
        X = st.text_area(f"{_from} Input as string", value=text_value)

    # Evaluate Output (Y) based on Input-type,
    # conversion schema and strategy.
    if options["convert_to"] == "DNA":
        Y = text_to_dna(text=X, schema=options["schema"], strategy=options["strategy"])
    elif options["convert_to"] == "TEXT":
        if X:
            diff = set(X.upper()) - set(list(Defaults.CONVERSION_SCHEMA))
            if diff:
                st.error("Input is not valid dna to convert from.")
                st.stop()
            else:
                Y = dna_to_text(dna=X, schema=options["schema"], strategy=options["strategy"])

    # Display User Input (X)
    with st.expander("User Input 👇", expanded=True):
        if not on_st_cloud:
            col1, col2 = st.columns([4, 1])
            with col1:
                show_input(options, X)

            with col2:
                st.button("Copy Input", help="Click to copy input to clipboard", on_click=pyperclip.copy(X))
        else:
            show_input(options, X)

    # Display Generated Output (Y)
    st.success("### Output 🎁")
    payload = {
        "input": X,
        "output": Y,
        "metadata": {
            "schema": options["schema"],
            "strategy": options["strategy"],
            "convert_to": options["convert_to"],
        },
    }

    "Test text here."

    with st.expander(f"Output: {_from} ➡️ {_to} 👇", expanded=True):
        if not on_st_cloud:
            col1, col2 = st.columns([4, 1])
            with col1:
                show_output(options, Y)
            with col2:
                st.button(
                    label="Copy Result",
                    help="Click to copy result to clipboard",
                    on_click=pyperclip.copy(Y)
                )
        else:
            show_output(options, Y)
        with st.container():
            st.info("JSON Output")
            st.json(payload)


def show_input(options, X):
    if options["convert_to"] == "DNA":
        st.write(f"{X}")
    else:
        st.write(f"`{X}`")

def show_output(options, Y):
    if options["convert_to"] == "DNA":
        st.write(f"`{Y}`")
    else:
        st.write(f"{Y}")

def transfer_payload(payload: Dict, mode: str="json", key: Optional[str]=None):
    """Function to associate with a button's on-click feature.

    This either writes a json (from the input dict ``p``) to the app,
    or copies a certain content from the json by a key.
    """
    if mode == "json":
        st.json(payload)
    else:
        if key is not None:
            pyperclip.copy(payload.get(key))

def is_streamlit_cloud(watchvariable: str="ST_IS_STREAMLIT_CLOUD") -> bool:
    """If running in the Streamlit Cloud, set environment variable
    (the same as ``watchvariable``) to 1.
    """
    return bool(os.environ.get(watchvariable, "0") == "1")

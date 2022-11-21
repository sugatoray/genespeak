from textwrap import dedent
from typing import Dict, Tuple

import streamlit as st
from composer import utils as U
from composer import visualization as V

Defaults = U.Defaults


__all__ = [
    "setup_app",
    "setup_preamble",
    "setup_sidebar",
]


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
        options["show_balloons"] = st.checkbox(
            label="Show balloons 🎈🎉",
            value=Defaults.SHOW_BALLOONS,
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

        U.add_about_section()

    return options, buttons


# @st.cache(suppress_st_warning=True)
def setup_preamble():
    with st.container():
        st.image(Defaults.GENESPEAK_BANNER_URL, caption="GeneSpeak Banner")

        st.write(dedent("""\
            
            [![GitHub - License](https://img.shields.io/github/license/sugatoray/genespeak?logo=github&style=flat&color=green)][#github-license]
            [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/genespeak?logo=pypi&style=flat&color=blue)][#pypi-package]
            [![PyPI - Package Version](https://img.shields.io/pypi/v/genespeak?logo=pypi&style=flat&color=orange)][#pypi-package]
            [![Conda - Platform](https://img.shields.io/conda/pn/conda-forge/genespeak?logo=anaconda&style=flat)][#conda-forge-package]
            [![Conda (channel only)](https://img.shields.io/conda/vn/conda-forge/genespeak?logo=anaconda&style=flat&color=orange)][#conda-forge-package]
            [![Conda Recipe](https://img.shields.io/static/v1?logo=conda-forge&style=flat&color=green&label=recipe&message=genespeak)][#conda-forge-feedstock]
            [![Docs - GitHub.io](https://img.shields.io/static/v1?logo=github&style=flat&color=pink&label=docs&message=genespeak)][#docs-package]
            [![CodeFactor](https://www.codefactor.io/repository/github/sugatoray/genespeak/badge)][#codefactor-package]
            [![GitHub Repo](https://img.shields.io/static/v1?logo=github&style=flat&color=blue&label=code&message=genespeak%20⭐)][#github-repo]

            [#github-repo]: https://github.com/sugatoray/genespeak
            [#github-license]: https://github.com/sugatoray/genespeak/blob/master/LICENSE
            [#pypi-package]: https://pypi.org/project/genespeak/
            [#conda-forge-package]: https://anaconda.org/conda-forge/genespeak
            [#conda-forge-feedstock]: https://github.com/conda-forge/genespeak-feedstock
            [#docs-package]: https://sugatoray.github.io/genespeak/
            [#codefactor-package]: https://www.codefactor.io/repository/github/sugatoray/genespeak

            GeneSpeak allows you to encode regular text as DNA single-strand
            using base-pairs (`A`, `C`, `G`, `T`) and convert back to the
            original text. Text encoding is done for both `ascii` and
            `utf-8` characters based on the `strategy` keyword argument.

            """
            ),
            unsafe_allow_html=True,
        )

        st.error(
            dedent(
                """
            If your text includes ***emojis*** or ***non-english*** characters, you **must
            use `utf-8` conversion strategy** to convert unicode characters into equivalent DNA
            base-pair sequence.
            """
            )
        )


def setup_app(options: Dict):
    """Sets up the app."""

    _, _, options = U.get_conversion_endpoints(options)
    X = U.get_input(options)
    Y = U.eval_output(X, options)
    U.display_input(X, options)
    U.display_output(X, Y, options)

    dna = "ACGT"
    if options["convert_to"] == "DNA":
        dna = Y
    elif options["convert_to"] == "TEXT":
        dna = X
    V.display_annotated_dna(
        options,
        dna=dna,
    )

    if options["convert_to"] == "TEXT":
        U.display_guessed_text(X, options)

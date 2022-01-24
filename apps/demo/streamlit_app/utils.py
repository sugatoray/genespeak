import os
import streamlit as st
import itertools
import pyperclip
from genespeak import text_to_dna, dna_to_text
from textwrap import dedent
from dataclasses import dataclass
from typing import Tuple, Dict, List, Optional


__all__ = [
    "Defaults",
    "is_streamlit_cloud",
    "add_about_section",
    "get_conversion_endpoints",
    "get_input",
    "eval_output",
    "display_input",
    "display_output",
    "display_guessed_text",
]


DEFAULT_SCHEMA = "ACGT"


def is_streamlit_cloud(watchvariable: str = "ST_IS_STREAMLIT_CLOUD") -> bool:
    """If running in the Streamlit Cloud, set environment variable
    (the same as ``watchvariable``) to 1.
    """
    return bool(os.environ.get(watchvariable, "0") == "1")


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
    ON_ST_CLOUD: bool = is_streamlit_cloud()


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


def transfer_payload(payload: Dict, mode: str = "json", key: Optional[str] = None):
    """Function to associate with a button's on-click feature.

    This either writes a json (from the input dict ``p``) to the app,
    or copies a certain content from the json by a key.
    """
    if mode == "json":
        st.json(payload)
    else:
        if key is not None:
            pyperclip.copy(payload.get(key))


def get_conversion_endpoints(options: Dict) -> Tuple[str, str, Dict]:
    """Returns conversion direction with endpoints
    (Text to DNA) or (DNA to Text)."""
    _from, _to = "TEXT", "DNA"
    if options["convert_to"] == "DNA":
        _from, _to = "TEXT", "DNA"
    elif options["convert_to"] == "TEXT":
        _from, _to = "DNA", "TEXT"
    options["convert_from"] = _from
    return _from, _to, options


def get_default_input_text_value(options: Dict) -> str:
    """Determines and returns the default text for the input box/area based on chosen schema: ``ascii`` or ``utf-8``."""
    text_value = ""
    if options["strategy"] == "ascii":
        text_value = Defaults.TEXT_INPUT_ASCII
    elif options["strategy"] == "utf-8":
        text_value = Defaults.TEXT_INPUT_UTF8

    # When converting from DNA to TEXT, this will
    #    autofill the default text_value with its
    #    DNA-equivalent for the chosen schema.
    if options["convert_to"] == "TEXT":
        text_value = text_to_dna(text_value, schema=options["schema"], strategy=options["strategy"])

    return text_value


def get_input(options: Dict) -> str:
    """Returns the text input (``X``), which could be either
    plain TEXT or DNA from the user.
    """
    X = ''
    convert_from = options["convert_from"]
    text_value = get_default_input_text_value(options)
    if options["text_input_type"] == "Text Field":
        X = st.text_input(f"{convert_from} Input as string", value=text_value)
    else:
        X = st.text_area(f"{convert_from} Input as string", value=text_value)

    return X


def eval_output(X: str, options: Dict, schema: Optional[str] = None, strategy: Optional[str] = None) -> str:
    """Evaluate output (``Y``) based on Input-type (TEXT or DNA),
    conversion schema and strategy.
    """
    schema = options["schema"] if schema is None else schema
    strategy = options["strategy"] if strategy is None else strategy
    Y: str = ""
    if options["convert_to"] == "DNA":
        Y = text_to_dna(text=X, schema=schema, strategy=strategy)
    elif options["convert_to"] == "TEXT":
        if X:
            diff = set(X.upper()) - set(list(Defaults.CONVERSION_SCHEMA))
            if diff:
                st.error("Input is not valid dna to convert from.")
                st.stop()
            else:
                Y = dna_to_text(dna=X, schema=schema, strategy=strategy)
    return Y


def display_input(X: str, options: Dict):
    """Displays User Input (``X``)."""
    with st.expander("User Input 👇", expanded=True):
        if not Defaults.ON_ST_CLOUD:
            col1, col2 = st.columns([4, 1])
            with col1:
                show_input(options, X)

            with col2:
                st.button("Copy Input", help="Click to copy input to clipboard", on_click=pyperclip.copy(X))
        else:
            show_input(options, X)


def display_output(X: str, Y: str, options: Dict):
    """Display Generated Output (``Y``)."""
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

    with st.expander(f'Output: {options["convert_from"]} ➡️ {options["convert_to"]} 👇', expanded=True):
        if not Defaults.ON_ST_CLOUD:
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


def generate_guesses(X: str, options: Dict) -> Dict:
    results = dict()
    for schema in Defaults.CONVERSION_SCHEMAS:
        Y, err, status = '', '', ''
        try:
            Y = eval_output(X, options, schema=schema)
            status = "SUCCESS"
        except Exception as e:
            status = "ConversionFailedError"
            err = e
        finally:
            result = {
                "schema": schema,
                "output": Y,
                "status": status,
                "error": err if err else "NA",
            }
        results.update({schema: result.copy()})
    payload = {
        "input": X,
        "metadata": {
            "strategy": options["strategy"],
            "convert_to": options["convert_to"],
        },
        "guesses": {
            "total": len(Defaults.CONVERSION_SCHEMAS),
            "results": results,
        }
    }
    st.json(payload)
    return payload


def display_guessed_text(X: str, options: Dict, schemas: Optional[List[str]]=None):
    """Displays all the guessed values of TEXT for a given DNA (``X``), and for a list of schemas."""
    st.info(dedent("""### Guess ❓ DNA ➡️ TEXT"""))
    with st.container():
        col1, col2 = st.columns([6, 1])
        with col1:
            schemas = list(schemas if schemas else Defaults.CONVERSION_SCHEMAS)
            num_schemas = len(schemas)
            filler = "all " if num_schemas==len(Defaults.CONVERSION_SCHEMAS) else ""
            filler += str(num_schemas)
            st.write(dedent(f"""
            Click the **Guess** button to guess the `TEXT` from the given `DNA` for {filler} schemas.
            """))
        with col2:
            guess = st.button("Guess")
        # Show guessed results
        if guess and options["convert_to"] == "TEXT":
            with st.expander("Click to see guesses 👇", expanded=False):
                _ = generate_guesses(X, options)

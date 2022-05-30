from typing import Dict, List, Optional, Tuple, Union

import annotated_text as AT
import streamlit as st
from composer import utils as U

Defaults = U.Defaults

DEFAULT_ANNOTATION_SCHEMA = {
    "A": dict(target="A", label="ADENINE", color="#8ef"),
    "C": dict(target="C", label="CYTOSINE", color="#fea"),
    "G": dict(target="G", label="GUANINE", color="#afa"),
    "T": dict(target="T", label="THYMINE", color="#faa"),
}

DEFAULT_ANNOTATION_LEGEND = dict(
    (k, tuple(v.get(x, "") for x in ["target", "label", "color"]))
    for k, v in DEFAULT_ANNOTATION_SCHEMA.items()
)

DEFAULT_ANNOTATION_MAP = dict(
    (k, tuple(v.get(x, "") for x in ["target", "UNKWNON", "color"]))
    for k, v in DEFAULT_ANNOTATION_SCHEMA.items()
)

AnnotationMapType = Optional[Dict[str, Tuple[str, str, str]]]


def _validate_annotation_map(annotation_map: AnnotationMapType = None):
    if annotation_map is None:
        annotation_map = DEFAULT_ANNOTATION_MAP.copy()  # type: ignore
    return annotation_map


def display_annotation_legend(annotation_map: AnnotationMapType = None):

    if annotation_map is None:
        annotation_map = DEFAULT_ANNOTATION_LEGEND.copy()  # type: ignore
    ## Displays something like this
    # AT.annotated_text(*[
    #     ("A", "ADENINE", "#8ef"),
    #     ("C", "CYTOSINE", "#fea"),
    #     ("G", "GUANINE", "#afa"),
    #     ("T", "THYMINE", "#faa"),
    # ])
    legends = ["DNA base-pair legends: "] + list(annotation_map.values())  # type: ignore
    AT.annotated_text(*legends)


def widthwrap(dna: str, wrap_length: int = 10):
    """Returns a dna wrapped after each ``wrap_length``
    number of base-pairs.
    """
    return "\n".join(
        [
            dna[i * wrap_length : (i + 1) * wrap_length]
            for i in range((len(dna) - 1) // wrap_length + 1)
        ]
    )


def annotate_dna(
    dna: str, wrap_length: Optional[int] = 10, annotation_map: AnnotationMapType = None
) -> List[Union[str, Tuple[str, str, str]]]:
    """Returns annotated DNA (as a list)."""
    annotation_map = _validate_annotation_map(annotation_map=annotation_map)
    if wrap_length is not None:
        dna = widthwrap(dna, wrap_length=wrap_length)
    annotated_dna = list(map(lambda x: annotation_map.get(x, x), list(dna)))  # type: ignore
    return annotated_dna  # type: ignore


def display_annotated_dna(
    options: Dict,
    dna: Optional[str] = None,
    show_balloons: bool = True,
    header: str = "Annotated DNA",
    show_annotated_dna: bool = True,
):
    """Displays annotated  dna"""

    with st.container():
        if options.get("show_balloons", show_balloons):
            st.balloons()
            # AT.annotated_text(*[
            #     ("A", "ADENINE", "#8ef"),
            #     ("C", "CYTOSINE", "#fea"),
            #     ("G", "GUANINE", "#afa"),
            #     ("T", "THYMINE", "#faa"),
            # ])
        st.warning(f"### {header} 🆎🧬✨")

        X = "ACGT"
        if dna is None:
            X = st.text_input("DNA Input  🧬👇", value=X)
        else:
            X = st.text_input("DNA Input  🧬👇", value=dna)
        if X and U.isDNAType(X):
            dna = X

        annotation_legend = DEFAULT_ANNOTATION_LEGEND

        if U.isDNAType(dna):  # type: ignore
            annots, annotation_legend = _prepare_annotated_dna(dna, options, dna_wrap_length=10)  # type: ignore

        col1, col2 = st.columns([5, 2])
        with col1:
            display_annotation_legend(annotation_map=annotation_legend)
        with col2:
            button_label = "Show Annotated DNA"
            if not options.get("show_annotated_dna", False):
                options["show_annotated_dna"] = st.button(button_label)

        st.write("\n\n")

        if options.get("show_annotated_dna", show_annotated_dna):
            AT.annotated_text(*annots)  # type: ignore
            st.write("\n\n")
            ## The following also works, but the rendered output messes up
            ## the font-formatting. Keeping it documented for future reference.
            #
            # html = AT.util.get_annotated_html(*annots)
            # st.components.v1.html(html, width=700, height=200, scrolling=True)


def _prepare_annotated_dna(dna: str, options: Dict, dna_wrap_length: int = 10):
    """Core logic for displaying annotated dna."""
    # update annotation-map
    annotation_map = _validate_annotation_map(
        annotation_map=options.get("annotation_map", None),
    )
    # update wrap_lenth for dna-annotation visualization
    wrap_length: int = options.get("dna_wrap_length", dna_wrap_length)
    # generate dna (base-pair) annotations
    annots = annotate_dna(
        dna,
        wrap_length=wrap_length,
        annotation_map=annotation_map,
    )
    # update annotation-legend
    annotation_legend = DEFAULT_ANNOTATION_LEGEND.copy()
    for k, v in annotation_legend.items():
        v = (v[0], v[1], annotation_map.get(k)[2])  # type: ignore
        annotation_legend.update({k: v})

    return annots, annotation_legend

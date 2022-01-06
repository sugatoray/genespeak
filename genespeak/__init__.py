from genespeak.core import dna_to_text, text_to_dna
from genespeak.converters import Converter, set_converter
from genespeak.dna_encoders import DNABaseEncoder
from genespeak.text_strategies import TextEncodingStrategies, set_strategy
from genespeak.utils import run_length_encode, run_length_decode

try:
    from importlib import metadata
except ImportError:  # for Python<3.8
    import importlib_metadata as metadata


__title__ = __name__
__version__ = metadata.version(__title__)  # type: ignore

__all__ = [
    # core
    "dna_to_text",
    "text_to_dna",
    # dna_encoders
    "DNABaseEncoder",
    # converters
    "Converter",
    "set_converter",
    # text_strategies
    "TextEncodingStrategies",
    "set_strategy",
    # utils
    "run_length_encode",
    "run_length_decode",
]

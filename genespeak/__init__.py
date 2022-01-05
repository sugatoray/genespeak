from genespeak.core import dna_to_text, text_to_dna
from genespeak.converter import DNABaseEncoder, Converter
from genespeak.text_strategies import TextEncodingStrategies

try:
    from importlib import metadata
except ImportError:  # for Python<3.8
    import importlib_metadata as metadata


__title__ = __name__
__version__ = metadata.version(__title__)

__all__ = [
    "dna_to_text",
    "text_to_dna",
    "DNABaseEncoder",
    "Converter",
    "TextEncodingStrategies",
]

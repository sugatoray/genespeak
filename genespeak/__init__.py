from genespeak.core import rna_to_text, text_to_rna
from genespeak.utils import RNABaseEncoder, Converter

try:
    from importlib import metadata
except ImportError:  # for Python<3.8
    import importlib_metadata as metadata


__title__ = __name__
__version__ = metadata.version(__title__)

__all__ = [
    "rna_to_text",
    "text_to_rna",
    "RNABaseEncoder",
    "Converter"
]
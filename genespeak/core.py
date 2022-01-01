from typing import Dict, List, Union, Optional
from genespeak.utils import ASCIIConverter


def text_to_dna(text: str, schema: str = "AGCT", binary_string_length: int = 8, converter: Optional[ASCIIConverter] = None) -> str:
    if (converter is None) or (not isinstance(converter, ASCIIConverter)):
        converter = ASCIIConverter(
            schema = schema,
            binary_string_length = binary_string_length,
        )
    text_ascii_bin8 = converter.convert_info_to_8bit_binary(text)
    dnabase_chr, dnabase_bin2 = converter.convert_to_dnabase(text_ascii_bin8)
    text_as_dnabase = ''.join(dnabase_chr)
    return text_as_dnabase

def dna_to_text(dna: str, schema: str = "AGCT", binary_string_length: int = 8, converter: Optional[ASCIIConverter] = None) -> str:
    if (converter is None) or (not isinstance(converter, ASCIIConverter)):
        converter = ASCIIConverter(
            schema = schema,
            binary_string_length = binary_string_length,
        )
    dnabase_as_bin = converter.encoder.chr2bin
    dnabase_as_bin2 = [dnabase_as_bin.get(x_chr) for x_chr in dna]
    dnabase_as_bin8 = converter.get_bin2_to_bin8(''.join(dnabase_as_bin2))
    num_digits = binary_string_length // len(converter.encoder.schema) # 8 // 4 = 2
    dnabase_as_chr = [chr(int(x, num_digits)) for x in dnabase_as_bin8]
    dnabase_as_text = ''.join(dnabase_as_chr)
    return dnabase_as_text

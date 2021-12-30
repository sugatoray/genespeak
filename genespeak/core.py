from typing import Dict, List, Union, Optional
from utils import Converter

def text_to_rna(text: str, schema: str="AGCT", binary_string_length: int=8, converter=None) -> str:
    if (converter is None) or (not isinstance(converter, Converter)):
        converter = Converter(
            schema = schema, 
            binary_string_length = binary_string_length,
        )
    text_ascii_bin8 = converter.convert_info_to_8bit_binary(text)
    rnabase_chr, rnabase_bin2 = converter.convert_to_rnabase(text_ascii_bin8)
    text_as_rnabase = ''.join(rnabase_chr)
    return text_as_rnabase

def rna_to_text(rna: str, schema: str="AGCT", binary_string_length: int=8, converter=None) -> str:
    if (converter is None) or (not isinstance(converter, Converter)):
        converter = Converter(
            schema = schema, 
            binary_string_length = binary_string_length,
        )
    rnabase_as_bin = converter.encoder.chr2bin
    rnabase_as_bin2 = [rnabase_as_bin.get(x_chr) for x_chr in rna]
    rnabase_as_bin8 = converter.get_bin2_to_bin8(''.join(rnabase_as_bin2))
    num_digits = binary_string_length // len(converter.encoder.schema) # 8 // 4 = 2
    rnabase_as_chr = [chr(int(x, num_digits)) for x in rnabase_as_bin8]
    rnabase_as_text = ''.join(rnabase_as_chr)
    return rnabase_as_text

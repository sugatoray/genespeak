from typing import Dict, List, Union, Optional
from genespeak.converter import Converter, set_converter


def text_to_dna(text: str, schema: str = "AGCT", binary_string_length: int = 8, strategy: str="ascii", converter: Optional[Converter] = None) -> str:
    if (converter is None) or (not isinstance(converter, Converter)):
        converter = Converter(
            schema = schema,
            binary_string_length = binary_string_length,
            strategy = strategy,
        )
    dnabase_chr: List[str] = []
    text_encoded_bin2N = converter.convert_info_to_2Nbit_binary(text, length2N=converter.strategy.binary_string_length)
    dnabase_chr, _ = converter.convert_to_dnabase(text_encoded_bin2N, strategy=converter.strategy.name)
    text_as_dnabase = ''.join(dnabase_chr)
    return text_as_dnabase


def dna_to_text(dna: str, schema: str = "AGCT", binary_string_length: int = 8, strategy: str = "ascii", converter: Optional[Converter] = None) -> str:
    converter = set_converter(
        schema = schema,
        binary_string_length = binary_string_length,
        strategy = strategy,
        converter = converter,
    )

    dnabase_as_bin = converter.encoder.chr2bin
    dnabase_as_bin2 = [dnabase_as_bin.get(x_chr) for x_chr in dna]
    length2N = converter.strategy.binary_string_length
    dnabase_as_bin2N = converter.get_bin2_to_bin2N(''.join(dnabase_as_bin2), length2N=length2N)
    # num_digits = 2 # length of any('00', '01', '10', '11')
    # binary to decimal conversion: int(x, 2)
    dnabase_as_chr = [chr(int(x, 2)) for x in dnabase_as_bin2N]
    dnabase_as_text = ''.join(dnabase_as_chr)
    return dnabase_as_text

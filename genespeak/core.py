from typing import Dict, List, Union, Optional
from genespeak.converters import Converter, set_converter


def text_to_dna(text: str,
                schema: str = "AGCT",
                binary_string_length: int = 8,
                strategy: str="ascii",
                converter: Optional[Converter] = None,
    ) -> str:
    """Encodes text string into DNA string with dna-bases (``A``, ``C``, ``G``, ``T``).

    Arguments:
        text: a string
        schema: the conversion schema to use (default: ``AGCT``)
        binary_string_length: the length of the binary-string during conversion
                              (use ``8`` for ``strategy='ascii'`` and ``24`` for ``strategy='utf-8'``)
        strategy: the text-encoding/decoding strategy to use (default: ``ascii``)
                  (options: ``ascii``, ``utf-8``)
        converter: optionally you can provide a converter (``genespeak.converter.Converter``)
    """

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


def dna_to_text(dna: str,
                schema: str = "AGCT",
                binary_string_length: int = 8,
                strategy: str = "ascii",
                converter: Optional[Converter] = None,
    ) -> str:
    """Decodes valid encoded DNA string back into the equivalent text string.

    Arguments:
        dna: a string of dna-base
        schema: the conversion schema to use (default: ``AGCT``)
        binary_string_length: the length of the binary-string during conversion
                              (use ``8`` for ``strategy='ascii'`` and ``24`` for ``strategy='utf-8'``)
        strategy: the text-encoding/decoding strategy to use (default: ``ascii``)
                  (options: ``ascii``, ``utf-8``)
        converter: optionally you can provide a converter (``genespeak.converter.Converter``)
    """

    converter = set_converter(
        schema = schema,
        binary_string_length = binary_string_length,
        strategy = strategy,
        converter = converter,
    )

    dnabase_as_bin = converter.encoder.chr2bin
    dnabase_as_bin2 = [dnabase_as_bin.get(x_chr) for x_chr in dna]
    length2N = converter.strategy.binary_string_length
    dnabase_as_bin2N = converter.get_bin2_to_bin2N(''.join(dnabase_as_bin2), length2N=length2N)  # type: ignore
    # num_digits = 2 # length of any('00', '01', '10', '11')
    # binary to decimal conversion: int(x, 2)
    dnabase_as_chr = [chr(int(x, 2)) for x in dnabase_as_bin2N]
    dnabase_as_text = ''.join(dnabase_as_chr)
    return dnabase_as_text

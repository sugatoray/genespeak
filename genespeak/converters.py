from typing import Dict, List, Tuple, Union, Optional
from genespeak.text_strategies import AVAILABLE_STRATEGY_NAMES, TextEncodingStrategies, set_strategy
from genespeak.dna_encoders import DNABaseEncoder

class Converter(object):
    # The Converter API will enforce the use of text-encoding strategy names
    # with hyphens when applicable:
    #   - example: "utf-8" instead of "utf8".
    # This makes sure of conveying that to the users.
    strategy_names = [s.replace("utf", "utf-") for s in AVAILABLE_STRATEGY_NAMES]
    strategies = TextEncodingStrategies()
    encoder: DNABaseEncoder

    def __init__(self, schema: str = "AGCT", binary_string_length: int = 8, strategy: str = "ascii"):
        self.encoder = DNABaseEncoder(
            schema=schema,
            binary_string_length=binary_string_length
        )
        self.strategy = self.get_strategy(strategy_name=strategy)

    def __repr__(self):
        kwargs = dict(
            schema=self.encoder.schema,
            binary_string_length=self.encoder.binary_string_length,
            strategy=self.strategy.name,
        )
        kwargs_string = ', '.join([f'{k}={v}' for k, v in kwargs.items()])
        classname = self.__class__.__name__
        template = '{classname}({kwargs_string})'
        return f'{classname}({kwargs_string})'

    def get_encoded_text(self, text: str) -> List[int]:
        """Encodes each character of the text and returns a list.

        The encoding strategy is picked from the ``Converter.strategy``.
        """
        text = str(text)
        encoded_chr_list = [ord(x) for x in text]
        return encoded_chr_list

    def get_decoded_text(self, encoded_chr_list: List[int], as_list: bool = False) -> Union[List[str], str]:
        """Decodes each character from an encoded-character-list (``encoded_chr_list``) and
        returns a either a string (if ``as_list = False``) or
        a list of decoded strings (if ``as_list = True``).

        The encoding/decoding strategy is picked from the ``Converter.strategy``.
        """

        if not(as_list):
            text = ''.join(chr(x) for x in encoded_chr_list)
        else:
            text = [chr(x) for x in encoded_chr_list]

        return text

    def dec_to_bin(self, decimal_numbers: List[int]) -> List[int]:
        """Returns a list of binary numbers for a given list of
        POSITIVE decimal integers.
        """
        return [int(bin(x)[2:]) for x in decimal_numbers]

    def convert_info_to_2Nbit_binary(self, text: str, length2N: int = 8) -> List[str]:
        # convert to list of ascii / encoded-characters
        text_encoded_chr = self.get_encoded_text(text)
        # convert to binary list of int
        text_encoded_bin = self.dec_to_bin(text_encoded_chr)
        # convert to list of binary-2N-bit str (just 2N digits: 0 or 1)
        text_encoded_bin_2Nbit = [str(x).zfill(length2N) for x in text_encoded_bin]

        return text_encoded_bin_2Nbit

    def get_bin2N_to_bin2(self, str_bin2N: str) -> List[str]:
        str_bin2_list = self.split_text(str_bin2N, length=2)
        return str_bin2_list

    def get_bin2_to_bin2N(self, str_bin2: str, length2N: int = 8) -> List[str]:
        str_bin2N_list = self.split_text(str_bin2, length=length2N)
        return str_bin2N_list

    def split_text(self, text: str, length=4) -> List[str]:
        split_text_list = list(map(''.join, zip(*[iter(text)] * length)))
        return split_text_list

    def convert_to_dnabase(self, bin_str_list: List[str], strategy: Optional[str] = None) -> Tuple[List[str], List[str]]:
        # A list of two-character binary strings
        dnabase_bin2: List[str] = []

        # Determine text-encoding-strategy
        if strategy is None:
            strategy = self.get_strategy(strategy_name=strategy)  # type: ignore
        else:
            strategy = self.strategy

        for x_bin2N in bin_str_list:
            dnabase_bin2 += self.get_bin2N_to_bin2(x_bin2N)
        dnabase_chr = [self.encoder.bin2chr.get(x_bin2) for x_bin2 in dnabase_bin2]
        return (dnabase_chr, dnabase_bin2)  # type: ignore

    def get_strategy(self, strategy_name: str = "ascii"):
        """Returns strategy based on name."""
        return set_strategy(strategy_name=strategy_name)


def set_converter(
    schema: str = "AGCT",
    binary_string_length: int = 8,
    strategy: str = "ascii",
    converter: Optional[Converter] = None
) -> Converter:
    """Creates a ``Converter`` if no ``Converter`` is provided."""

    if (converter is None) or (not isinstance(converter, Converter)):
        converter = Converter(
            schema=schema,
            binary_string_length=binary_string_length,
            strategy=strategy,
        )

    return converter

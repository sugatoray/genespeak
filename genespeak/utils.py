from typing import Dict, List, Tuple, Union, Optional
from abc import ABC, abstractmethod

# Define Dictionaries and Functions for DNA/Text Conversion
DEFAULT_SCHEMA = "AGCT"
DNABASE_AS_CHR = dict({'00':'A', '01':'G', '10':'C', '11':'T'})
DNABASE_AS_BIN = dict({'A':'00', 'G':'01', 'C':'10', 'T':'11'})

def dec2bin(x: int, n: int=2) -> str:
    """Converts a single decimal integer to it binary representation
    and returns as string for length >= n.
    """
    return str(int(bin(x)[2:])).zfill(n)

class DNABaseEncoder(object):
    dnabase_as_bin: Dict[str, str] = DNABASE_AS_BIN.copy()
    dnabase_as_chr: Dict[str, str] = DNABASE_AS_CHR.copy()

    def __init__(self, schema: str="AGCT", binary_string_length: int=8):
        conds = [
            len(schema) != 4,
            set(schema) != set(DEFAULT_SCHEMA),
        ]
        self.schema = DEFAULT_SCHEMA if any(conds) else schema
        self.dnabase_as_bin = self.chr2bin.copy()
        self.dnabase_as_chr = self.bin2chr.copy()

    @property
    def bin2chr(self) -> Dict[str, str]:
        return dict((dec2bin(i), base) for i, base in enumerate(self.schema))

    @property
    def chr2bin(self) -> Dict[str, str]:
        return dict((base, dec2bin(i)) for i, base in enumerate(self.schema))


class Converter(ABC): pass

class ASCIIConverter(Converter):
    encoder: DNABaseEncoder

    def __init__(self, schema: str="AGCT", binary_string_length: int=8):
        self.encoder = DNABaseEncoder(
            schema=schema,
            binary_string_length=binary_string_length
        )


    def get_text_to_ascii(self, text: str) -> List[int]:
        text = str(text)
        ascii_list = [ord(x) for x in text]
        return ascii_list

    def get_ascii_to_text(self, ascii_list: List[int], as_list: bool = False) -> Union[List[str], str]:

        if not(as_list):
            text = ''.join(chr(x) for x in ascii_list)
        else:
            text = [chr(x) for x in ascii_list]

        return text

    def dec_to_bin(self, decimal_numbers: List[int]) -> List[int]:
        return [int(bin(x)[2:]) for x in decimal_numbers]

    def convert_info_to_8bit_binary(self, text: str) -> List[str]:
        # convert to list of ascii
        text_ascii = self.get_text_to_ascii(text)
        # convert to binary list of int
        text_ascii_bin = self.dec_to_bin(text_ascii)
        # convert to list of binary-8bit str (just 8 bigits: 0 or 1)
        text_ascii_bin_8bit = [str(x).zfill(8) for x in text_ascii_bin]

        return text_ascii_bin_8bit

    def get_bin8_to_bin2(self, str_bin8: str) -> List[str]:
        str_bin2_list = self.split_text(str_bin8, length = 2)
        return str_bin2_list

    def get_bin2_to_bin8(self, str_bin2: str) -> List[str]:
        str_bin8_list = self.split_text(str_bin2, length = 8)
        return str_bin8_list

    def split_text(self, text: str, length = 4) -> List[str]:
        split_text_list = list(map(''.join, zip(*[iter(text)]*length)))
        return split_text_list

    def convert_to_dnabase(self, bin_str_list: List[str]) -> Tuple[List[str], List[str]]:
        dnabase_bin2: List[str] = []
        for x_bin8 in bin_str_list:
            dnabase_bin2 += self.get_bin8_to_bin2(x_bin8)
        dnabase_chr = [self.encoder.bin2chr.get(x_bin2) for x_bin2 in dnabase_bin2]
        return (dnabase_chr, dnabase_bin2)

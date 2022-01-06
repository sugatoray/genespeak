from typing import Dict


# Define Dictionaries and Functions for DNA/Text Conversion
DEFAULT_SCHEMA = "ACGT"
DNABASE_AS_CHR = dict({'00': 'A', '01': 'C', '10': 'G', '11': 'T'})
DNABASE_AS_BIN = dict({'A': '00', 'C': '01', 'G': '10', 'T': '11'})


def dec2bin(x: int, n: int = 2) -> str:
    """Converts a single decimal integer to it binary representation
    and returns as string for length >= n.
    """
    return str(int(bin(x)[2:])).zfill(n)


class DNABaseEncoder(object):
    """A BaseEncoder class for DNA.

    Arguments:
        dnabase_as_bin: dnabase with char:binary mapping
        dnabase_as_chr: dnabase with binary:char mapping
        schema: the dnabase-schema (default: "ACGT")
        binary_string_length: the binary-string length to use (example: `01` --> `00000001`)

    Usage:

    ```python
    from genespeak.utils import DNABaseEncoder
    encoder = DNABaseEncoder(schema="ACGT")
    print(encoder.dnabase_as_chr) # {'00':'A', '01':'C', '10':'G', '11':'T'}
    print(encoder.dnabase_as_bin) # {'A':'00', 'C':'01', 'G':'10', 'T':'11'}
    ```

    There are a total of 24 (`4 x 3 x 2 x 1 = 4!`) possible schemas:
    `ACGT`, `ACTG`, `AGCT`, `AGTC`, `ATGC`, `ATCG`, `GACT`, `GCAT`, `GCTA`, `AGCT`, etc.
    """
    dnabase_as_bin: Dict[str, str] = DNABASE_AS_BIN.copy()
    dnabase_as_chr: Dict[str, str] = DNABASE_AS_CHR.copy()

    def __init__(self, schema: str = "AGCT", binary_string_length: int = 8):
        conds = [
            len(schema) != 4,
            set(schema) != set(DEFAULT_SCHEMA),
        ]
        self.schema = DEFAULT_SCHEMA if any(conds) else schema
        self.binary_string_length = binary_string_length
        self.dnabase_as_bin = self.chr2bin.copy()  # type: ignore
        self.dnabase_as_chr = self.bin2chr.copy()  # type: ignore

    @property
    def bin2chr(self) -> Dict[str, str]:
        return dict((dec2bin(i), base) for i, base in enumerate(self.schema))

    @property
    def chr2bin(self) -> Dict[str, str]:
        return dict((base, dec2bin(i)) for i, base in enumerate(self.schema))

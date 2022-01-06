# cspell: disable

from typing import Union, List, Tuple
import re


_PAT_RLE_DECODE = r"((\d+)(\w))"
_PAT_RLE_DECODE = re.compile(_PAT_RLE_DECODE)

_PAT_RLE_ENCODE = r"((A*)(C*)(G*)(T*))"
_PAT_RLE_ENCODE = re.compile(_PAT_RLE_ENCODE)


def run_length_encode(dna: str) -> str:
    """Return the run length encoding of a string

    Usage:

    ```python
    dna = "A"*3 + "G"*2 + "C" + "T"*5 + "A"*6 + "GCCT"
    dna_rle = run_length_encode(dna)
    ```

    """

    return _run_length_encode(dna, use_regex=True, return_list=False)  # type: ignore

def _run_length_encode(dna: str, use_regex: bool = True, return_list: bool = False) -> Union[str, List[Tuple[str, int]]]:
    """Return the run length encoding of a string

    Usage:

    ```python
    dna = "A"*3 + "G"*2 + "C" + "T"*5 + "A"*6 + "GCCT"
    dna_rle = run_length_encode(dna)
    ```

    """
    if use_regex:
        return regex_dna_rle(dna, return_list=return_list)
    else:
        return noregex_dna_rle(dna, return_list=return_list)

def noregex_dna_rle(dna: str, return_list: bool = False) -> Union[str, List[Tuple[str, int]]]:

    counter = []
    temp_counter = []
    for i, e in enumerate(dna):
        if i == 0:
            temp_counter = [e, 1]
        else:
            if e == dna[i - 1]:
                temp_counter[1] += 1
            else:
                counter.append(tuple(temp_counter.copy()))
                if i <= len(dna) - 1:
                    temp_counter = [e, 1]
            if i == len(dna) - 1:
                counter.append(tuple(temp_counter.copy()))

    if not return_list:
        dna_rle = ''.join([f'{c[1]}{c[0]}' for c in counter])
        return dna_rle
    else:
        return counter


def regex_dna_rle(dna: str, return_list: bool = False) -> Union[str, List[Tuple[str, int]]]:
    pat = _PAT_RLE_ENCODE
    if return_list:
        dna_rle = []
    else:
        dna_rle = ''
    for v in pat.findall(dna):
        groups = v[1:]
        for g in groups:
            if g:
                if return_list:
                    dna_rle.append(tuple([g[0], len(g)]))  # type: ignore
                else:
                    dna_rle += f"{len(g)}{g[0]}"
    if return_list:
        dna_rle = ''.join([f'{c[1]}{c[0]}' for c in dna_rle])

    return dna_rle


def run_length_decode(dna_rle: str) -> str:
    pat = _PAT_RLE_DECODE
    return ''.join([c * int(n) for _, n, c in pat.findall(dna_rle)])




import re

def run_length_encode(dna: str) -> str:
    """Return the run length encoding of s string

    Usage:

    ```python
    dna = "A"*3 + "G"*2 + "C" + "T"*5 + "A"*6 + "GCCT"
    dna_rle = run_length_encode(dna)
    ```

    """
    counter = []
    temp_counter = []
    # print(len(dna))
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

        ## print(i, counter)

    dna_rle = ''.join([f'{c[1]}{c[0]}' for c in counter])

    return dna_rle


def run_length_decode(dna_rle: str) -> str:
    pat = r"((\d+)(\w))"
    pat = re.compile(pat)
    return ''.join([c * int(n) for g, n, c in pat.findall(dna_rle)])

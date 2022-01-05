# **GeneSpeak**

A library to encode text as DNA and decode DNA to text.

GeneSpeak allows you to encode regular text as DNA using the bases
(`A`, `T`, `G`, `C`) and convert back to text. The coding scheme could
be any combination of `A`, `T`, `G`, `C`.

A DNA molucule consists of a double-helix, where each strand is composed
of a series of bases from the following four types:

- Adenine (**A**)
- Cytosine (**C**)
- Guanine (**G**)
- Thymine (**T**)

Adenine pairs with thymine, and cytosine pairs with guanine.

- <kbd>A</kbd> -- <kbd>T</kbd>
- <kbd>C</kbd> -- <kbd>G</kbd>

| ![dna-molecule](https://www.genome.gov/sites/default/files/tg/en/illustration/acgt.jpg) |
|:---:|
| Source: <https://www.genome.gov/genetics-glossary/acgt> |

## Installation

You can install the library via `pip` or `conda`.

**Install with pip**

```
python -m pip install genespeak
```

**Install with conda**

```
conda install -c conda-forge genespeak
```

## **Example**

```python
import genespeak as gp
print(f'{gp.__name__} version: {gp.__version__}')

schema = "ATCG" # (1)
text = "Hello World!"
dna = gp.text_to_dna(text, schema=schema)
text_from_dna = gp.dna_to_text(dna, schema=schema)
print(f'Text: {text}\nEncoded DNA: {dna}\nDecoded Text: {text_from_dna}\n')
```

1. This is an annotation.

**Output**

```sh
genespeak version: 0.0.3

Text: Hello World!
Encoded DNA: TACATCTTTCGATCGATCGGACAATTTGTCGGTGACTCGATCTAACAT
Decoded Text: Hello World!
```

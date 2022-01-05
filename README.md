# GeneSpeak

<!--- BADGES: START --->
[![GitHub - License](https://img.shields.io/github/license/sugatoray/genespeak?logo=github&style=flat&color=green)][#github-license]
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/genespeak?logo=pypi&style=flat&color=blue)][#pypi-package]
[![PyPI - Package Version](https://img.shields.io/pypi/v/genespeak?logo=pypi&style=flat&color=orange)][#pypi-package]
[![Conda - Platform](https://img.shields.io/conda/pn/conda-forge/genespeak?logo=anaconda&style=flat)][#conda-forge-package]
[![Conda (channel only)](https://img.shields.io/conda/vn/conda-forge/genespeak?logo=anaconda&style=flat&color=orange)][#conda-forge-package]
[![Docs - GitHub.io](https://img.shields.io/static/v1?logo=github&style=flat&color=pink&label=docs&message=genespeak)][#docs-package]

[#github-license]: https://github.com/sugatoray/genespeak/blob/main/LICENSE
[#pypi-package]: https://pypi.org/project/genespeak/
[#conda-forge-package]: https://anaconda.org/conda-forge/genespeak
[#docs-package]: https://koaning.github.io/genespeak/
<!--- BADGES: END --->

A library to encode text as DNA and decode DNA to text.

GeneSpeak allows you to encode regular text as DNA using base-pairs (`A`, `T`, `G`, `C`) and convert back to text. The coding scheme could be any combination of `A`, `T`, `G`, `C`.

## Example

```python
import genespeak as gp
print(f'{gp.__name__} version: {gp.__version__}')

schema = "ATCG"
text = "Hello World!"
dna = gp.text_to_dna(text, schema=schema)
print(f'Text: {text}\nEncoded DNA: {dna}\n')
text_from_dna = gp.dna_to_text(dna, schema=schema)
print(f'Text: {text}\nEncoded DNA: {dna}\nDecoded Text: {text_from_dna}\n')
```

**Output**

```sh
genespeak version: 0.0.3
Text: Hello World!
Encoded DNA: TACATCTTTCGATCGATCGGACAATTTGTCGGTGACTCGATCTAACAT

Text: Hello World!
Encoded DNA: TACATCTTTCGATCGATCGGACAATTTGTCGGTGACTCGATCTAACAT
Decoded Text: Hello World!
```

# GeneSpeak

![genespeak-banner][#repo-banner]

[#repo-banner]: docs/assets/images/genespeak_banner_01.png

<!--- BADGES: START --->
[![GitHub - License](https://img.shields.io/github/license/sugatoray/genespeak?logo=github&style=flat&color=green)][#github-license]
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/genespeak?logo=pypi&style=flat&color=blue)][#pypi-package]
[![PyPI - Package Version](https://img.shields.io/pypi/v/genespeak?logo=pypi&style=flat&color=orange)][#pypi-package]
[![Conda - Platform](https://img.shields.io/conda/pn/conda-forge/genespeak?logo=anaconda&style=flat)][#conda-forge-package]
[![Conda (channel only)](https://img.shields.io/conda/vn/conda-forge/genespeak?logo=anaconda&style=flat&color=orange)][#conda-forge-package]
[![Docs - GitHub.io](https://img.shields.io/static/v1?logo=github&style=flat&color=pink&label=docs&message=genespeak)][#docs-package]

[#github-license]: https://github.com/sugatoray/genespeak/blob/master/LICENSE
[#pypi-package]: https://pypi.org/project/genespeak/
[#conda-forge-package]: https://anaconda.org/conda-forge/genespeak
[#docs-package]: https://sugatoray.github.io/genespeak/
<!--- BADGES: END --->

A library to encode text as DNA and decode DNA to text.

GeneSpeak allows you to encode regular text as DNA using
base-pairs (`A`, `T`, `G`, `C`) and convert back to the
original text. Text encoding is done for both `ascii` and
`utf-8` characters based on the `strategy` keyword argument.
The encoding scheme could be any combination of `A`, `T`, `G`, `C`.

## Installation

You can install the library via `pip` or `conda`.

**Install with pip**

```sh
pip install genespeak
```

**Install with conda**

```sh
conda install -c conda-forge genespeak
```

## Quickstart

See the quickstart guide here.

| Service | Link/Badge |
|:---:|:---:|
| Colab | [![Colab Badge](https://colab.research.google.com/assets/colab-badge.svg)][gh-colab-quickstart] |
| Binder | [![Binder](https://mybinder.org/badge_logo.svg)][gh-binder-quickstart] |

[gh-colab-quickstart]: https://colab.research.google.com/github/sugatoray/genespeak/blob/master/notebooks/quickstart_genespeak.ipynb

[gh-binder-quickstart]: https://mybinder.org/v2/gh/sugatoray/genespeak/master?labpath=notebooks%2Fquickstart_genespeak.ipynb

## Usage

```python
import genespeak as gp
print(f'{gp.__name__} version: {gp.__version__}')

schema = "ATCG" # (1)
strategy = "ascii" # (2)
text = "Hello World!"

dna = gp.text_to_dna(text, schema=schema)
text_from_dna = gp.dna_to_text(dna, schema=schema)
print(f'Text: {text}\nEncoded DNA: {dna}\nDecoded Text: {text_from_dna}\nSuccess: {text == text_from_dna}')
```

**Output**

```sh
genespeak version: 0.0.5
Text: Hello World!
Encoded DNA: TACATCTTTCGATCGATCGGACAATTTGTCGGTGACTCGATCTAACAT

Text: Hello World!
Encoded DNA: TACATCTTTCGATCGATCGGACAATTTGTCGGTGACTCGATCTAACAT
Decoded Text: Hello World!
```

## Documentation

[![Docs - GitHub.io](https://img.shields.io/static/v1?logo=github&style=flat&color=pink&label=docs&message=genespeak)][#docs-package]

The `genespeak` docs are maintained [here][#docs-package].

## License

[![GitHub - License](https://img.shields.io/github/license/sugatoray/genespeak?logo=github&style=flat&color=green)][#github-license]

The library is available under [MIT license][#github-license].

## Citation

You may cite this library as follows.

```bibtex
@software{ray2022genespeak,
    author = {Ray, Sugato},
    title = {{genespeak} - A library to encode text as DNA and decode DNA to text},
    url = {https://github.com/sugatoray/genespeak}
}
```

## GeneSpeak Thumb Print 👍

Let's have some fun! ✨ The following is a ***GeneSpeak thumbprint*** of `genespeak` itself.

| **schema** | **strategy** | **thumbprint** |
|:---:|:---:|:---|
| `ATCG` | `ascii` | `TCTGTCTTTCGCTCTTTGAGTGAATCTTTCATTCCG` |

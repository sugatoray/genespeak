# GeneSpeak

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

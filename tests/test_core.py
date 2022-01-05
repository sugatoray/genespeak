

def test_reconstruction():
    from genespeak import text_to_dna, dna_to_text

    texts = {
        "ascii": "A good life",
        "utf-8": "A good life 鸞!..."
    }

    schemas = ["ACGT", "GATC", "ATGC", ]

    for schema in schemas:
        for strategy, text in texts.items():
            dna = text_to_dna(text, schema=schema, strategy=strategy)
            rcon_text = dna_to_text(dna, schema=schema, strategy=strategy)
            print(f'\n\nschema: {schema} | strategy: {strategy} \n\ttext: {text} \n\tdna: {dna} \n\trecovered-text: {rcon_text} \n\tsuccess: {text == rcon_text} \n\n' + '-' * 60)


if __name__ == "__main__":

    test_reconstruction()

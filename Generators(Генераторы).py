def all_variants (text):
    for i in range(len(text) + 1):
        for j in range(i + 1):
            yield text[j:i]

text = "Функция-генератор"
generator = all_variants(text)
for variant in generator:
    print(variant)
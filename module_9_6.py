def all_variants(text: str):
    res = set()

    for len_sym in range(1, len(text) + 1):
        for i in range(len(text)):
            for j in range(i + 1, len(text) + 1):
                if len(text[i:j]) == len_sym:
                    res.add(text[i:j])
                    yield text[i:j]

    return res


a = all_variants("abc")
for i in a:
    print(i, end = ' ')

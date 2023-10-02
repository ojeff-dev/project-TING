def exists_word(word, instance):
    lower_word = word.lower()
    data = []

    for i in range(instance.__len__()):
        file = instance.search(i)

        words = file["linhas_do_arquivo"]
        occurrences = []

        for index, w in enumerate(words):
            if lower_word in w.lower():
                occurrences.append({"linha": index + 1})

        if occurrences:
            data.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })

    return data


def search_by_word(word, instance):
    lower_word = word.lower()
    data = []

    for i in range(instance.__len__()):
        file = instance.search(i)

        words = file["linhas_do_arquivo"]
        occurrences = []

        for index, w in enumerate(words):
            if lower_word in w.lower():
                occurrences.append({"linha": index + 1, "conteudo": w})

        if occurrences:
            data.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })

    return data

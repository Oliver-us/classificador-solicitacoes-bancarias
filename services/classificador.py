import re

import pandas as pd
import spacy


# Modelo básico em português.
# Não precisamos baixar um modelo grande para este projeto.
nlp = spacy.blank("pt")


# Base de palavras-chave
dados_palavras = [
    {
        "categoria": "Bloqueio de cartão",
        "palavras": [
            "bloquear",
            "bloqueio",
            "cartão",
            "perdi",
            "perdido",
            "perdida",
            "roubo",
            "roubado",
            "roubada"
        ]
    },
    {
        "categoria": "Segunda via de boleto",
        "palavras": [
            "boleto",
            "segunda",
            "via",
            "pagamento",
            "vencimento",
            "vencido",
            "vencida"
        ]
    },
    {
        "categoria": "Limite do cartão",
        "palavras": [
            "limite",
            "aumentar",
            "aumento",
            "reduzir",
            "redução",
            "crédito"
        ]
    },
    {
        "categoria": "Pix",
        "palavras": [
            "pix",
            "transferência",
            "transferir",
            "chave",
            "pix"
        ]
    },
    {
        "categoria": "Conta",
        "palavras": [
            "conta",
            "cadastro",
            "cadastrar",
            "senha",
            "acesso",
            "entrar",
            "login"
        ]
    }
]


def normalizar_texto(texto):

    texto = texto.lower()

    texto = re.sub(
        r"[^\w\s]",
        " ",
        texto,
        flags=re.UNICODE
    )

    return texto


def classificar_texto(texto):

    texto_normalizado = normalizar_texto(texto)

    doc = nlp(texto_normalizado)

    tokens = set(
        token.text
        for token in doc
        if not token.is_space
    )

    resultados = []

    for item in dados_palavras:

        palavras_encontradas = []

        for palavra in item["palavras"]:

            if palavra.lower() in tokens:

                palavras_encontradas.append(palavra)

        quantidade = len(palavras_encontradas)

        resultados.append(
            {
                "categoria": item["categoria"],
                "quantidade": quantidade,
                "palavras": palavras_encontradas
            }
        )


    # DataFrame utilizado para organizar
    # e comparar os resultados.
    df = pd.DataFrame(resultados)


    if df.empty or df["quantidade"].max() == 0:

        return {
            "categoria": "Não identificada",
            "confianca": 0.0,
            "palavras": []
        }


    maior_quantidade = df["quantidade"].max()

    candidatos = df[
        df["quantidade"] == maior_quantidade
    ]


    # Em caso de empate, mantém a primeira categoria.
    melhor = candidatos.iloc[0]


    total_palavras = len(
        dados_palavras[
            next(
                i
                for i, item in enumerate(dados_palavras)
                if item["categoria"] == melhor["categoria"]
            )
        ]["palavras"]
    )


    confianca = (
        maior_quantidade / total_palavras
    )


    return {
        "categoria": melhor["categoria"],
        "confianca": round(confianca, 2),
        "palavras": melhor["palavras"]
    }
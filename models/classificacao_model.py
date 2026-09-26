from database.banco import conectar


def salvar_classificacao(texto, categoria, confianca):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO solicitacoes
        (texto, categoria, confianca)
        VALUES (?, ?, ?)
        """,
        (
            texto,
            categoria,
            confianca
        )
    )

    conexao.commit()

    conexao.close()


def listar_classificacoes():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT
            id,
            texto,
            categoria,
            confianca,
            data_criacao
        FROM solicitacoes
        ORDER BY id DESC
        LIMIT 10
        """
    )

    resultados = cursor.fetchall()

    conexao.close()

    return resultados
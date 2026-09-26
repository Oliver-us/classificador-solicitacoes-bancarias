import sqlite3
import os


CAMINHO_BANCO = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "banco.db"
)


def conectar():

    os.makedirs(
        os.path.dirname(CAMINHO_BANCO),
        exist_ok=True
    )

    conexao = sqlite3.connect(CAMINHO_BANCO)

    return conexao


def inicializar_banco():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS solicitacoes (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            texto TEXT NOT NULL,

            categoria TEXT NOT NULL,

            confianca REAL NOT NULL,

            data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP

        )
        """
    )

    conexao.commit()

    conexao.close()
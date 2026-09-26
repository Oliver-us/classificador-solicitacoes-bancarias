from flask import Blueprint, render_template, request

from services.classificador import classificar_texto
from models.classificacao_model import salvar_classificacao, listar_classificacoes


classificacao_bp = Blueprint(
    "classificacao",
    __name__
)


@classificacao_bp.route("/", methods=["GET", "POST"])
def index():

    resultado = None
    historico = listar_classificacoes()

    if request.method == "POST":

        texto = request.form.get("texto", "").strip()

        if texto:

            resultado = classificar_texto(texto)

            salvar_classificacao(
                texto=texto,
                categoria=resultado["categoria"],
                confianca=resultado["confianca"]
            )

            historico = listar_classificacoes()

    return render_template(
        "index.html",
        resultado=resultado,
        historico=historico
    )
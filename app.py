from flask import Flask

from controllers.classificacao_controller import classificacao_bp
from database.banco import inicializar_banco


app = Flask(__name__)

# Inicializa o banco de dados
inicializar_banco()

# Registra as rotas do controller
app.register_blueprint(classificacao_bp)


if __name__ == "__main__":
    app.run(debug=True)
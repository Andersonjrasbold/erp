from flask import Blueprint, render_template

produtos_blueprint = Blueprint('produtos', __name__, template_folder='templates')

# Rota sem parâmetro
@produtos_blueprint.route("/produtos")
def cadastrar_produtos():
    return render_template('produtos.html')

# Rota com parâmetro
@produtos_blueprint.route("/produtos/<int:produto_id>")
def cadastrar_produto_id(produto_id):
    # Aqui você poderia buscar o produto no banco, por exemplo
    return render_template('produtos.html', produto_id=produto_id)
from flask import Flask, render_template, blueprints
from produtos.produtos import produtos_blueprint


app = Flask(__name__)

app.register_blueprint(produtos_blueprint)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



if __name__ == "__main__":
    app.run(debug=True)

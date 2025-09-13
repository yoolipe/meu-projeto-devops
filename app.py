from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Aplicação rodando no Docker!"

if __name__ == "__main__":
    # Importante: host 0.0.0.0 para ser acessível de fora do container
    app.run(host="0.0.0.0", port=5000)

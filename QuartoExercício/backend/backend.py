from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite requisições do Vue.js

# Carregar o CSV na memória (substitua pelo caminho correto)
CSV_PATH = "Relatorio_cadop.csv"
df = pd.read_csv(CSV_PATH, delimiter=';', encoding='latin1')

# Normalizar colunas para evitar problemas com espaços extras
df.columns = df.columns.str.strip()

@app.route("/buscar_operadora", methods=["GET"])
def buscar_operadora():
    query = request.args.get("q", "").strip().lower()
    if not query:
        return jsonify({"erro": "Parâmetro de busca não fornecido"}), 400
    
    # Filtrar por nome ou CNPJ
    resultado = df[
        df["Nome_Fantasia"].str.lower().str.contains(query, na=False) |
        df["CNPJ"].astype(str).str.contains(query)
    ]
    
    return jsonify(resultado.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)

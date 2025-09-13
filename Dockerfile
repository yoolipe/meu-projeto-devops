# Usar imagem oficial do Python
FROM python:3.11-slim

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar todos os arquivos do projeto para o container
COPY . .

# Instalar dependências (se houver)
RUN pip install --no-cache-dir -r requirements.txt || echo "Sem dependências"

# Comando para rodar a aplicação
CMD ["python", "app.py"]

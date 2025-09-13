# Imagem oficial do Python
FROM python:3.11-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar arquivos de dependência primeiro
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do projeto
COPY . .

# Expor a porta que a aplicação vai usar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]


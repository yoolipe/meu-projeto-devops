# Estágio 1: Build
# Usa uma imagem Python oficial como imagem base.
# A tag 'slim' indica uma versão mínima, sem ferramentas desnecessárias.
FROM python:3.9-slim as builder

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala as dependências de build (se necessário, para pacotes com extensões C)
# RUN apt-get update && apt-get install -y gcc

# Copia o arquivo de dependências primeiro para aproveitar o cache do Docker.
# A instalação das dependências só será executada novamente se o requirements.txt mudar.
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r 

# Estágio 2: Final
# Imagem final, leve e otimizada para produção
FROM python:3.9-slim

# Cria um usuário e grupo não-root para executar a aplicação por segurança
RUN addgroup --system app && adduser --system --ingroup app appuser
USER appuser

# Define o diretório de trabalho
WORKDIR /app

# Copia as dependências instaladas do estágio de build
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copia o código da aplicação para o diretório de trabalho
COPY . .

# Expõe a porta que o Flask usa (5000 por padrão)
EXPOSE 5000

# Comando para executar a aplicação.
# O host '0.0.0.0' é necessário para que o container aceite conexões externas.
CMD ["python", "app.py"]

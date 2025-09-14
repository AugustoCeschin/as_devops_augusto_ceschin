FROM python:slim-bullseye

WORKDIR /usr/src/app

# Copia e instala as dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Expõe porta
EXPOSE 80

# Comando de execução
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

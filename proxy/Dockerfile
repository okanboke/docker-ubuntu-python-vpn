FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt update && apt install -y iproute2 curl && apt clean

COPY . .

RUN chmod +x start.sh

CMD ["sh", "./start.sh"]

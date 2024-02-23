FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN \
    apt-get update && \
    apt-get install --yes \
        python3 \
        python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Note: Docker context refers to the root directory of the project.

COPY ./api-gateway-service/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

COPY ./api-gateway-service/src/ ./
COPY ./VERSION ./

CMD ["python3", "main.py"]

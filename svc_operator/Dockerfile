FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .

RUN apt update
RUN apt-get install -y golang
RUN go install github.com/google/go-jsonnet/cmd/jsonnet@latest
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY ../k8s k8s/

#CMD [ "python", "operator_main.py" ]
ENTRYPOINT ["sleep", "infinity"]
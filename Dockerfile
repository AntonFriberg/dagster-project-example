FROM python:3.10-slim

# Change working directory
WORKDIR /usr/src/app
ENV DAGSTER_HOME=/usr/src/app

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY ./dagster.yaml .
COPY  ./src .

CMD ["dagit", "-w", "workspace.yaml", "-h", "0.0.0.0", "-p", "3000"]

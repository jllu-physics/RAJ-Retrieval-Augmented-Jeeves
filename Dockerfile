FROM python:3.10-slim

# Set environment variables for noninteractive installs
ENV DEBIAN_FRONTEND=noninteractive

# Update + install Java 11 and required build tools
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gnupg2 \
    unzip \
    git \
    software-properties-common \
    && apt-get clean

# Add OpenJDK 11 manually (for compatibility with Anserini)
RUN wget https://download.oracle.com/java/21/latest/jdk-21_linux-x64_bin.tar.gz && \
    mkdir -p /opt/java && \
    tar -xzf jdk-21_linux-x64_bin.tar.gz -C /opt/java && \
    rm jdk-21_linux-x64_bin.tar.gz

ENV JAVA_HOME=/opt/java/jdk-21.0.6
ENV PATH="$JAVA_HOME/bin:$PATH"

# Install Maven
RUN apt-get update && apt-get install -y maven && apt-get clean

# Install Python deps
RUN pip install --no-cache-dir pyserini==0.44.0 fastapi uvicorn

RUN git clone https://github.com/castorini/anserini.git && cd anserini
#  && mvn clean package appassembler:assemble

# Create working directory
WORKDIR /app
COPY . /app

CMD ["uvicorn", "pyserini_search_api:app", "--host", "0.0.0.0", "--port", "8000"]

# To run docker
# go to the project root, open a terminal, do
# 1. docker build -t jeeves-pyserini-api .
# 2. docker run -p 8000:8000 -v $PWD/indexes/sample_collection_jsonl:/index jeeves-pyserini-api
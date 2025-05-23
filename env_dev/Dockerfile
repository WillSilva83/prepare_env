# Use uma imagem base específica
FROM ubuntu:22.04

# Configure o fuso horário para evitar prompts interativos
ENV TZ=America/Sao_Paulo
RUN apt-get update && apt-get install -y \
    tzdata && \
    ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Instale dependências essenciais
RUN apt-get update && apt-get install -y \
    openjdk-11-jdk \
    python3 \
    python3-venv \
    python3-distutils \
    curl \
    git-all \
    unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Configure python3 como padrão
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# Instale pip para Python 3
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

# Instale o AWS CLI V2
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf aws awscliv2.zip

# Verifique a instalação do AWS CLI
RUN aws --version

# Defina o JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

# Crie e ative um ambiente virtual com Python 3
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Instale o PySpark no ambiente virtual
RUN pip install --upgrade pip && \
    pip install pyspark==3.4.0

# Instale o Jupyter Notebook e dependências adicionais
RUN pip install notebook

# Configure o diretório de trabalho
WORKDIR /home

# Copie arquivos necessários para o diretório de trabalho
COPY ./dev /home

# Instale as dependências listadas no requirements.txt
COPY requirements.txt /home/requirements.txt
RUN pip install -r /home/requirements.txt

# Exponha a porta padrão do Jupyter Notebook
EXPOSE 8888

# Comando padrão para iniciar o Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

### README.md para o Dockerfile

```markdown
# Ambiente Docker com PySpark, AWS CLI e Jupyter Notebook

Este Dockerfile configura um ambiente Docker com suporte para desenvolvimento em PySpark, Jupyter Notebook e AWS CLI. Ele é ideal para processar dados em Spark e trabalhar com serviços da AWS.

---

## Recursos Incluídos

- **Base**: Ubuntu 22.04
- **Python**: Python 3.10 configurado com pip e ambiente virtual.
- **PySpark**: Versão 3.4.0 instalada.
- **Jupyter Notebook**: Para desenvolvimento interativo.
- **AWS CLI**: CLI da AWS para interações com serviços como S3, Glue, etc.
- **Ferramentas Essenciais**: curl, git, unzip e OpenJDK 11.

---

## Como Usar

### 1. Construir a Imagem
Clone este repositório e use o comando abaixo para construir a imagem:
```bash
docker build -t pyspark-aws-env .
```

### 2. Executar o Container
Inicie um container baseado na imagem criada:
```bash
docker run -it -p 8888:8888 pyspark-aws-env
```

### 3. Acessar o Jupyter Notebook
Após iniciar o container, o Jupyter Notebook estará disponível. No terminal do container, será exibido um link com um token para acessar o notebook. Abra o link no navegador.

Por exemplo:
```
http://127.0.0.1:8888/?token=<TOKEN>
```

Substitua `<TOKEN>` pelo token exibido no terminal.

---

## Personalização

### Adicionar Dependências Python
Para instalar pacotes adicionais, adicione-os ao arquivo `requirements.txt` antes de construir a imagem. Exemplo de arquivo `requirements.txt`:
```
boto3==1.24.0
faker==13.3.4
```

### Modificar a Configuração do Docker
Se precisar alterar o ambiente (por exemplo, instalar pacotes adicionais do sistema), edite o `Dockerfile` e reconstrua a imagem.

---

## Estrutura do Projeto

A estrutura do projeto é a seguinte:
```
/dev                 # Diretório com scripts e arquivos de desenvolvimento
Dockerfile           # Arquivo Dockerfile para criar a imagem
requirements.txt     # Arquivo com dependências Python
README.md            # Este arquivo
```

---

## Componentes Configurados

1. **AWS CLI**:
   - O CLI da AWS está instalado e pronto para uso.
   - Verifique a versão usando `aws --version`.

2. **PySpark**:
   - O PySpark está instalado e pode ser usado no notebook ou diretamente no Python.

3. **Jupyter Notebook**:
   - Está configurado para rodar no modo sem navegador (`--no-browser`).
   - Porta exposta: `8888`.

---

## Solução de Problemas

1. **Erro ao Acessar o Jupyter**:
   - Certifique-se de que o token está correto e a porta `8888` está liberada.

2. **Problemas com Pacotes**:
   - Verifique o arquivo `requirements.txt` para garantir que as versões dos pacotes estão corretas.
   - Recrie a imagem após alterações no `requirements.txt`.

3. **Erro ao Instalar Python**:
   - Caso precise de outra versão do Python, ajuste a imagem base no Dockerfile.

## API Financeiro

### Descrição
Tutorial original [aqui](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04-pt)


### Instruções
> Para Ubuntu 20.04
Instale o pyhton3 com os comandos abaixo:
```
sudo apt update && 
sudo apt install software-properties-common && 
sudo add-apt-repository ppa:deadsnakes/ppa && 
sudo apt update && 
sudo apt install python3.10 build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget python3.10-venv -y

```

##### Flask
Para instalar o qualquer dependência é preciso usar um ambiente de desenvolvimento virtual do python. Para isso abra a pasta do projeto e digite `python3 -m venv venv` e ative o ambiente `. venv/bin/activate`. 

> Nessa parte eu tive dificuldade porque o venv instalado era uma versão diferente, confira e se caso ocorrer o mesmo instale o venv da versão de seu python, exemplo: python3-3.suaversao-venv.

O seu terminal deve ficar com a tag **(venv)** ativada como no exemplo abaixo:

`(venv) gesiel@gesiel-PC:~/Documents/financeiro$ `

Agora instale o Flask com o comando `pip install Flask`.

Para testar podemos usar a linha de comando recomendada pela documentação.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

Para rodar o projeto agora primeiro exporte o FLASK_APP com o comando `export FLASK_APP=hello` e execute `flask run`.

Caso esteja rodando localmente acesso a url **http://127.0.0.1:5000/** e você verá sua mensagem de Hello World.

##### Gunicorn
Para instalar o Guinicorn use `pip install gunicorn`. Para executar use `gunicorn -w 4 app:app`.

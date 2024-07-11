![alt imagem de capa](./.github/wallpaper.png)
# NLW 16: Journey - Triha Python #
Este projeto é uma API backend desenvolvida em Python, como parte do evento NLW Journey da Rocketseat. O objetivo principal da API é facilitar o planejamento de viagens com amigos, permitindo a criação de planos de viagem, registro de atividades e armazenamento de links úteis.



### Funcionalidades

1 - Criação de Planos de Viagem: Permite a criação de diferentes planos de viagem com informações detalhadas.

2 - Registro de Atividades: Possibilita adicionar e gerenciar atividades específicas dentro de cada plano de viagem.

3 - Links Úteis: Armazenamento e gerenciamento de links úteis para facilitar o acesso a informações relevantes durante a viagem.

## Stacks utilizadas ##

### BACK-END ###

- [Python](https://www.python.org/)
- [Flask](https://pypi.org/project/Flask/)
- [Virtualenv](https://pypi.org/project/virtualenv/)
- [Pytest](https://docs.pytest.org/en/8.2.x/)
- [Pylint](https://docs.pytest.org/en/8.2.x/)
- [Sqlite](https://sqlite.com/)


## Funcionalidades da Aplicação ##

### - schema.sql

CREATE TABLE IF NOT EXISTS 'trips' (
    id TEXT PRIMARY KEY,
    destination TEXT NOT NULL,
    start_date DATETIME,
    end_date DATETIME,
    owner_name TEXT NOT NULL,
    owner_email TEXT NOT NULL,
    status INTEGER -- 1 para verdadeiro (true), 0 para falso (false)
);

CREATE TABLE IF NOT EXISTS 'emails_to_invite' (
    id TEXT PRIMARY KEY,
    trip_id TEXT,
    email TEXT NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trips(id)
);

CREATE TABLE IF NOT EXISTS 'links' (
    id TEXT PRIMARY KEY,
    trip_id TEXT,
    link TEXT NOT NULL,
    title TEXT NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trips(id)
);

CREATE TABLE IF NOT EXISTS 'participants' (
    id TEXT PRIMARY KEY,
    trip_id TEXT NOT NULL,
    emails_to_invite_id TEXT NOT NULL,
    name TEXT NOT NULL,
    is_confirmed INTEGER, -- 1 para verdadeiro (true), 0 para falso (false)
    FOREIGN KEY (trip_id) REFERENCES trips(id),
    FOREIGN KEY (emails_to_invite_id) REFERENCES emails_to_invite(id)
);

CREATE TABLE IF NOT EXISTS 'activities' (
    id TEXT PRIMARY KEY,
    trip_id TEXT NOT NULL,
    title TEXT NOT NULL,
    occurs_at DATETIME,
    FOREIGN KEY (trip_id) REFERENCES trips(id)
);

## Modelagem de entidade e relacionamento - MER

![MER](/mer.png "Modelagem de entidade e relacionamento")

## Documentação da API
- https://documenter.getpostman.com/view/24656609/2sA3e5cSuM


## Clonando e executando o app ##

1. Clone o repositório usando o comando:

```bash
git clone https://github.com/Humberto08/upload-ai-nlw.git
```

2. Navegue para o diretório raiz do projeto e instale as dependências backend:


3. Crie um ambiente virtual:

```bash
python -m venv venv

```

4. Ative o ambiente virtual:

No Windows
```bash
venv\Scripts\activate

```

No macOS/Linux
```
source venv/bin/activate
```

5. Instale as dependências:
Instale as dependências listadas no arquivo requirements.txt:
```
pip install -r requirements.txt
```

6. Execute o projeto:

```bash
 python3 run.py    
```



```

<div id='contatos' align="center">
  <p align="center">Made with 💜 by Humberto Luciano</p>
  <div id="contatos" align="center">
    <a href="https://www.linkedin.com/in/humberto-luciano/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
</div>





# Gerenciador de Tarefas com Flask

Este exemplo mostra uma interface web simples usando Programação Orientada a Objetos.

## O que é frontend

```text
HTML + CSS
```

O frontend é a parte que aparece no navegador. Neste exemplo, o HTML mostra o formulário e a lista de tarefas, e o CSS cuida da aparência.

## O que é backend

```text
Python + Flask + classes
```

O backend recebe as ações do usuário. O Flask chama os métodos das classes Python para adicionar e concluir tarefas.

## Estrutura

```text
exemplo_interface_web/
├── app.py
├── main.py
├── README.md
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Fluxo

```text
Usuário
↓
HTML
↓
Flask
↓
Classes Python
↓
Flask
↓
HTML
```

## Como executar no Windows

No terminal, entre na pasta `exemplo_interface_web` e execute:

```cmd
py -m pip install -r requirements.txt
py app.py
```

Depois, abra este endereço no navegador:

```text
http://127.0.0.1:5000
```

## Observação

As tarefas ficam somente na memória. Elas desaparecem quando o servidor é encerrado. Isso é proposital para manter o exemplo simples e focado na ligação entre HTML/CSS, Flask e classes Python.

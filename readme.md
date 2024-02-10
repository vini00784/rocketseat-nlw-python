# NLW - Python

## Criando ambiente virtual
Para que os comandos sejam executados dentro de um ambiente virtual, basta instalar o virtual env através do comando: 

```
    pip install virtualenv
```

E para acessá-lo, através do cmd do windows, basta rodar o comando:

```
    .venv\Scripts\activate
```

## Formatação do código
Para isso iremos instalar o pylint rodando o comando:

```
    pip install pylint
```

É preciso também baixar a extensão PyLint do vscode, e para gerar um arquivo de configuração, rode o comando:

```
    pylint --generate-rcfile > .pylintrc
```

## Verificação do código antes de commits
Como um "husky" da vida, iremos fazer com que o pylint seja rodado antes de todo commit para que não haja possibilidade de subir arquivos que estejam malformatados e para isso instalaremos a lib pre-commit através do comando:

```
    pip install pre-commit
```

Crie na raíz um arquivo chamado .pre-commit-config.yaml e dentro dele coloque o conteúdo:

```
    repos:
      - repo: local
        hooks:
          - id: pylint
            name: pylint
            entry: pylint
            language: system
            types: [python]
            args:
              [
                "-rn", # Only display messages
                "-sn", # Don't display the score
                "--rcfile=.pylintrc", # Link to yout config file
                "--load-plugins=pylint.extensions.docparams" # Load an extension
              ]
```
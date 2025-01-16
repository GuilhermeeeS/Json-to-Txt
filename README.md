# JSON-to-Text Converter 
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height=50/>

- Este repositório contém um script automatizado para converter arquivos JSON em arquivos de texto formatados e indentados (.txt). O script utiliza a biblioteca watchdog para monitorar uma pasta específica no desktop (chamada "Json") em busca de novos arquivos JSON. Quando um arquivo é adicionado, ele é automaticamente convertido e salvo em uma outra pasta no desktop (chamada "Txt").

## Funcionalidades
- Monitoramento contínuo da pasta "Json" em busca de novos arquivos JSON.
- Conversão automática do JSON para um arquivo de texto (.txt) com formatação indentada.
- Suporte a diferentes codificações de arquivos (UTF-8 e ISO-8859-1).
- Garante que os arquivos convertidos sejam salvos com nomes únicos na pasta "Txt".

## Como usar

1. Clone este repositório para sua máquina.

2. Certifique-se de ter a biblioteca watchdog instalada:

~~~
pip install watchdog
~~~

3. Execute o script ( Conversor.py )
~~~
python nome_do_arquivo.py
~~~

4. Adicione arquivos JSON à pasta "Json" localizada no seu desktop. Os arquivos convertidos serão salvos automaticamente na pasta "Txt".

## Requisitos

- Python 3.6 ou superior
- Biblioteca ```Watchdog```

## Personalização

- O caminho das pastas "Json" e "Txt" pode ser alterado no código, modificando as variáveis ```source_dir``` e ```destination_dir```.



# Gerador de Senhas Fortes

Este é um script Python que gera senhas aleatórias e seguras, com opções personalizáveis para atender às suas necessidades de segurança. Ele permite que você defina o tamanho da senha, escolha os tipos de caracteres a incluir (letras maiúsculas, minúsculas, números e símbolos), além de evitar caracteres ambíguos (como "O", "0", "I" e "l").

## Funcionalidades

- **Tamanho Personalizável**: Defina o tamanho mínimo e máximo da senha gerada.
- **Inclusão de Caracteres**: Escolha se deseja incluir letras maiúsculas, minúsculas, números e símbolos.
- **Evitar Caracteres Ambíguos**: Evita caracteres que podem ser confundidos (como "O", "0", "I" e "l").
- **Copia para Área de Transferência**: A senha gerada é automaticamente copiada para a área de transferência.
- **Armazenamento**: Opcionalmente, a senha gerada pode ser salva em um arquivo de texto.

## Tecnologias

- `random` – Para gerar caracteres aleatórios.
- `secrets` – Para garantir maior segurança na geração das senhas.
- `argparse` – Para permitir a personalização do script via linha de comando.
- `pyperclip` – Para copiar a senha para a área de transferência.

## Instalação

Para rodar o script, é necessário ter o Python instalado em sua máquina. Além disso, o pacote `pyperclip` deve ser instalado para permitir o recurso de copiar a senha para a área de transferência.

### Instalar dependências

```bash
pip install pyperclip
```

## Como Usar
Clone este repositório em sua máquina local:

```bash
git clone https://github.com/pkaarina/gerador_de_senhas_em_python.git
cd gerador_de_senhas_em_python
```

Execute o script gerador_senhas.py com os parâmetros desejados:

```bash
python gerador_senhas.py
```
 
Opções

`--t ou --tamanho` – Define o tamanho da senha gerada (padrão: 12).

`--sem-maiusculas` - Exclui letras maiúsculas da senha gerada.

`--sem-minusculas` - Exclui letras minúsculas da senha gerada.

`--sem-numeros` - Exclui números da senha gerada.

`--sem-simbolos` - Exclui símbolos da senha gerada.

`--salvar` - Salva a senha gerada no arquivo senhas.txt.



## Exemplos de Uso

Gerar uma senha padrão de 12 caracteres (com todos os tipos de caracteres):

```bash
python gerador_de_senhas.py
```


Gerar uma senha com 16 caracteres, sem números e sem símbolos:

```bash
python gerador_de_senhas.py -t 16 --sem-numeros --sem-simbolos
```

Gerar uma senha e salvar em um arquivo:

```bash
python gerador_de_senhas.py --salvar
```

## ***Contribuição***

Sinta-se à vontade para fazer um fork deste repositório, criar uma branch com suas melhorias e abrir um pull request.


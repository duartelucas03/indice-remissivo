## Índice remissivo

Projeto criado para criar um índice sobre o arquivo de texto lido baseado em Python.

## Descrição

O projeto `indice-remissivo` é projetado para ajudar os usuários a criar e gerenciar índices de forma eficiente usando árvore AVL baseado em Python. Este projeto pode ser personalizado para atender a várias necessidades relacionadas à indexação. Ele consiste basicamente na leitura de um arquivo e no retorno de informações sumarizadas sobre a linha em que cada palavra aparece, além do índice ao fim do arquivo, contendo:
- Total de palavras
- Total de palavras distintas
- Palavras descartadas
- Tempo de construção
- Total de rotações

*Obs:* O arquivo `shrek.txt` foi utilizado como exemplo para o `indice-remissivo` no código.

## Requisitos

- Python

```bash
https://www.python.org/downloads/
```

## Uso

Para usar este projeto, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/duartelucas03/indice-remissivo.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd indice-remissivo
   ```
3. Execute o script principal:
   ```bash
   python main.py
   ```

## Funcionalidades

- **Inserção e Balanceamento**: A árvore é balanceada automaticamente após a inserção de cada nova palavra.
- **Busca**: Permite buscar uma palavra específica e verificar em quantas linhas ela aparece.
- **Geração de Índice Remissivo**: Cria um arquivo `indice_remissivo.txt` que lista todas as palavras distintas e suas respectivas linhas.
- **Frequência de Palavras**: Identifica qual palavra aparece no maior número de linhas.

## Estrutura do Projeto

O projeto contém os seguintes arquivos:

- **`no.py`**: Define a classe `NO`, que representa os nós da árvore AVL. Cada nó armazena a informação (a palavra), sua altura, os ponteiros para os filhos esquerdo e direito, e uma lista com as linhas em que a palavra aparece.
  
- **`avl.py`**: Implementa a classe `AVL`, que contém as funções necessárias para inserir palavras, balancear a árvore (rotacionar), buscar palavras, e gerar o índice remissivo. As funções principais incluem:
  - Inserção de palavras mantendo o balanceamento da árvore.
  - Busca de palavras e verificação da frequência em diferentes linhas.
  - Geração do arquivo `indice_remissivo.txt` contendo o índice remissivo.
avl.py: Implementa a classe AVL, que contém as funções necessárias para inserir palavras, balancear a árvore (rotacionar), buscar palavras, e gerar o índice remissivo. As funções principais incluem:

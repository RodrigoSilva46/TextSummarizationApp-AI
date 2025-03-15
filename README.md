# README - Sumarização de Texto com LangChain e Claude-3

Este projeto demonstra como utilizar a biblioteca **LangChain** em conjunto com o modelo de linguagem **Claude-3** da Anthropic para realizar a sumarização de textos. O código é dividido em blocos que explicam cada etapa do processo, desde a importação das bibliotecas até a execução da sumarização.

---

## 📋 Tabela de Conteúdos
1. [Requisitos](#-requisitos)
2. [Configuração do Ambiente](#-configuração-do-ambiente)
3. [Explicação do Código](#-explicação-do-código)
4. [Como Executar o Projeto](#-como-executar-o-projeto)
5. [Estrutura do Projeto](#-estrutura-do-projeto)

---

## 🛠️ Requisitos

Antes de executar o projeto, certifique-se de ter os seguintes requisitos instalados:

- Python 3.8 ou superior
- `pip` (gerenciador de pacotes do Python)
- `venv` (para criar um ambiente virtual)

---

## ⚙️ Configuração do Ambiente

### 1. Clonar o Repositório
Primeiro, clone o repositório do GitHub para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2. Criar e Ativar um Ambiente Virtual
Utilize o `venv` para criar um ambiente virtual e isolar as dependências do projeto:

```bash
python -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate
```

### 3. Instalar as Dependências
Instale as bibliotecas necessárias utilizando o `pip`:

```bash
pip install langchain-anthropic python-dotenv
```

### 4. Configurar Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API da Anthropic:

```ini
ANTHROPIC_API_KEY=sua_chave_aqui
```

---

## 📜 Explicação do Código

### 1. Importação das Bibliotecas
```python
from langchain_anthropic import ChatAnthropic
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv, find_dotenv
import os
```

- **ChatAnthropic**: Interface para interagir com o modelo Claude-3.
- **Document**: Estrutura para representar documentos textuais.
- **CharacterTextSplitter**: Divide textos longos em partes menores.
- **load_summarize_chain**: Cadeia de sumarização pré-configurada.
- **dotenv**: Carrega variáveis de ambiente de um arquivo `.env`.
- **os**: Acessa variáveis de ambiente do sistema.

---

### 2. Carregamento das Variáveis de Ambiente
```python
load_dotenv(find_dotenv())
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
```

- Carrega a chave da API da Anthropic do arquivo `.env`.
- A chave é armazenada na variável `ANTHROPIC_API_KEY`.

---

### 3. Criação do Modelo de IA
```python
llm = ChatAnthropic(
    model="claude-3-opus-20240229",
    temperature=0,
    anthropic_api_key=ANTHROPIC_API_KEY
)
```

- **model**: Define o modelo a ser utilizado (`claude-3-opus-20240229`).
- **temperature**: Controla a criatividade do modelo (0 = respostas determinísticas).
- **anthropic_api_key**: Autentica o acesso à API da Anthropic.

---

### 4. Definição do Texto de Entrada
```python
text = """
Elon Musk co-founded and leads Tesla, SpaceX, Neuralink and The Boring Company.
...
"""
```

- Texto de exemplo sobre Elon Musk e suas empresas.
- Será utilizado como entrada para a sumarização.

---

### 5. Divisão do Texto
```python
text_splitter = CharacterTextSplitter()
texts = text_splitter.split_text(text)
```

- Divide o texto em partes menores para facilitar o processamento.
- **CharacterTextSplitter**: Utiliza tamanho fixo de chunks (configurável).

---

### 6. Criação de Documentos
```python
docs = [Document(page_content=text) for text in texts]
```

- Transforma cada parte do texto em um objeto `Document`.
- **List comprehension**: Cria uma lista de documentos de forma eficiente.

---

### 7. Configuração da Cadeia de Sumarização
```python
chain = load_summarize_chain(llm=llm, chain_type="stuff")
```

- **chain_type="stuff"**: Processa todo o texto de uma vez (ideal para textos curtos).
- Alternativas: `map_reduce` (para textos longos) ou `refine` (para maior precisão).

---

### 8. Execução e Exibição do Resumo
```python
summary = chain.invoke(docs)
print(summary['output_text'])
```

- **invoke(docs)**: Executa a cadeia de sumarização nos documentos.
- **output_text**: Contém o texto resumido gerado pelo modelo.

---

## 🚀 Como Executar o Projeto

1. Ative o ambiente virtual (se ainda não estiver ativado):
   ```bash
   source venv/bin/activate  # No Windows, use: venv\Scripts\activate
   ```

2. Execute o script Python:
   ```bash
   python nome_do_arquivo.py
   ```

3. O resumo do texto será exibido no terminal.

---

## 📂 Estrutura do Projeto

```
nome-do-repositorio/
│
├── venv/                  # Ambiente virtual (gerado automaticamente)
├── .env                   # Arquivo de variáveis de ambiente
├── nome_do_arquivo.py     # Script principal
├── README.md              # Este arquivo
└── requirements.txt       # Dependências do projeto (opcional)
```

---

## 📝 Observações Finais

- Certifique-se de que a chave da API da Anthropic está corretamente configurada no arquivo `.env`.
- Para textos muito longos, considere utilizar `chain_type="map_reduce"` ou `chain_type="refine"`.
- O ambiente virtual (`venv`) é recomendado para evitar conflitos de dependências.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

# IMPORTANDO AS BIBLIOTECAS
from langchain_anthropic import ChatAnthropic                   # Importando a biblioteca anthropic
from langchain.docstore.document import Document                # Importando a biblioteca Document permite a criação de documentos
from langchain.text_splitter import CharacterTextSplitter       # Importando a biblioteca CharacterTextSplitter que permite a divisão de texto
from langchain.chains.summarize import load_summarize_chain     # Importando a biblioteca load_summarize_chain que permite a sumarização de texto
from dotenv import load_dotenv, find_dotenv                     # Importando a biblioteca dotenv que permite a leitura de variáveis de ambiente
import os                                                       # Importando a biblioteca os que permite a manipulação de variáveis de ambiente

# CARREGANDO AS VARIÁVEIS DE AMBIENTE
load_dotenv(find_dotenv())
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]

# CRIAR MODELO AI
llm = ChatAnthropic(
    model = "claude-3-opus-20240229",
    temperature= 0, # Ajusta o nível de criatividade do modelo
    anthropic_api_key = ANTHROPIC_API_KEY
)

text = """
Elon Musk co-founded and leads Tesla, SpaceX, Neuralink and The Boring Company.

As the co-founder and CEO of Tesla, Elon leads all product design, engineering and global manufacturing of the company's electric vehicles, battery products and solar energy products.

Since the company’s inception in 2003, Tesla’s mission has been to accelerate the world’s transition to sustainable energy. The first Tesla product, the Roadster sports car, debuted in 2008, followed by the Model S sedan, which was introduced in 2012, and the Model X SUV, which launched in 2015. Model S received Consumer Reports’ Best Overall Car and has been named the Ultimate Car of the Year by Motor Trend, while Model X was the first SUV ever to earn 5-star safety ratings in every category and sub-category in the National Highway Traffic Safety Administration’s tests. In 2017, Tesla began deliveries of Model 3, a mass-market electric vehicle with more than 320 miles of range, and unveiled Tesla Semi, which is designed to save owners at least $200,000 over a million miles based on fuel costs alone. In 2019, Tesla unveiled Cybertruck, which will have better utility than a traditional truck and more performance than a sports car, as well as the Model Y compact SUV, which began customer deliveries in early 2020.

"""
# SPLIT TEXT : Fatiamento do Texto
text_splitter = CharacterTextSplitter()
texts = text_splitter.split_text(text)

# CREATE DOCUMENTS : CRIAÇÃO DE DOCUMENTOS
docs = [Document(page_content=text) for text in texts] # List Comprenhension

# Summarização dos textos
chain = load_summarize_chain(llm=llm, chain_type="stuff")

#Executar a Chain
summary = chain.invoke(docs) # Executa a cadeia de resumo dos textos]

print(summary['output_text']) # Exibe o resumo do texto
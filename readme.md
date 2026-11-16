# PB Juizados Especiais — TP4

**Autora:** Carolina Gabriela Mesquita.

Projeto acadêmico para comparar o tempo médio até a sentença nos Juizados Especiais dos 27 Tribunais de Justiça, utilizando dados de 2025 do CNJ.
O TP4 acrescenta um modelo de linguagem local ao backend FastAPI para produzir explicações textuais sobre comparações fornecidas na entrada.

## Funcionalidades

- painel Streamlit com quatro páginas;
- consultas, filtros, tabelas, gráficos e download de CSV;
- dados estatísticos obtidos pelo GET `/tribunais`;
- notícias do CNJ como informações de contexto;
- recebimento de observações pela API e armazenamento em `data/observacoes.csv`;
- geração de explicações pelo POST `/processar_texto`;
- respostas estruturadas com Pydantic e tratamento de erros.

## Modelo escolhido

Foi utilizado `TinyLlama/TinyLlama-1.1B-Chat-v1.0`, executado na CPU, com `bfloat16`, `max_new_tokens=256` e `do_sample=False`.

Nos testes do notebook, duas comparações tiveram os valores e a direção da diferença preservados. Os tempos observados foram de 16,4 e 21,2 segundos. A memória calculada para os parâmetros foi de aproximadamente 2,2 GB; esse valor não representa a RAM total utilizada pela aplicação.

A justificativa completa está em `docs/escolha_modelo.docx`.

## Instalação e execução

Na pasta do projeto, instale as dependências:

```powershell
python -m pip install -r requirements-api.txt
```

Inicie a API em um terminal:

```powershell
python -m uvicorn api.main:app
```

Aguarde `Application startup complete`. Na primeira execução, é necessária conexão com a internet para baixar o modelo. Depois do download, o carregamento e a geração foram testados sem internet.

Em outro terminal, inicie o aplicativo:

```powershell
python -m streamlit run app.py
```

Endereços locais:

- aplicativo: http://localhost:8501
- documentação da API: http://127.0.0.1:8000/docs

Os dois processos precisam permanecer em execução para o funcionamento integrado do painel.

## Uso do LLM

Em `/docs`, execute POST `/processar_texto` com:

```json
{
  "texto": "Ano: 2025\nIndicador: tempo médio até a sentença nos Juizados Especiais\nTribunal com menor tempo: TJDFT\nTempo do TJDFT: 90,1 dias\nTribunal com maior tempo: TJSE\nTempo do TJSE: 111,7 dias\nDiferença: 21,6 dias"
}
```

A resposta contém `texto`, `tipo_analise` e `resultado`.

Entradas ausentes, de tipo incorreto, vazias ou contendo somente espaços são recusadas com 422. Se o modelo não estiver disponível, a rota retorna 503 com uma mensagem explicativa, enquanto as outras rotas continuam funcionando.

## Ajustes decorrentes do feedback do TP3

- O GET passou a alimentar tabelas e gráficos.
- As observações passaram a ser gravadas em CSV e recuperadas na inicialização.
- A tarefa efetiva do LLM foi registrada no Project Charter e no Data Summary Report.
- O endereço da API foi centralizado em `comum.py`.

## Limitações

A configuração atual é destinada à execução local. Um aplicativo publicado precisaria acessar uma API disponível em endereço alcançável pela hospedagem.

A saída do LLM é consultada pela API, em `/docs`; ainda não há interface de geração no Streamlit. O modelo pode incluir os rótulos “Dados” e “Resposta”. Os dois casos avaliados não representam uma medida geral de precisão.

O indicador é agregado por tribunal e não representa a duração de processos individuais.

## Fontes e apoio

- Conselho Nacional de Justiça — Justiça em Números e notícias dos Juizados Especiais.
- Organização das Nações Unidas — ODS 16.
- ChatGPT — apoio na orientação de código e revisão da documentação. Apoio na correção gramatical e ajuste na fluidez dos textos. Apoio na complementação da documentação. A execução e a conferência dos resultados foram realizadas pela autora.
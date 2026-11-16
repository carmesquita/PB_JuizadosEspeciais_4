# Data Summary Report — TP4 Juizados Especiais

**Autora:** Carolina Gabriela Mesquita.

## Dados utilizados

| Fonte | Tipo | Objetivo | Resumo e limitações |
|---|---|---|---|
| Justiça em Números/CNJ | CSV estruturado | comparar o tempo médio até a sentença | 27 tribunais, ano de 2025, sem valores ausentes no arquivo processado. O indicador é agregado por tribunal |
| Notícias dos Juizados Especiais/CNJ | HTML | apresentar informações de contexto | dez notícias coletadas por requisições HTTP e Beautiful Soup. São utilizados metadados e trechos, não o conteúdo integral dos artigos |
| CSV enviado pelo usuário | CSV estruturado | acrescentar informações complementares | deve conter `tribunal`, `observacao` e `fonte` |
| Observações enviadas pela API | JSON, armazenado em CSV | registrar informações sem alterar a base oficial | registros com tribunal, observação, fonte e identificador, salvos em `data/observacoes.csv` |

## Arquivos e integração

`tempo_sentenca_juizados.csv` contém ano, tribunal, nome do tribunal, UF, tempo médio até a sentença e quantidade de sentenças de conhecimento.

A API lê essa base e disponibiliza os dados pelo GET `/tribunais`. O Streamlit utiliza o retorno para alimentar suas tabelas e gráficos.

As notícias permanecem em `noticias_juizados.csv`. O arquivo `noticias_para_llm.csv`, preparado no TP3, foi mantido como parte do trabalho anterior. A tarefa de LLM escolhida para o TP4 utiliza os dados das comparações entre tribunais.

## Processamento com LLM

O TinyLlama recebe um texto com ano, tribunais, tempos médios e diferença. A saída é uma explicação textual em português.

O POST `/processar_texto` devolve os campos:

- `texto`: entrada recebida;
- `tipo_analise`: comparação;
- `resultado`: texto produzido pelo modelo.

Os testes com TJDFT/TJSE e TJBA/TJMA preservaram os valores e a indicação de menor e maior tempo. A amostra é pequena e a conferência dos resultados continua necessária.

Entradas inválidas são recusadas com 422. A indisponibilidade do modelo é informada com 503, mantendo as demais rotas disponíveis.

## Atendimento ao feedback do TP3

O GET passou a alimentar o painel, as observações passaram a ser persistidas em CSV e a tarefa efetiva do LLM foi registrada neste relatório e no Project Charter.

## Decisão sobre a coleta

As fontes atuais são acessadas por arquivos estruturados, requisições HTTP e Beautiful Soup. O Selenium permanece reservado para uma eventual fonte que exija interação dinâmica.

As fontes e o apoio de IA estão declarados no README.
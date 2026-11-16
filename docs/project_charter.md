# Project Charter - TP3 Juizados Especiais

**Autora:** Carolina Gabriela Mesquita

## Problema

Os dados do CNJ permitem comparar o tempo médio até a sentença nos Juizados Especiais, mas essa comparação não é apresentada de forma simples para todos os Tribunais de Justiça.

**Pergunta do projeto:** como o tempo médio até a sentença varia entre os 27 Tribunais de Justiça?

## Escopo

A aplicação apresenta dados de 2025, consultas e comparações entre tribunais, notícias de contexto e informações complementares.

No TP4, o modelo TinyLlama foi integrado ao FastAPI para transformar os resultados de uma comparação em uma explicação textual em português.

A entrada informa ano, siglas, tempos e diferença. A tarefa do modelo é preservar esses dados ao produzir a explicação. O foco do LLM nesta etapa é a comparação dos Juizados Especiais.

Ficam fora do escopo a análise de processos individuais, a previsão de prazos e a avaliação de magistrados.

## Objetivos e critérios de sucesso

- apresentar os dados dos 27 tribunais;
- permitir consultas, filtros, tabelas, gráficos e download;
- manter a aplicação organizada em quatro páginas;
- obter os dados estatísticos pela API;
- receber e persistir observações complementares em CSV;
- executar o LLM localmente por meio do POST /processar_texto;
- retornar JSON com texto, tipo de análise e resultado;
- recusar entradas inválidas e informar a indisponibilidade do modelo.


## Público e ODS

O público é formado pelo professor, alunos e pessoas interessadas em dados públicos da Justiça. O tema está relacionado à ODS 16, sobre acesso à Justiça e instituições eficazes.


## Riscos

O modelo pode produzir informações incorretas, por isso a fidelidade dos valores e das siglas deve ser conferida. Os testes realizados são limitados a exemplos de comparação e não medem a precisão geral do modelo.

A escolha do modelo está documentada em docs/escolha_modelo.docx. As fontes e o apoio de IA estão declarados no README.
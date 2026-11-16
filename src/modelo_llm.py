import torch
from transformers import GenerationConfig, pipeline


def carregar_modelo():
    # Teste temporário: falha no carregamento do modelo.
    #raise ValueError("Falha simulada no carregamento do modelo.")
    pipe = pipeline(
        "text-generation",
        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        dtype=torch.bfloat16,
        device=torch.device("cpu"),
    )
    pipe.model.generation_config.max_length = None
    return pipe


def gerar_comparacao(pipe, texto):
    prompt = pipe.tokenizer.apply_chat_template(
        [
            {
                "role": "system",
                "content": "Você explica dados dos Juizados Especiais em português.",
            },
            {
                "role": "user",
                "content": f"""TAREFA
Transforme o resultado abaixo em uma única frase em português.
Preserve os valores e a indicação de menor e maior tempo.
Use apenas as siglas fornecidas para identificar os tribunais.

EXEMPLO FICTÍCIO DE FORMATO
Dados: ano 2024; menor tempo: TJA, 100 dias;
maior tempo: TJB, 150 dias; diferença: 50 dias.

Resposta: Em 2024, o TJA apresentou tempo médio até a sentença
de 100 dias, ficando 50 dias abaixo do TJB, que registrou 150 dias.

O exemplo mostra somente o formato.
Escreva sua resposta usando os dados da seção
RESULTADO DA COMPARAÇÃO abaixo.

RESULTADO DA COMPARAÇÃO
{texto}

FORMATO
Somente a frase solicitada, sem expandir as siglas nem
acrescentar informações.""",
            },
        ],
        tokenize=False,
        add_generation_prompt=True,
    )

    return pipe(
        prompt,
        max_length=None,
        generation_config=GenerationConfig(
            max_new_tokens=256,
            do_sample=False,
        ),
        return_full_text=False,
    )[0]["generated_text"]
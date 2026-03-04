from crewai import Task


def criar_tarefa_thumbnail(agente_criador_thumbnail, tarefa_roteiro):
    return Task(
        description=(
            "Com base no roteiro gerado para o vídeo sobre '{consulta}', crie 3 opções de "
            "thumbnails chamativas para YouTube.\n\n"
            "Para cada thumbnail, você deve:\n"
            "1. Criar uma descrição detalhada do visual da thumbnail\n"
            "2. Usar a ferramenta de geração de imagem com um prompt detalhado em inglês\n"
            "3. A thumbnail deve ter elementos visuais impactantes relacionados ao conteúdo do vídeo\n\n"
            "Diretrizes para as thumbnails:\n"
            "- Use cores vibrantes e contrastantes\n"
            "- Inclua elementos de games relevantes ao tema\n"
            "- O design deve ser limpo mas impactante\n"
            "- Pense em composições que funcionem bem em tamanho pequeno (como aparece no feed do YouTube)\n"
            "- Cada opção deve ter um estilo visual diferente\n\n"
            "Gere as 3 imagens usando a ferramenta disponível e descreva cada uma."
        ),
        expected_output=(
            "3 opções de thumbnails geradas com:\n"
            "- Descrição visual detalhada de cada thumbnail\n"
            "- O prompt utilizado para gerar cada imagem\n"
            "- O caminho de cada arquivo de imagem gerado\n"
            "- Justificativa do porquê cada design seria efetivo para atrair cliques"
        ),
        agent=agente_criador_thumbnail,
        context=[tarefa_roteiro],
    )

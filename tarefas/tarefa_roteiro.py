from crewai import Task


def criar_tarefa_roteiro(agente_roteirista):
    return Task(
        description=(
            "Pesquise sobre o tema '{consulta}' e crie um roteiro detalhado para um vídeo de YouTube "
            "no segmento de videogames.\n\n"
            "O roteiro deve conter:\n"
            "1. **Gancho Inicial** - Uma abertura impactante para prender o espectador nos primeiros 10 segundos\n"
            "2. **Introdução** - Apresentação do tema e do que será abordado no vídeo\n"
            "3. **Desenvolvimento** - Conteúdo principal dividido em tópicos claros, com dados e curiosidades\n"
            "4. **Momentos de Destaque** - Partes do roteiro que merecem ênfase visual ou sonora\n"
            "5. **Call to Action** - Momento para pedir likes, inscrição e comentários\n"
            "6. **Conclusão** - Resumo e encerramento envolvente\n"
            "7. **Sugestões de Edição** - Dicas de cortes, transições e efeitos visuais\n\n"
            "Use a ferramenta de pesquisa para buscar informações atualizadas sobre o tema."
        ),
        expected_output=(
            "Um roteiro completo e detalhado em português para um vídeo de YouTube sobre games, "
            "formatado em Markdown, contendo todas as seções solicitadas. "
            "O roteiro deve ser envolvente, informativo e otimizado para engajamento."
        ),
        agent=agente_roteirista,
    )

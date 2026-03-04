from crewai import Task


def criar_tarefa_revisao(agente_revisor, tarefa_roteiro, tarefa_thumbnail):
    return Task(
        description=(
            "Revise o roteiro e as thumbnails geradas para o vídeo sobre '{consulta}'.\n\n"
            "Suas responsabilidades:\n"
            "1. **Revisão do Roteiro**:\n"
            "   - Corrija erros de gramática e ortografia\n"
            "   - Melhore a fluidez e coesão do texto\n"
            "   - Verifique se o roteiro está envolvente e otimizado para YouTube\n"
            "   - Garanta que todas as seções estão presentes e bem desenvolvidas\n\n"
            "2. **Escolha da Thumbnail**:\n"
            "   - Analise as 3 opções de thumbnails geradas\n"
            "   - Escolha a melhor opção com justificativa detalhada\n"
            "   - Considere: impacto visual, relevância ao conteúdo, potencial de CTR\n\n"
            "3. **Documento Final**:\n"
            "   - Compile tudo em um documento final organizado\n"
            "   - Inclua o roteiro revisado e a thumbnail escolhida"
        ),
        expected_output=(
            "Um documento final completo em Markdown contendo:\n"
            "1. O roteiro revisado e polido\n"
            "2. A thumbnail escolhida com justificativa\n"
            "3. Referências aos arquivos de imagem gerados\n\n"
            "O documento deve estar pronto para ser utilizado como guia de produção do vídeo."
        ),
        agent=agente_revisor,
        context=[tarefa_roteiro, tarefa_thumbnail],
        output_file="saida/resultado_final.md",
    )

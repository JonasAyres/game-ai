from crewai import Crew, Process

from agentes.roteirista import criar_roteirista
from agentes.criador_thumbnail import criar_criador_thumbnail
from agentes.revisor import criar_revisor
from tarefas.tarefa_roteiro import criar_tarefa_roteiro
from tarefas.tarefa_thumbnail import criar_tarefa_thumbnail
from tarefas.tarefa_revisao import criar_tarefa_revisao


def criar_equipe_video() -> Crew:
    roteirista = criar_roteirista()
    criador_thumbnail = criar_criador_thumbnail()
    revisor = criar_revisor()

    tarefa_roteiro = criar_tarefa_roteiro(roteirista)
    tarefa_thumbnail = criar_tarefa_thumbnail(criador_thumbnail, tarefa_roteiro)
    tarefa_revisao = criar_tarefa_revisao(revisor, tarefa_roteiro, tarefa_thumbnail)

    return Crew(
        agents=[roteirista, criador_thumbnail, revisor],
        tasks=[tarefa_roteiro, tarefa_thumbnail, tarefa_revisao],
        process=Process.sequential,
        verbose=True,
    )

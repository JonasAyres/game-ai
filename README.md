# 🎮 Game AI — Geração de Roteiros e Thumbnails para Vídeos de Games

Sistema automatizado que utiliza **múltiplos agentes de IA** para gerar roteiros detalhados e thumbnails profissionais para vídeos de YouTube no segmento de videogames.

Construído com [CrewAI](https://www.crewai.com/) e [Google Gemini](https://ai.google.dev/).

## 🧠 Agentes

| Agente                      | Função                                                                   | Ferramentas                |
| --------------------------- | ------------------------------------------------------------------------ | -------------------------- |
| **🎬 Roteirista**           | Pesquisa o tema e elabora um roteiro completo com storytelling           | Pesquisa na Web (Serper)   |
| **🎨 Criador de Thumbnail** | Gera 3 opções de thumbnails chamativas baseadas no roteiro               | Geração de Imagem (Gemini) |
| **📝 Revisor**              | Revisa o roteiro, escolhe a melhor thumbnail e compila o documento final | —                          |

## 📁 Estrutura do Projeto

```
Game-Ai/
├── main.py                        # Ponto de entrada
├── agentes/
│   ├── roteirista.py              # Agente roteirista com pesquisa web
│   ├── criador_thumbnail.py       # Agente designer de thumbnails
│   └── revisor.py                 # Agente revisor e editor
├── ferramentas/
│   └── gerador_imagem.py          # Ferramenta customizada de geração de imagens (Gemini)
├── tarefas/
│   ├── tarefa_roteiro.py          # Tarefa de criação do roteiro
│   ├── tarefa_thumbnail.py        # Tarefa de geração das thumbnails
│   └── tarefa_revisao.py          # Tarefa de revisão e compilação final
├── equipe/
│   └── equipe_video.py            # Configuração da Crew (orquestração)
├── saida/                         # Resultados gerados (roteiro + imagens)
├── .env                           # Chaves de API (não versionado)
├── .gitignore
└── requirements.txt
```

## 🚀 Como Executar

### Pré-requisitos

- Python 3.10+
- Chave de API do [Google Gemini](https://aistudio.google.com/apikey)
- Chave de API do [Serper](https://serper.dev/) (gratuita)

### Instalação

```bash
git clone https://github.com/JonasAyres/game-ai.git
cd game-ai
pip install -r requirements.txt
```

### Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
GEMINI_API_KEY=sua-chave-gemini-aqui
SERPER_API_KEY=sua-chave-serper-aqui
```

### Execução

```bash
python main.py
```

Ao executar, o sistema solicitará um tema para o vídeo. Exemplos:

```
📝 Digite o tema do vídeo: Melhores jogos de 2020
```

### Resultado

Após a execução, os resultados estarão na pasta `saida/`:

- `resultado_final.md` — Roteiro revisado + thumbnail escolhida
- `*.png` — Imagens das thumbnails geradas

## ⚙️ Tecnologias

- **[CrewAI](https://www.crewai.com/)** — Framework de orquestração de agentes IA
- **[Google Gemini 2.0 Flash](https://ai.google.dev/)** — LLM e geração de imagens
- **[Serper](https://serper.dev/)** — API de pesquisa na web
- **Python 3.12**

## 🔄 Fluxo de Execução

```
Usuário (tema) → Roteirista (pesquisa + roteiro) → Criador de Thumbnail (3 imagens)
                                                          ↓
                                          Revisor (revisão + escolha) → resultado_final.md
```

## 📄 Licença

Este projeto é de uso educacional.

import os
import base64
from pathlib import Path

from crewai.tools import BaseTool
from google import genai
from google.genai import types


class FerramentaGeracaoImagem(BaseTool):
    """Ferramenta para gerar imagens usando a API do Google Gemini."""

    name: str = "Gerador de Imagem"
    description: str = (
        "Gera uma imagem a partir de uma descrição textual detalhada. "
        "Recebe um prompt descrevendo a imagem desejada e retorna o caminho do arquivo salvo. "
        "Use descrições detalhadas e específicas para melhores resultados."
    )

    def _run(self, prompt: str) -> str:
        try:
            cliente = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

            resposta = cliente.models.generate_content(
                model="gemini-2.0-flash-exp",
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_modalities=["TEXT", "IMAGE"],
                ),
            )

            diretorio_saida = Path("saida")
            diretorio_saida.mkdir(exist_ok=True)

            nome_arquivo = prompt[:50].replace(" ", "_").replace("/", "_")
            nome_arquivo = "".join(c for c in nome_arquivo if c.isalnum() or c == "_")
            caminho_imagem = None

            for parte in resposta.candidates[0].content.parts:
                if parte.inline_data is not None:
                    dados_imagem = base64.b64decode(parte.inline_data.data)
                    caminho_imagem = diretorio_saida / f"{nome_arquivo}.png"
                    with open(caminho_imagem, "wb") as arquivo:
                        arquivo.write(dados_imagem)
                    break

            if caminho_imagem:
                return f"Imagem gerada com sucesso e salva em: {caminho_imagem}"

            return "Não foi possível gerar a imagem. Tente com um prompt diferente."

        except Exception as erro:
            return f"Erro ao gerar imagem: {str(erro)}"

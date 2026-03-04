import os
from dotenv import load_dotenv
from equipe.equipe_video import criar_equipe_video


def executar():
    load_dotenv()

    print("=" * 60)
    print("🎮 Sistema de Geração de Roteiros e Thumbnails para Games")
    print("=" * 60)

    tema = input("\n📝 Digite o tema do vídeo (ou Enter para usar o padrão): ").strip()

    if not tema:
        tema = "Melhores jogos de 2020"
        print(f"   Usando tema padrão: {tema}")

    print(f"\n🚀 Iniciando geração para: '{tema}'")
    print("-" * 60)

    equipe = criar_equipe_video()
    resultado = equipe.kickoff(inputs={"consulta": tema})

    print("\n" + "=" * 60)
    print("✅ Processo finalizado!")
    print("=" * 60)
    print(f"\n📄 Resultado salvo em: saida/resultado_final.md")
    print(f"\n{resultado}")


if __name__ == "__main__":
    executar()

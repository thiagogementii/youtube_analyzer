import os
from src.downloader import download_audio
from src.transcriber import transcribe_audio
from src.summarizer import summarize_text

OUTPUT_DIR = "output/transcriptions"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    url = input("🔗 Insira a URL do vídeo do YouTube: ").strip()

    print("⬇️  Baixando áudio...")
    audio_path = download_audio(url)

    print("🧠 Transcrevendo com Whisper...")
    transcription = transcribe_audio(audio_path)

    print("📝 Gerando resumo...")
    summary = summarize_text(transcription)

    base_name = os.path.join(OUTPUT_DIR, "output")
    with open(f"{base_name}_transcription.txt", "w", encoding="utf-8") as f:
        f.write(transcription)

    with open(f"{base_name}_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    print("✅ Transcrição e resumo salvos em:", OUTPUT_DIR)

if __name__ == "__main__":
    main()
